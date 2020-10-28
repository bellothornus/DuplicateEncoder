from src.code import duplicate_encode

def test_din():
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())", "should ignore upper and lower cases"
    assert duplicate_encode("(( @") == "))((", "should work too with special characters"
