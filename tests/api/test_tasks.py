from src.api_clients.task_api_client import TaskApiClient
from src.scenarios.task_scenarios import TaskScenarios


class TestTasks:
    def test_get_and_verify_task_exist(self, auth_session):
        """
        Сценарий: получить task и проверить, что ответ не пуст.
        """
        task_api_client = TaskApiClient(auth_session)
        task_scenarios = TaskScenarios(task_api_client)
        task_scenarios.get_and_verify_task_exist()
