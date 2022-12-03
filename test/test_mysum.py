from mysum import mysummation


def test_mysummation_positives():
    assert mysummation([1, 2, 3]) == 6
    assert mysummation([1, 2, 3, 4, 5]) == 15


def test_mysummation_negatives():
    assert mysummation([1, -1]) == 0


#def test_mysummation_float():
#    assert mysummation([1.1, -1]) == 0.1
#TODO: how to assert float?

#def test_mysummation_str():
#    assert mysummation(["a", "b", "c"]) == "abc"
#TODO: how to assert str polymorphism?
