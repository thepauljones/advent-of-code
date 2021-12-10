with open('data.dat') as file:
    data = [line.strip() for line in file]

def map_char_to_points(char):
    if char == ')':
        return 3
    if char == ']':
        return 57
    if char == '}':
        return 1197
    if char == '>':
        return 25137

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
                return False

            if braces_match(tracker[len(tracker) - 1], char):
                tracker.pop(len(tracker) - 1)
            else:
                return False

    if len(tracker) == 0:
        return True
    else:
        return ''.join(tracker)

def part_one(data):
    illegal_chars = []
    for line in data:
        result = parse_braces(line)
        if (result == True or result == False):
           continue
        else:
            illegal_chars.append(result)

    return sum(map(map_char_to_points, illegal_chars))

def map_char_to_points2(char):
    if char == ')':
        return 1
    if char == ']':
        return 2
    if char == '}':
        return 3
    if char == '>':
        return 4

def part_two(data):
    total_score = []
    for line in data:
        result = parse_braces(line)
        if (result == True or result == False):
           continue
        else:
            unmatched = result

            missing = []
            for brace in unmatched:
                missing.append(get_matching(brace))

            missing = list(reversed(missing))

            score = 0
            for char in missing:
                score *= 5
                val = map_char_to_points2(char)
                score += val

            total_score.append(score)

    return sorted(total_score)[len(total_score) / 2]

        

# print(part_one(data))
print(part_two(data))

# tc1 = '([])'
# tc2 ='{()()()}'
# tc3 = '<([{}])>'
# tc4 = '[<>({}){}[([])<>]]'
# tc5 = '(((((((((())))))))))'
# 
# corr = '{([(<{}[<>[]}>{[]{[(<()>'
# corr2 = '[[<[([]))<([[{}[[()]]]'
# corr3 = '[{[{({}]{}}([{[{{{}}([]'
# corr4 = '[<(<(<(<{}))><([]([]()'
# corr5 = '<{([([[(<>()){}]>(<<{{'

# print(parse_braces(tc1))
# print(parse_braces(tc2))
# print(parse_braces(tc3))
# print(parse_braces(tc4))
# print(parse_braces(tc5))
# 
# print(parse_braces(corr))
# print(parse_braces(corr2))
# print(parse_braces(corr3))
# print(parse_braces(corr4))
# print(parse_braces(corr5))
