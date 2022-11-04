"""
ConstCalc
"""
from calc import *

def exec_program(p: list()):
    if is_program(p):
        define_statements(program_statements(p))
    else:
        print("Is not Calc program")


"""def exec_statement(statement):
    if is_output(statement):
        print(output_expression(statement))
    elif is_binaryexpr(statement):
        return None


def define_statements(statements):
    for statement in statements:

        if is_selection(statement):
            exec_statement(eval_condition(statement))
        else:
            exec_statement(statement)"""

def eval_expression(statements):

    if isinstance(statements, list):
        if is_assignment(first_statement(statements)):
            return None
        elif is_repetition(first_statement(statements)):
            return None
        elif is_selection(first_statement(statements)):
            print(eval_condition(first_statement(statements)))

        elif is_output(first_statement(statements)):
            ""
        elif is_input(first_statement(statements)):
            ""
        elif is_binaryexpr(first_statement(statements)):
            eval_binaryoper(first_statement(statements))
    else:
        return first_statement(statements)

cond = selection_condition(['if', [3, '>', 5], ['print', 2], ['print', 4]])

print(eval_expression(condition_left(cond)))

def eval_condition(statement):
    cond = selection_condition(statement)

    cond_left = eval_expression(condition_left(cond))
    cond_right = eval_expression(condition_right(cond))

    if is_condition(cond):
        if condition_operator(cond) == '<' and (cond_left < cond_right):
            return selection_true_branch(statement)

        elif condition_operator(cond) == '>' and (cond_left > cond_right):
            return selection_true_branch(statement)

        elif condition_operator(cond) == '=' and (cond_left == cond_right):
            return selection_true_branch(statement)

        elif selection_has_false_branch(statement):
            return selection_false_branch(statement)
        
        else:
            return False

def eval_binaryoper(statement):
    binary = selection_condition(statement)
    if is_binaryexpr(binary):
        if bineryexp_operator(binary) == "+":
            return False



a = [['if', [3, '>', 5], ['print', 2], ['print', 4]]]

#eval_expression(a)
#calc1 = [['print', 2], ['print', 4]]
#calc2 = ['calc', ['if', [3, '>', 5], ['print', 2], ["print", 4]], ["print", 5]]
#exec_program(calc2)
#exec_program(calc1)