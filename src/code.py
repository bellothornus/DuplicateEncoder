def duplicate_encode(string):
    string = string.lower()
    encode = ""
    characters = list(string)
    for character in characters:
        if characters.count(character) > 1:
            encode += ")"
        else:
            encode += "("
    return encode

if __name__ == "__main__":
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())", "should ignore upper and lower cases"
    assert duplicate_encode("(( @") == "))((", "should work too with special characters"