import pytest
import datetime
import time


@pytest.fixture(scope='session', autouse=True)
def setup_module(request):
    """Записываем время запуска сессии тестов"""
    start_time = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
    print(f'Запустили тест {start_time}!')

    def closure():
        """Записываем время завершения сессии тестов"""
        end_time = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
        print(f'Тест завершился {end_time}.')

    request.addfinalizer(closure)


@pytest.fixture(scope='function')
def test_fixture(request):
    """Записываем время запуска отдельного теста"""
    start_time = time.time()
    print('Тест запустился!')

    def closure():
        """Записываем время завершения отдельного тестов"""
        end_time = time.time()
        print(f'Тест завершился. Время выполнения {end_time - start_time} секунд.')

    request.addfinalizer(closure)

