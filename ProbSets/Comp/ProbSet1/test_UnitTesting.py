#test_UnitTesting.py

import UnitTesting as ut
import pytest as pt

def test_smallest_factor():
    assert ut.smallest_factor(1)==1, "Fails for 1"
    assert ut.smallest_factor(2)==2, "Fails for 2"
    assert ut.smallest_factor(3)==3, "Fails for 3"
    assert ut.smallest_factor(4)==2, "Fails for 4"
    assert ut.smallest_factor(5)==5, "Fails for 5"
    assert ut.smallest_factor(6)==2, "Fails for 6"
    assert ut.smallest_factor(10)==2, "Fails for 10"

# The above yields perfecct coverage on the function.

def test_month_length():
    assert ut.month_length("September")==30, "Failed for 30 days"
    assert ut.month_length("May")==31, "Failed for 31 days"
    assert ut.month_length("February")==28, "Failed for Feb normal"
    assert ut.month_length("February", leap_year=True)==29, "Failed for Feb leap year"
    assert ut.month_length("Not a Month")==None, "Failed for non-months"

# The above yields perfect coverage on the function.

def test_operate():
    assert ut.operate(3, 6, '+')==9, "Addition"
    assert ut.operate(3, 6, '-')==-3, "Subtraction"
    assert ut.operate(3, 6, '*')==18, "Multiplication"
    assert ut.operate(3, 6, '/')==.5, "Division"
    with pt.raises(ZeroDivisionError) as excinfo:
        ut.operate(3, 0, "/")
    assert excinfo.value.args[0] == "division by zero is undefined"
    with pt.raises(TypeError) as excinfo:
        ut.operate(3, 6, 7)
    assert excinfo.value.args[0] == "oper must be a string"
    with pt.raises(ValueError) as excinfo:
        ut.operate(3, 6, "Not operator")
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"

# The above test yields perfect coverage on the function.
@pt.fixture
def set_up_fractions():
    frac_1_3 = ut.Fraction(1, 3)
    frac_1_2 = ut.Fraction(1, 2)
    frac_n2_3 = ut.Fraction(-2, 3)
    return frac_1_3, frac_1_2, frac_n2_3

def test_fraction_init(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3.numer == 1
    assert frac_1_2.denom == 2
    assert frac_n2_3.numer == -2
    frac = ut.Fraction(30, 42) # 30/42 reduces to 5/7.
    assert frac.numer == 5
    assert frac.denom == 7
    with pt.raises(ZeroDivisionError) as excinfo:
        ut.Fraction(1, 0)
    assert excinfo.value.args[0] == "denominator cannot be zero"
    with pt.raises(TypeError) as excinfo:
        ut.Fraction("Hello World", "Hooray")
    assert excinfo.value.args[0] == "numerator and denominator must be integers"

def test_fraction_str(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert str(frac_1_3) == "1 / 3"
    assert str(frac_1_2) == "1 / 2"
    assert str(frac_n2_3) == "-2 / 3"
    assert str(ut.Fraction(3, 1)) == "3"

def test_fraction_float(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert float(frac_1_3) == 1 / 3.
    assert float(frac_1_2) == .5
    assert float(frac_n2_3) == -2 / 3.

def test_fraction_eq(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 == ut.Fraction(1, 2)
    assert frac_1_3 == ut.Fraction(2, 6)
    assert frac_n2_3 == ut.Fraction(8, -12)
    assert frac_1_2 == 2. / 4.

def test_fraction_add(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3 + frac_1_2 == ut.Fraction(5, 6)

def test_fraction_sub(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 - frac_1_3 == ut.Fraction(1, 6)

def test_fraction_mul(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 * frac_1_3 == ut.Fraction(1, 6)

def test_fraction_div(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 / frac_1_3 == ut.Fraction(3, 2)
    with pt.raises(ZeroDivisionError) as excinfo:
        frac_1_2 / ut.Fraction(0, 1)
    assert excinfo.value.args[0] == "cannot divide by zero"
