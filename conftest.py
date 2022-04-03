import pytest
from testcontainers.elasticsearch import ElasticSearchContainer

from utils.tests.containers import PostgresDjangoContainer


@pytest.fixture(scope="session")
def django_db_setup(django_db_blocker) -> None:
    with PostgresDjangoContainer("postgres:latest") as postgres:
        with django_db_blocker.unblock():
            from django.test.utils import setup_databases

            setup_databases(verbosity=1, interactive=False)
            yield


@pytest.fixture(scope="session", autouse=True)
def elastic_setup() -> None:
    with ElasticSearchContainer("elasticsearch:7.17.2") as es:
        yield
