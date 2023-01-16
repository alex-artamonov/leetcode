import longest_common_prefix as lcp

def test_longest_common_prefix():
    strs = ["flower","flow","flight"]
    assert 'fl' == lcp.longest_common_prefix(strs)

def test_no_common_prefix():
    strs = ["dog","racecar","car"]
    assert '' == lcp.longest_common_prefix(strs)


def test_equal_words():
    strs = ["flower","flower","flower","flower"]
    assert 'flower' == lcp.longest_common_prefix(strs)