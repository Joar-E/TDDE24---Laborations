"""
ConstCalc
"""
from calc import *

def exec_program(p: list()):
    if is_program(p):
        exec_statements(program_statements(p))
    else:
        print("Is not Calc program")

variable_dict = {}        


def exec_statements(statements, rest_list = False):
    if not empty_statements(statements):
        return (eval_expression(first_statement(statements)), exec_statements(rest_statements(statements)))


def eval_expression(statement):
    if is_statement(statement):
        return eval_statement(statement)
    elif is_binaryexpr(statement):
        return eval_binaryoper(statement)
    elif is_variable(statement):
        return eval_variable(statement)
    elif is_constant(statement):
        return(statement)


def eval_statement(s):
    if is_assignment(s):
        return eval_assignment(s)

    elif is_selection(s):
        return eval_condition(s)

    elif is_output(s):
        return eval_output(s)


def eval_assignment(a):
    variable_dict[assignment_variable(a)] = eval_expression(assignment_expression(a))


def eval_condition(statement):
    cond = selection_condition(statement)

    cond_left = eval_expression(condition_left(cond))
    cond_right = eval_expression(condition_right(cond))

    if is_condition(cond):
        if condition_operator(cond) == '<' and (cond_left < cond_right):
            return eval_expression(selection_true_branch(statement))

        elif condition_operator(cond) == '>' and (cond_left > cond_right):
            return eval_expression(selection_true_branch(statement))

        elif condition_operator(cond) == '=' and (cond_left == cond_right):
            return eval_expression(selection_true_branch(statement))

        elif selection_has_false_branch(statement):
            return eval_expression(selection_false_branch(statement))
        
        else:
            return False


def eval_output(o):
    return print(eval_expression(output_expression(o)))


def eval_binaryoper(b):

    biny_left = eval_expression(binaryexpr_left(b))
    biny_right = eval_expression(binaryexpr_right(b))

    if binaryexpr_operator(b) == "+":
        return (biny_left + biny_right)
    elif binaryexpr_operator(b) == "-":
        return (biny_left - biny_right)
    elif binaryexpr_operator(b) == "/":
        return (biny_left / biny_right)
    elif binaryexpr_operator(b) == "*":
        return (biny_left * biny_right)


def eval_variable(v):
    if v in variable_dict:
        return variable_dict[v]


calc1 = ['calc', ["set", "res", 5], ['print', 2], ['print', [4, "+", [2, "*", 2]]], ["print", "res"]]
calc2 = ['calc', ['if', [[3, "+", 2], '=', 5], ["set", "a", 5], ["print", 2]], ["print", "a"]]
exec_program(calc2)