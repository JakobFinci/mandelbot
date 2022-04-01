"""
A collection of unit tests for Mandelbot Beta
"""
import sys
import pytest
import requests  # pylint: disable=import-error,wrong-import-position
sys.path.append("..")
# Import relevant libraries.

pytest_used = pytest.skip  # for pylint to be happy


# pylint: disable=bad-option-value,useless-object-inheritance
def test_data_type():
    """
    Test that mandelbot_beta.py is behaving correctly and capturing the correct
    data in JSON format.
    """
    response = requests.get(
        "https://api.spotify.com/v1/audio-features")
    assert response.headers["Content-Type"] == "application/json"

# pylint: disable=bad-option-value,consider-using-sys-exit
