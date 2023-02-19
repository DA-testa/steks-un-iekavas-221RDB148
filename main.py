# python3
# Valters Mārtinsons

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

# b = Bracket('aa',2)                        #MY
# print(b.char)                              #MY

def are_matching(left, right):                     #parbauda vai iekavas sakrit
    return (left + right) in ["()", "[]", "{}"]    #parbauda vai iekavas sakrit

# if (are_matching("{", "}") == True):       #MY
#     print("YES")                           #MY


def find_mismatch(text):
    opening_brackets_stack = []
    closing_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if len(opening_brackets_stack)==0 or not are_matching(opening_brackets_stack[-1].char,next):
                print(i+1)
                return 0
            opening_brackets_stack.pop()
        
    if len(opening_brackets_stack) == 0:
        print("Success")
    else:
        print(opening_brackets_stack[-1].position + 1)

    # print("opening: ", end="")           #PRINT
    # for i, j in opening_brackets_stack:  #PRINT
    #     print(i, j, end=" ")             #PRINT
    # print("\nclosing: ", end="")         #PRINT
    # for i, j in closing_brackets_stack:  #PRINT
    #     print(i, j, end=" ")             #PRINT
    # print()                              #PRINT

    # for i, j in closing_brackets_stack:                              #dead 
    #     print(j, end=" ")                                            #dead
    #     # a = len(closing_brackets_stack)-1                          #dead
    #     print(closing_brackets_stack[len(closing_brackets_stack)-1]) #dead

    # a = closing_brackets_stack[len(closing_brackets_stack)-1].position
    # print(a)

    # print(opening_brackets_stack.position) #dead

    # for i in range(a-1,-1,-1):
    #     print(i)
    #     if i in opening_brackets_stack:
    #         print(i, "uraaa")




def main():
    text = input()
    # mismatch = find_mismatch(text)
    find_mismatch(text)




if __name__ == "__main__":
    main()
# main()
