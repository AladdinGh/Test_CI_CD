import pytest
from check import check_for_test

def test_pass_case():
    data = {"message": "This contains Test"}
    assert check_for_test(data) == "PASS"

def test_fail_case():
    data = {"message": "No match here"}
    assert check_for_test(data) == "FAIL"
