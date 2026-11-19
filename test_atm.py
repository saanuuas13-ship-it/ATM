from atm import atm

def test_approved():
    assert atm(2000, 5000, 1234) == "Approved"

def test_declined():
    assert atm(6000, 5000, 1234) == "Declined"

def test_wrong_pin():
    assert atm(2000, 5000, 1111) == "Declined"