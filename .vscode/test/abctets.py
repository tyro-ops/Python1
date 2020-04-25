import pytest


class TestClass:

    def pytest_addoption(self, parser):
        parser.addoption(
            "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
        )

    @pytest.fixture
    def cmdopt(self, request):
        return request.config.getoption("--cmdopt")
