import requests

BASE = 'https://jsonplaceholder.typicode.com'

def test_get_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body, list)
    assert len(body) > 0



def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    r = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == "foo"


def test_delete_post(): 
    r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert r.status_code == 200 or r.status_code == 204
