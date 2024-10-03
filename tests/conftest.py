import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="function", autouse=True)
def base_url():
    return "https://automationexercise.com/"

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()