import parentheses as p

def test_case1():
    s = "()"
    assert True == p.isValid(s)

def test_case2():
    s = "()[]{}"
    assert True == p.isValid(s)

def test_case3():
    s = "(]"
    assert False == p.isValid(s)


def test_case4():
    s = "{[()]}"
    assert True == p.isValid(s)


def test_case4():
    s = "(([]){})"
    assert True == p.isValid(s)

    