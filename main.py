# python3
# Valters Mārtinsons

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):                     #parbauda vai iekavas sakrit
    return (left + right) in ["()", "[]", "{}"]    #parbauda vai iekavas sakrit


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if len(opening_brackets_stack)==0 or not are_matching(opening_brackets_stack[-1].char,next):
                return i + 1
            opening_brackets_stack.pop()
        
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack[-1].position + 1

def main():
    i = input()
    if i[0] == "I":
        text = input()
    # text = ""
        mismatch = find_mismatch(text)
        print(mismatch)

if __name__ == "__main__":
    main()