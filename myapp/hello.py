import requests
from hamcrest import assert_that, equal_to


def hello(name):
    print(f"Hello {name}!")


if __name__ == "__main__":
    hello("James")
    response = requests.request('GET', "https://en.wikipedia.org")
    assert_that(response.status_code, equal_to(200))
