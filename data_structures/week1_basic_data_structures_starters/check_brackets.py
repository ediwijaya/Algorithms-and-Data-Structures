# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    flag = True
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) > 0:
                last_bracket = opening_brackets_stack[-1].bracket_type
                if last_bracket == '(' and next == ')':
                    opening_brackets_stack.pop()
                elif last_bracket == '[' and next == ']':
                    opening_brackets_stack.pop()
                elif last_bracket == '{' and next == '}':
                    opening_brackets_stack.pop()
                else:
                    flag = False
                    break
            else:
                flag = False
                break

    # Printing answer, write your code here
    if flag:
        if len(opening_brackets_stack) == 0:
            print("Success")
        else:
            print(opening_brackets_stack[-1].position)
    else:
        print(i+1)
