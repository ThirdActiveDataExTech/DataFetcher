class _MinioServer:
    access_key = ""
    secret_key = ""
    url = "0.0.0.0:9004"


class _PostgresServer:
    host = "0.0.0.0"
    user = ""
    password = ""
    port = 5432
    database = ""


class _DataPortal:
    base_url = "api.odcloud.kr/api"
    endpoint = ""
    service_key = ""


class _SeoulPortal:
    base_url = "openapi.seoul.go.kr:8088/"
    endpoint = ""
    service_key = ""


class Config:
    minio_server = _MinioServer()
    postgres_server = _PostgresServer()
    data_portal = _DataPortal()
    seoul_portal = _SeoulPortal()


class NaverAPIIdentify:
    client_id = "<KEY>"
    client_secret = "<KEY>"
