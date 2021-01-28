import pytest


@pytest.fixture(scope="class")
# use fixtures for opening chrome browser, setting up database, all prerequisite stuff.
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","Rahul","shetty"), ("Firefox","Shetty"),("IE","SS")])
def crossBrowser(request):
    return request.param

