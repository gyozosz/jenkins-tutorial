import requests
from hamcrest import assert_that, equal_to
import pytest


def hello(name):
    return f"Hello {name}!"


def test_hello():
    name = "James"
    hello_ret = hello(name)
    assert_that(hello_ret, equal_to("Hello James!"))


def test_request():
    response = requests.request('GET', "https://en.wikipedia.org")
    assert_that(response.status_code, equal_to(200))
