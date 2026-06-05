import pytest

@pytest.mark.regression
def test_get_users(api_context):
    response = api_context.get("/users")
    assert response.status == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0

@pytest.mark.regression
@pytest.mark.smoke
def test_create_user(api_context):
    new_user = {
        "title": "testing post",
        "body": "johndoe",
        "userId": 1
    }
    response = api_context.post("/posts", data=new_user)
    assert response.status == 201
    body = response.json()
    assert body["title"] == new_user["title"]
    assert body["body"] == new_user["body"]
    assert body["userId"] == new_user["userId"]

@pytest.mark.regression
def test_delete_user(api_context):
    response = api_context.delete("/posts/1")
    body = response.json()
    assert response.status == 200
    assert body == {}
