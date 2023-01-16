import random as r
import pytest as p
import roman_arab as ra


def test_romans1():
    assert 3 == ra.roman_to_int('III')

def test_romans2():
    assert 58 == ra.roman_to_int('LVIII')


def test_romans3():
    assert 1994 == ra.roman_to_int('MCMXCIV')


romans =  ('I', 'V', 'X', 'L', 'C', 'D', 'M')


def test_err_too_long():    
    s = ''.join(r.choices(romans, k=16))
    with p.raises(ValueError):
        ra.roman_to_int(s)

def test_err_not_roman():
    s = 'IVxL'
    with p.raises(ValueError):
        ra.roman_to_int(s)

