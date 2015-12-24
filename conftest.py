import pytest


@pytest.fixture
def args():
    return {
        "quiet"  : False,
        "verbose": False,
        "output" : "out.png",
        "folder" : "tests/assets/happy_path",
    }
