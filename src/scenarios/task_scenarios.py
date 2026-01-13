from src.api_clients.task_api_client import TaskApiClient


class TaskScenarios:
    def __init__(self, api_client: TaskApiClient):  # Типизация для ясности
        self.api_client = api_client

    def get_and_verify_task_exist(self):
        """
        Сценарий: получить task и проверить, что ответ не пуст.
        """
        task = self.api_client.get_task().json()

        # TODO: assert len(bookings) > 0, "Список bookings пуст"
        # TODO: print(f"Получено {len(bookings)} bookings id.")

        return task
