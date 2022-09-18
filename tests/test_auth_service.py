import json


class TestAuthService:
    def test_get_user(self, test_app):
        refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IjEyMzRkamxramFAZ21haWwuY29tIiwicGFzc3dvcmQiOiJWZXJ5X3N0cm9uZ19wYXNzIiwiZXhwIjoxNjc0NzM1ODYxfQ.8eWMoyR8WblZ7q537RIctagRNB9isKSLXoQEbI8NgXM"
        headers = {"Authorization": "Bearer {}".format(refresh_token)}
        client = test_app.test_client()
        resp = client.get("/user/", headers=headers)
        data = resp.data
        assert data.get("name")
        assert resp.status_code == 200
