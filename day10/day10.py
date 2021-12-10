with open('data.dat') as file:
    data = [line.strip() for line in file]

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

def is_opening(char):
    if char == '(' or char == '[' or char == '{' or char == '<':
        return True

    return False

def get_matching(brace):
    if brace == '(':
        return ')'
    if brace == '[':
        return ']'
    if brace == '{':
        return '}'
    if brace == '<':
        return '>'
    if brace == ')':
        return '('
    if brace == ']':
        return '['
    if brace == '}':
        return '{'
    if brace == '>':
        return '<'

# Returns True when string is valid, and the illegal character
# when a string cannot be parsed
def parse_braces(test_case):
    tracker = []
    for char in test_case:
        if is_opening(char):
            tracker.append(char)
        else:
            if len(tracker) == 0:
                return 'Corrupted'

            if braces_match(tracker[len(tracker) - 1], char):
                tracker.pop(len(tracker) - 1)
            else:
                return char

    return len(tracker) == 0

def map_char_to_points(char):
    if char == ')':
        return 3
    if char == ']':
        return 57
    if char == '}':
        return 1197
    if char == '>':
        return 25137

illegal_chars = []
for line in data:
    result = parse_braces(line)
    print(line, result)
    if (result == True or result == False):
       continue
    else:
        illegal_chars.append(result)


print(sum(map(map_char_to_points, illegal_chars)))

tc1 = '([])'
tc2 ='{()()()}'
tc3 = '<([{}])>'
tc4 = '[<>({}){}[([])<>]]'
tc5 = '(((((((((())))))))))'

corr = '{([(<{}[<>[]}>{[]{[(<()>'
corr2 = '[[<[([]))<([[{}[[()]]]'
corr3 = '[{[{({}]{}}([{[{{{}}([]'
corr4 = '[<(<(<(<{}))><([]([]()'
corr5 = '<{([([[(<>()){}]>(<<{{'

print(parse_braces(tc1))
print(parse_braces(tc2))
print(parse_braces(tc3))
print(parse_braces(tc4))
print(parse_braces(tc5))

print(parse_braces(corr))
print(parse_braces(corr2))
print(parse_braces(corr3))
print(parse_braces(corr4))
print(parse_braces(corr5))
