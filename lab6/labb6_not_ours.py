"""Labb 6"""
#%%
from calc import *

def exec_program(program, table = {}):
    """
    Kontrollerar att ett program börjar med "calc" mha is_program
    i calc.py och anropar exec_statements
    """
    if is_program(program):
        statements = program_statements(program)
        return exec_statements(statements, table)

def exec_statements(statements, table):
    """ Kollar om det finns icke tomma statements och utför exec_statement för varje statement """
    if not empty_statements(statements):
        vars_after_first = exec_statement(first_statement(statements), table)
        return exec_statements(rest_statements(statements), vars_after_first)
    return table

def exec_statement(statement, table):
    """ Kollar vilken typ av statetement som skickas in """
    if is_assignment(statement):
        return exec_assignment(statement, table)
    elif is_repetition(statement):
        return exec_repetition(statement, table)
    elif is_selection(statement):
        return exec_selection(statement, table)
    elif is_output(statement):
        return exec_output(statement, table)
    elif is_input(statement):
        return exec_input(statement, table)
    print("Input was wrong")

def exec_selection(statement, table):
    """ Tolkar ett villkor """
    if is_condition(selection_condition(statement)):
        if eval_condition(selection_condition(statement), table):
            return exec_statement(selection_true_branch(statement), table)
        elif selection_has_false_branch(statement):
            return exec_statement(selection_false_branch(statement), table)
    return table

def exec_output(statement, table):
    """ Printar statement """
    out = output_expression(statement)
    evl = eval_expression(out, table)
    if is_variable(out):
        print(f"{output_expression(statement)} = {evl}")
    else:
        print(evl)
    return table

def exec_assignment(statement, table):
    """ Beräknar ett värde för en variabel i en ny table """
    table = table.copy()
    table[assignment_variable(statement)] = eval_expression(assignment_expression(statement), table)
    return table

def exec_repetition(statement, table):
    table = exec_statements(repetition_statements(statement), table)
    """ Upprepar statements sålänge condition är sann """
    while eval_condition(repetition_condition(statement), table):
        table = exec_statements(repetition_statements(statement), table)
    return table

def exec_input(statement, table):
    """ Läser in en variabel """
    table = table.copy()
    inp = input(f"Enter value for {input_variable(statement)}: ")
    try:
        inp = int(inp)
    except ValueError:
        pass
    table[input_variable(statement)] = eval_expression(inp, table)
    return table

def eval_condition(cond, table):
    """ Tar ett uttryck och returnerar dess sanningsvärde """
    left = eval_expression(condition_left(cond), table)
    right = eval_expression(condition_right(cond), table)
    if condition_operator(cond) == "<":
        return left < right
    if condition_operator(cond) == ">":
        return left > right
    if condition_operator(cond) == "=":
        return left == right

def eval_expression(expr, table):
    """ Kollar om uttrycket är konstant, en variabel eller binärt """
    if is_constant(expr):
        return eval_constant(expr, table)
    if is_variable(expr):
        return eval_variable(expr, table)
    if is_binaryexpr(expr):
        return eval_binaryexpr(expr, table)
    print("Input was incorrect")

def eval_binaryexpr(expr, table):
    """ Tar ut värden för en binary expression och räknar sedan ut resultatet m.h.a operatorn """
    left  = eval_expression(binaryexpr_left(expr), table)
    right = eval_expression(binaryexpr_right(expr), table)
    if binaryexpr_operator(expr) == "+":
        return left + right
    elif binaryexpr_operator(expr) == "-":
        return left - right
    elif binaryexpr_operator(expr) == "*":
        return left * right
    elif binaryexpr_operator(expr) == "/":
        return left / right
    print("Other operators do not work")

def eval_constant(expr, table):
    """ Returnerar värdet på konstanten """
    return expr

def eval_variable(expr, table):
    """ Returnerar variabelns värde i table """
    return table[expr]

# if __name__ == "__main__":
#     #Egna testexempel:

#     #Fungerande exempel
#     exec_program(['calc', ['read', 'a'], ['set', 'b', 2], ['set', 'res', ['a', '+', 'b']], ['print', 'res']])
#     exec_program(['calc', ['set', 'a', 5], ['while', ['a', '>', 0], ['print', 'a'], ['set', 'a', ['a', '-', 1]]]])
#     exec_program(['calc', ['read', 's'], ['if', ['s', '<', 11], ['print', 96], ['print', [68, '+', 1]]]])

#     #Felaktiga exempel:
#     exec_program(['calc', ['set', 'a', [1, '+', 1, '+', 1]]])
#     exec_program(['calc', ['print', 5, 6]])
#     exec_program(['calc', ['set', 'a', [5, '%', 1]]])

calc2 = ['calc', ['if', [[3, "+", 2], '=', 5], ["set", "a", 5], ["print", 2]], ["print", "a"]]
exec_program(calc2)