"""
A collection of unit tests for Mandelbot Alpha
"""
import os
import sys
from random import randint
import pytest
sys.path.append("..")
from mandelbot_alpha import all_track_chars, track_dur_min #pylint: disable=import-error,wrong-import-position
# Import relevant libraries.

pytest_used = pytest.skip # for pylint to be happy

index_zero = [(0, "Xtal"),
              (0, 0.51),
              (0, 0.505),
              (0, 9),
              (0, -13.053),
              (0, 0.0344),
              (0, 0.342),
              (0, 0.96),
              (0, 0.117),
              (0, 0.318),
              (0, 114.532),
              (0, 4),
              (0, 4.895866666666667)]

# Create list of expected values at index 0 of every data list in
# "all_track_chars".

def test_alpha_index_zero():
    """
    Test that mandelbot_alpha.py is pulling from the correct database
    in the correct order by checking index 0 of track data which
    should remain constant.
    """
    i = 0
    for temp_tuple in index_zero:
        assert all_track_chars[i][temp_tuple[0]] == temp_tuple[1]
        i += 1

def test_alpha_index_rand():
    """
    Test that all data was correctly appended to all_track_chars by
    crosschecking its last section (track duration in minutes) with
    the standalone data list of track duration it appends from as well
    as checking for the correct number of lists within it.
    """
    random_index = randint(0, 100)
    assert track_dur_min[random_index] == all_track_chars[12][random_index]

if os.path.exists("all_track_chars.csv"):
    os.remove("all_track_chars.csv")

# Bug fix where testing Mandelbot Alpha may erroneously write a track
# data CSV file to the tests folder.
