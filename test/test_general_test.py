from src.code import duplicate_encode

def test_normal():
    assert duplicate_encode("din") == "((("
def test_duplicate_and_not_duplicate():
    assert duplicate_encode("recede") == "()()()"
def test_lower_upper_text():
    assert duplicate_encode("Success") == ")())())", "should ignore upper and lower cases"
def test_special_character():
    assert duplicate_encode("(( @") == "))((", "should work too with special characters"
