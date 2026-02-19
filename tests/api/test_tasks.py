import pytest

from src.api_clients.task_api_client import TaskApiClient
from src.scenarios.task_scenarios import TaskScenarios
from tests.conftest import delete_manager


class TestTasks:
    list_ID = "901519603511"

    def test_create_task_and_check(self, auth_session, delete_manager, task_data, list_id=list_ID):
        """
        Сценарий: создать и проверить task.
        """
        task_api_client = TaskApiClient(auth_session)
        task_scenarios = TaskScenarios(task_api_client)
        task_scenarios.create_task_and_check(delete_manager, task_data, list_id)

    def test_get_and_verify_task_exist(self, auth_session, delete_manager, task_data, list_id=list_ID):
        """
        Сценарий: получить task и проверить, что ответ не пуст.
        """
        task_api_client = TaskApiClient(auth_session)
        task_scenarios = TaskScenarios(task_api_client)
        task_scenarios.get_and_verify_task_exist(delete_manager, task_data, list_id)

    def test_update_task_and_verify_changes(self, auth_session, delete_manager, task_data, list_id=list_ID):
        """
        Сценарий: создать, изменить и проверить task.
        """
        task_api_client = TaskApiClient(auth_session)
        task_scenarios = TaskScenarios(task_api_client)
        task_scenarios.update_task_and_check(delete_manager, task_data, list_id)

    def test_delete_existing_task_and_verify(self, auth_session, task_data, list_id=list_ID):
        """
        Сценарий: создать и удалить task.
        """
        task_api_client = TaskApiClient(auth_session)
        task_scenarios = TaskScenarios(task_api_client)
        task_scenarios.delete_existing_task_and_verify(task_data, list_id)

    @pytest.mark.parametrize("invalid_task_data, expected_status_code", [
        ({'name': ''}, 400),
        ({"name": None}, 400),
        ({"name": 0}, 400),
        ({"description": "Description"}, 400)
    ])
    def test_create_task_negative(self, auth_session, invalid_task_data, expected_status_code, list_id=list_ID):
        """
        Сценарий: создать task с разными наборами невалидных данных,
        чтобы убедиться, что система правильно обрабатывает ошибки.
        """
        task_api_client = TaskApiClient(auth_session)
        task_scenarios = TaskScenarios(task_api_client)
        task_scenarios.create_task_negative(invalid_task_data, list_id, expected_status_code)

    @pytest.mark.parametrize("invalid_task_data, expected_status_code", [
        ({'name': 1}, 400)
    ])
    def test_update_task_negative(self, auth_session, delete_manager, task_data, invalid_task_data,
                                  expected_status_code, list_id=list_ID):
        """
        Сценарий: создать task, отправить запрос на изменение task,
        используя разные невалидных данных, чтобы убедиться,
        что система правильно обрабатывает ошибки.
        """
        task_api_client = TaskApiClient(auth_session)
        task_scenarios = TaskScenarios(task_api_client)
        task_scenarios.update_task_negative(delete_manager, task_data, invalid_task_data, list_id, expected_status_code)
