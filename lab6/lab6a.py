"""
ConstCalc
"""
from calc import *

def exec_program(p: list()):
    if is_program(p):
        define_statements(program_statements(p))


def define_statements(statements):
    if statements == []:
        return None
    elif is_output(statements[0]):
        print(output_expression(statements[0]))
        return define_statements(rest_statements(statements))


def if_statement(statement):
    cond = selection_condition(statement)
    if is_condition(cond):
        if condition_operator(cond) == '<':
            if condition_left(cond) < condition_right(cond):
                return True
            return False
        elif condition_operator(cond) == '>':
            if condition_left(cond) > condition_right(cond):
                return True
            return False
        elif condition_operator(cond) == '=':
            if condition_left(cond) == condition_right(cond):
                return True
            return False


cond = ['if', [3, '>', 5], ['print', 2], ['print', 4]]

print(if_statement(cond))

calc1 = ['calc', ['print', 2], ['print', 4], ['print', 73]]

exec_program(calc1)

#def exec_statement(s: list())
