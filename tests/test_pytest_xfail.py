import pytest


@pytest.mark.xfail(reason='Bug has been found in the app; the test should fail with an error.')
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason='The bug fixed, but the test is marked as xfail.')
def test_without_bug():
    pass


@pytest.mark.xfail(reason='The external service is temporarily unavailable.')
def test_external_services_is_unavailable():
    assert 1 == 2
