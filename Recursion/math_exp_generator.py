""" from interviewing.io session

write a function that takes no parameters and generates a
valid mathematical expression of random length,
with random numbers and random operators. output is string format.
"""

import random


def start_exp():
    # must start with num, not operator
    output_list = []

    open_paren = random.randint(0, 1)
    if open_paren:
        output_list.append("(")
        output_list.append(start_exp())
        output_list.append(")")
    else:
        output_list.append(str(random.randint(0, 9)))

    iterations = random.randint(1, 5)

    for i in range(iterations):
        exp = build_exp()
        output_list.append(exp)

    return " ".join(output_list)


def build_exp():
    operators = ["+", "-", "/", "%", "*"]

    op_index = random.randint(0, 3)
    operator = operators[op_index]
    num = str(random.randint(0, 9))

    return " " + operator + " " + num


print start_exp()
print start_exp()
print start_exp()
print start_exp()

# not perfect.  Either the exp starts with paren, or there are NO PAREN in the
# whole exp.  :(
