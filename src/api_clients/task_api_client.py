from src.enums.urls import Url


class TaskApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = Url.BASE_URL.value

    def get_task(self, task_id=""):
        """Отправляет запрос на получение task."""
        response = self.auth_session.get(f"{self.base_url}/api/v2/task/{task_id}")
        if response.status_code != 200:
            response.raise_for_status()
        return response
