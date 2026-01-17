from src.api_clients.task_api_client import TaskApiClient


class TaskScenarios:
    def __init__(self, api_client: TaskApiClient):  # Типизация для ясности
        self.api_client = api_client

    def get_and_verify_task_exist(self):
        """
        Сценарий: получить task и проверить, что ответ не пуст.
        """
        task = self.api_client.get_task("86c7f4v8a").json()

        assert task, "Ответ task пуст"
        print(f"Получена информация о task с id '86c7f4v8a'.")

        return task
