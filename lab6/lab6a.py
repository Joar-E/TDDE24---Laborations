"""
ConstCalc
"""
from calc import *

def exec_program(p, table = {}):
    """Runs the program if it is a Calc program"""
    if is_program(p):
        return exec_statements(program_statements(p), table)
    else:
        raise SyntaxError("Is not Calc program")


def exec_statements(statements, table):
    """Runs through every statement, one at a time"""
    if not empty_statements(statements):
        new_table = eval_expression(first_statement(statements), table)
        return exec_statements(rest_statements(statements), new_table)
    else:
        return table


def eval_expression(expression, table):
    """Checks what type of expression it is and evaluates it"""
    if is_statement(expression):
        return eval_statement(expression, table)
    elif is_binaryexpr(expression):
        return eval_binaryoper(expression, table)
    elif is_variable(expression):
        return eval_variable(expression, table)
    elif is_constant(expression):
        return expression
    else:
        raise SyntaxError('Calc program syntax was invalid')


def eval_statement(s, table):
    """Checks the type of statement and executes it"""
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


def exec_assignment(s, table):
    """Executes set statements"""
    table = table.copy()

    table[assignment_variable(s)] = eval_expression(assignment_expression(s), table)
    
    return table


def exec_repetition(s, table):
    """Executes while statements"""
    while eval_condition(s, table):
        table = exec_statements(repetition_statements(s), table)
    return table


def exec_selection(s, table):
    """Executes if statements"""
    if eval_condition(s, table):
         return eval_expression(selection_true_branch(s), table)

    elif selection_has_false_branch(s):
         return eval_expression(selection_false_branch(s), table)
    return table


def exec_input(s, table):
    """Executes read statements"""
    table = table.copy()
    
    user_input = int(input(f'Enter value for {input_variable(s)}: '))

    table[input_variable(s)] = eval_expression(user_input, table)
    
    return table


def exec_output(s, table):
    """Executes print statements"""
    output = eval_expression(output_expression(s), table)

    if is_variable(output_expression(s)):
        print(f'{output_expression(s)} = {eval_variable(output_expression(s), table)}')
    else:
        print(output)

    return table


def eval_condition(s, table):
    """Evaluates the condition inside of the statement and 
       returns whether it is True or False"""
    cond = selection_condition(s)

    cond_left = eval_expression(condition_left(cond), table)
    cond_right = eval_expression(condition_right(cond), table)

    condopers = {'<': lambda x, y: x < y, '>': lambda x, y: x > y,\
                 '=': lambda x, y: x == y}

    if is_condition(cond):
        if condition_operator(cond) in condopers:
            return condopers[condition_operator(cond)](cond_left, cond_right)


def eval_binaryoper(s, table):
    """Evaluates the binaryexpression inside of the statements
       and executes the calculation"""
    biny_left = eval_expression(binaryexpr_left(s), table)
    biny_right = eval_expression(binaryexpr_right(s), table)

    op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, \
          '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    if binaryexpr_operator(s) in op:
        return op[binaryexpr_operator(s)](biny_left, biny_right)


def eval_variable(s, table):
    """Returns the value of a given key in the given table"""
    return table[s]


# --- Correct statements ---
# calc_set_print = ['calc', ["set", "res", 5], ['print', 2], ['print', [4, "+", [2, "*", 2]]], ["print", "res"]]

# calc_if = ['calc', ['if', [[3, "+", 3], '=', 6], ['print', True], ["print", False]]]

# calc_read_print = ['calc', ['read', 'n'], ['print', 'n']]

# calc_fac = ['calc', ['read', 'n'], ['set', 'sum', 1], ['while', ['n', '>', 0], ['set', 'sum', ['sum', '*', 'n']], ['set', 'n', ['n', '-', 1]]], ['print', 'sum']]

# calc_fib = ['calc', ['read', 'steps'], ['set', 'n', 1], ['set', 'n0', 0], ['while', ['steps', '>', 0], ['set', 'n', ['n', '+', 'n0']], ['set', 'n0', ['n', '-', 'n0']], ['print', 'n'], ['set', 'steps', ['steps', '-', 1]]]]


# # --- Faulty statements ---
# calc_error_binary = ['calc', ['read', 'n'], ['set', 'n', ['n', '%', 2]], ['print', 'n']]

# calc_error_not_calc = ['hej', ['print', 5]]

# exec_program(calc_error_not_calc)
