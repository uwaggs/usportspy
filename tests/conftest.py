import time
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--test-delay",
        action="store",
        default=0,
        type=float,
        help="Delay in seconds between tests",
    )


@pytest.fixture(autouse=True)
def slow_down_tests(request):
    delay = request.config.getoption("--test-delay")
    yield
    if delay > 0:
        time.sleep(delay)
