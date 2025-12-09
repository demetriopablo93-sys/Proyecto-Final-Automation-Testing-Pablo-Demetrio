import pytest
from utils.driver_factory import create_driver
from utils.logger import get_logger
import os


logger = get_logger('pytest')

@pytest.fixture(scope='function')
def driver_scope(request):
    headless = os.getenv('HEADLESS', 'false').lower() == 'true'
    driver = create_driver(headless=headless)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver_scope, tmp_path):
# yield to test
    yield
# after test
    outcome = request.session.testscollected if False else None
# simpler: inspect request.node.rep_call
    rep = getattr(request.node, 'rep_call', None)
    if rep is None:
# pytest < 3.9: use request.node._report_sections? Keep it simple and try attribute
        pass


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
# hook to attach screenshot on failure
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get('driver_scope')
        if driver:
            folder = os.path.join(os.getcwd(), 'reports', 'screenshots')
            os.makedirs(folder, exist_ok=True)
            file_path = os.path.join(folder, f"{item.name}_{rep.when}.png")
            try:
                driver.save_screenshot(file_path)
                print(f"[screenshot] saved to {file_path}")
            except Exception as e:
                print('Could not save screenshot:', e)