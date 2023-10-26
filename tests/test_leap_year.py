import pytest
from leapYear import isLeapYear

# Simple obvious year
def test_leap_year_div_by_4():
    assert isLeapYear(2004) == True

#
def test_leap_year_div_by_400():
    assert isLeapYear(2000) == True

def test_non_leap_year():
    assert isLeapYear(2001) == False

# Non-leap year. divisible by 100 but not by 400
def test_non_leap_year_divisible_by_100_but_not_400():
    assert isLeapYear(1900) == False

# Leap year. edge case: divisible by 4 and 400
# This still works even though the function has an OR statement because:
# In Python, the and operator has a higher precedence than the or operator.
def test_leap_year_divisible_by_4_and_400():
    assert isLeapYear(1600) == True

# Leap year. edge case: divisible by 4 and 100 but not 400
def test_non_leap_year_divisible_by_4_and_100_but_not_400():
    assert isLeapYear(1700) == False

# Leap year. edge case: divisible by 4 and 100 and 400
def test_leap_year_divisible_by_4_and_100_and_400():
    assert isLeapYear(2000) == True

def test_random_year_for_CI():
    assert isLeapYear(2005) == False