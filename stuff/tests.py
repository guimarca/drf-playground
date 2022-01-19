import pytest
from rest_framework.test import APIRequestFactory

from stuff.views import StuffViewset

factory = APIRequestFactory()


@pytest.mark.django_db
def test_stuff_get(client):
    response = client.get("/stuff/")
    assert response.status_code == 200


def test_foo():
    request = factory.post("/api/resource/1/foo/")
    view = StuffViewset.as_view({"post": "foo"})
    response = view(request, pk=1)
    assert response.status_code == 200
    assert response.data == {"pk": 1}
