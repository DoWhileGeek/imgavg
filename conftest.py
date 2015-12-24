import pytest


@pytest.fixture
def args():
    return {
        "verbose": False,
        "output" : "out.png",
        "folder" : "tests/assets/happy_path",
    }
