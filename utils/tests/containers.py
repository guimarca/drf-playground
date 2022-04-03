import psycopg2
from django.conf import settings
from psycopg2 import OperationalError
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_container_is_ready


class PostgresDjangoContainer(DockerContainer):
    db_settings = settings.DATABASES["default"]

    POSTGRES_USER = db_settings["USER"]
    POSTGRES_DB = db_settings["NAME"]
    POSTGRES_PASSWORD = db_settings["PASSWORD"]

    def __init__(
        self, image="postgres:latest", port=5432, user=None, password=None, dbname=None
    ):
        super().__init__(image=image)
        self.POSTGRES_USER = user or self.POSTGRES_USER
        self.POSTGRES_PASSWORD = password or self.POSTGRES_PASSWORD
        self.POSTGRES_DB = dbname or self.POSTGRES_DB
        self.port_to_expose = port

        self.with_exposed_ports(self.port_to_expose)

    @wait_container_is_ready(OperationalError)
    def _connect(self):
        exposed_port = int(self.get_exposed_port(int(self.db_settings["PORT"])))
        psycopg2.connect(
            dbname=self.db_settings["NAME"],
            user=self.db_settings["USER"],
            password=self.db_settings["PASSWORD"],
            host=self.db_settings["HOST"],
            port=exposed_port,
        )
        self.db_settings["PORT"] = exposed_port

    def _configure(self):
        self.with_env("POSTGRES_USER", self.POSTGRES_USER)
        self.with_env("POSTGRES_PASSWORD", self.POSTGRES_PASSWORD)
        self.with_env("POSTGRES_DB", self.POSTGRES_DB)

    def _create_connection_url(
        self, dialect, username, password, host=None, port=None, db_name=None
    ):
        if self._container is None:
            raise RuntimeError("container has not been started")
        if not host:
            host = self.get_container_host_ip()
        port = self.get_exposed_port(port)
        url = "{dialect}://{username}:{password}@{host}:{port}".format(
            dialect=dialect, username=username, password=password, host=host, port=port
        )
        if db_name:
            url += "/" + db_name
        return url

    def start(self):
        self._configure()
        super().start()
        self._connect()
        return self

    def get_connection_url(self, host=None):
        return self._create_connection_url(
            dialect="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            db_name=self.POSTGRES_DB,
            host=host,
            port=self.port_to_expose,
        )
