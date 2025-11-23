from app import calculate_bill

def test_calculate_bill():
    assert calculate_bill(100) == 118
    assert calculate_bill(0) == 0
