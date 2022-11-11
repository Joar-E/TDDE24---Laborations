"""
ConstCalc
"""
from calc import *

def exec_program(p, table = {}):
    if is_program(p):
        exec_statements(program_statements(p), table)
    else:
        print("Is not Calc program")


def exec_statements(statements, table):
    if not empty_statements(statements):
        if is_assignment(first_statement(statements)):

            table = exec_assignment(first_statement(statements), table)

            return exec_statements(rest_statements(statements), table)

        else:
            return eval_expression(first_statement(statements), table), exec_statements(rest_statements(statements), table)


def eval_expression(statement, table):
    if is_statement(statement):
        return eval_statement(statement, table)
    elif is_binaryexpr(statement):
        return eval_binaryoper(statement, table)
    elif is_variable(statement):
        return eval_variable(statement, table)
    elif is_constant(statement):
        return statement

def eval_statement(s, table):
    if is_assignment(s):
        return exec_assignment(s, table)

    elif is_selection(s):
        return eval_condition(s, table)

    elif is_output(s):
        return eval_output(s, table)


def exec_assignment(a, table):
    table = table.copy()

    table[assignment_variable(a)] = eval_expression(assignment_expression(a), table)
    #print(table)
    return table


def eval_condition(statement, table):
    cond = selection_condition(statement)

    cond_left = eval_expression(condition_left(cond), table)
    cond_right = eval_expression(condition_right(cond), table)

    if is_condition(cond):
        if condition_operator(cond) == '<' and (cond_left < cond_right):
            return eval_expression(selection_true_branch(statement), table)

        elif condition_operator(cond) == '>' and (cond_left > cond_right):
            return eval_expression(selection_true_branch(statement), table)

        elif condition_operator(cond) == '=' and (cond_left == cond_right):
            return eval_expression(selection_true_branch(statement), table)

        elif selection_has_false_branch(statement):
            return eval_expression(selection_false_branch(statement), table)
        
        else:
            return False


def eval_output(o, table):
    output = eval_expression(output_expression(o), table)

    if is_variable(output_expression(o)):
        print(f'{output_expression(o)} = {eval_variable(output_expression(o), table)}')
    else:
        print(output)

    return table


def eval_binaryoper(b, table):

    biny_left = eval_expression(binaryexpr_left(b), table)
    biny_right = eval_expression(binaryexpr_right(b), table)

    if binaryexpr_operator(b) == "+":
        return (biny_left + biny_right)
    elif binaryexpr_operator(b) == "-":
        return (biny_left - biny_right)
    elif binaryexpr_operator(b) == "/":
        return (biny_left / biny_right)
    elif binaryexpr_operator(b) == "*":
        return (biny_left * biny_right)

    return table


def eval_variable(v, table):
    return table[v]


calc1 = ['calc', ["set", "res", 5], ['print', 2], ['print', [4, "+", [2, "*", 2]]], ["print", "res"]]
calc2 = ['calc', ['if', [[3, "+", 2], '=', 5], ["print", 3], ["print", 2]]]

calc3 = ['calc', ['set', 'a', 5], ['print', "a"]]
exec_program(calc2)