import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
# unique annotation for pytest, xfail useful when you want the test case to run but not report.
def test_SecondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
    print(crossBrowser[1])

