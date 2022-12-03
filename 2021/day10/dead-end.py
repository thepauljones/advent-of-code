def braces_match(opening, closing):
    if opening == '(':
        return closing == ')'
    if opening == '[':
        return closing == ']'
    if opening == '{':
        return closing == '}'
    if opening == '<':
        return closing == '>'

    return False

def parse_braces(test_case):
    if len(test_case) == 0:
        return 'Valid'
    
    if braces_match(test_case[0], test_case[len(test_case) - 1]):
        return parse_braces(test_case[1:len(test_case)-1])

    return 'Corrupted'


tc1 = '([])'
tc2 ='{()()()}'
tc3 = '<([{}])>'
tc4= '[<>({}){}[([])<>]]'
tc5 = '(((((((((())))))))))'

print(parse_braces(tc1))
print(parse_braces(tc2))
print(parse_braces(tc3))
print(parse_braces(tc4))
print(parse_braces(tc5))
