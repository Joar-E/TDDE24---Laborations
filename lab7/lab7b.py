"""Hjälpfunktioner"""
def is_empty_tree(tree):
    return isinstance(tree, list) and not tree


def is_leaf(tree):
    return isinstance(tree, int)


def create_tree(left_tree, key, right_tree):
    return [left_tree, key, right_tree]

	
def left_subtree(tree):
    return tree[0]

def node(tree):
    return tree[1]

def right_subtree(tree):
    return tree[2]

# ----------------------------------------------------------------------

def empty_tree_fn():
    return 0

def leaf_fn(leaf_key):
    return leaf_key**2

def inner_node_fn(inner_node_key, left_value, right_value):
    return inner_node_key + left_value

"""Huvudfunktion"""
def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
    if is_empty_tree(tree):
        return empty_tree_fn()
    elif isinstance(left_subtree(tree), list):
        return inner_node_fn(node(tree), leaf_fn(traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)), right_subtree(tree))

    else:
        return inner_node_fn(node(tree), leaf_fn(left_subtree(tree)), right_subtree(tree))

def contains_key(search_value, tree):
    pass

