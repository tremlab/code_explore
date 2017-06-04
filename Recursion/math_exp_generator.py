""" from interviewing.io session

write a function that takes no parameters and generates a
valid mathematical expression of random length,
with random numbers and random operators. output is string format.
"""

import random


def start_exp_r():
    iterations = random.randint(1, 20)

    exp = exp_recursion(iterations)

    final_num = str(random.randint(0, 9))
    if exp[-1] == ")":
        exp.insert(-1, final_num)
    else:
        exp.append(final_num)
    return " ".join(exp)


def exp_recursion(iterations, count=0, open_paren=0):

    if iterations == count:
        if open_paren:
            return ")"
        return ""

    operators = ["+", "-", "/", "%", "*"]
    op_index = random.randint(0, 3)
    operator = operators[op_index]

    num = str(random.randint(0, 15))

    exp = []

    if open_paren:
        close_paren = random.randint(0, 1)
        if close_paren:
            exp = [num, ")", operator]
            open_paren = 0
    else:
        open_paren = random.randint(0, 1)
        if open_paren:
            exp = ["(", num, operator]
        else:
            exp = [num, operator]

    exp.extend(exp_recursion(iterations, count + 1, open_paren))

    return exp


def exp_iteration():

    # starts the string - maybe a paren, definitely a num.
    output_list = []
    open_paren = random.randint(0, 1)
    if open_paren:
        output_list.append("(")
    output_list.append(str(random.randint(0, 9)))

    iterations = random.randint(1, 15)

    for i in range(iterations):
        exp = op_and_num()

        if open_paren:
            close_paren = random.randint(0, 1)
            if close_paren:
                exp += (")")
                open_paren = 0
        else:
            open_paren = random.randint(0, 1)
            if open_paren:
                exp = exp[0] + " ( " + exp[-1]

        output_list.append(exp)

    if open_paren:
        output_list.append(")")

    return " ".join(output_list)


def op_and_num():
    operators = ["+", "-", "/", "%", "*"]

    op_index = random.randint(0, 3)
    operator = operators[op_index]
    num = str(random.randint(0, 9))

    return operator + " " + num


print start_exp_r()
# print exp_iteration()


## ideally, I'd like to ahve the option of NESTED parens. :(
## but for now, this solution works well.
