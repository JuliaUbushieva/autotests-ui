import pytest


@pytest.mark.skip(reason="Feature in development")
def test_feature_in_development():
    pass


SYSTEM_VERSION = "v1.2.0"


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",
    reason="The test cannot be run on system version v1.3.0."
)
def test_system_version_valid():
    pass


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",
    reason="The test cannot be run on system version v1.2.0."
)
def test_system_version_invalid():
    pass
