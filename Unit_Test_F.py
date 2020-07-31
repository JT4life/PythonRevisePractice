import Unit_Test_Framework

def test_add():
    assert Unit_Test_Framework.add(4,5)==9
    assert Unit_Test_Framework.add(4)==104

def test_product():
    assert Unit_Test_Framework.product(4,5)==20
    assert Unit_Test_Framework.product(4)==4