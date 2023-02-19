# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if len(opening_brackets_stack) == 0 or not are_matching(opening_brackets_stack[-1].char,next):
                print(i+1)
                return 0
            opening_brackets_stack.pop()

    if len(opening_brackets_stack) == 0:
        print("Success")
    else:
        print(opening_brackets_stack[-1].position + 1)


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()

