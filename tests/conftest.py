import pytest

import requests

from src.enums.headers import Headers

HEADERS = Headers.HEADERS.value


@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(HEADERS)

    return session
