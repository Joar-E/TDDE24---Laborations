"""
ConstCalc
"""
from calc import *

def exec_program(p, table = {}):
    if is_program(p):
        return exec_statements(program_statements(p), table)
    else:
        print("Is not Calc program")


def exec_statements(statements, table):
    if not empty_statements(statements):
        new_table = eval_expression(first_statement(statements), table)
        return exec_statements(rest_statements(statements), new_table)
    else:
        return table

def eval_expression(statement, table):
    if is_statement(statement):
        return eval_statement(statement, table)
    elif is_binaryexpr(statement):
        return eval_binaryoper(statement, table)
    elif is_variable(statement):
        return eval_variable(statement, table)
    elif is_constant(statement):
        return statement
    else:
        raise ValueError('Input was wrong')

def eval_statement(s, table):
    if is_assignment(s):
        return exec_assignment(s, table)

    elif is_repetition(s):
        return exec_repetition(s, table)

    elif is_selection(s):
        return exec_selection(s, table)

    elif is_input(s):
        return exec_input(s, table)

    elif is_output(s):
        return exec_output(s, table)


def exec_assignment(a, table):
    table = table.copy()

    table[assignment_variable(a)] = eval_expression(assignment_expression(a), table)
    
    return table


def exec_repetition(r, table):
    table = table.copy()

    while eval_condition(r, table):
        table = exec_statements(repetition_statements(r), table)
    return table


def exec_selection(statement, table):
    if eval_condition(statement, table):
         return eval_expression(selection_true_branch(statement), table)

    elif selection_has_false_branch(statement):
         return eval_expression(selection_false_branch(statement), table)
    return table


def exec_input(i, table):
    table = table.copy()
    
    user_input = int(input(f'Enter value for {input_variable(i)}: '))

    table[input_variable(i)] = eval_expression(user_input, table)
    
    return table


def exec_output(o, table):
    output = eval_expression(output_expression(o), table)

    if is_variable(output_expression(o)):
        print(f'{output_expression(o)} = {eval_variable(output_expression(o), table)}')
    else:
        print(output)

    return table


def eval_condition(statement, table):
    cond = selection_condition(statement)

    cond_left = eval_expression(condition_left(cond), table)
    cond_right = eval_expression(condition_right(cond), table)

    if is_condition(cond):
        if condition_operator(cond) == '<':
            return cond_left < cond_right

        elif condition_operator(cond) == '>':
            return cond_left > cond_right

        elif condition_operator(cond) == '=':
            return cond_left == cond_right 

        else:
            return False


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
    print('Can not compute binaryoperator')
    #return table


def eval_variable(v, table):
    return table[v]


# --- Correct statements ---
calc_set_print = ['calc', ["set", "res", 5], ['print', 2], ['print', [4, "+", [2, "*", 2]]], ["print", "res"]]

calc2_if_set = ['calc', ['if', [[3, "+", 2], '=', 5], ['set', 'a', 5], ["print", 2]], ['print', 'a']]

calc_read_print = ['calc', ['read', 'n'], ['print', 'n']]

calc_fac = ['calc', ['read', 'n'], ['set', 'sum', 1], ['while', ['n', '>', 0], ['set', 'sum', ['sum', '*', 'n']], ['set', 'n', ['n', '-', 1]]], ['print', 'sum']]

calc_fib = ['calc', ['read', 'steps'], ['set', 'n', 1], ['set', 'n0', 0], ['while', ['steps', '>', 0], ['set', 'n', ['n', '+', 'n0']], ['set', 'n0', ['n', '-', 'n0']], ['print', 'n'], ['set', 'steps', ['steps', '-', 1]]]]


# --- Faulty statements ---
calc_error_binary = ['calc', ['read', 'n'], ['set', 'n', ['n', '%', 2]], ['print', 'n']]
exec_program(calc_read_print)

