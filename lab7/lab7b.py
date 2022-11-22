"""Hjälpfunktioner"""
def is_empty_tree(tree):
    return isinstance(tree, list) and not tree


def is_leaf(tree):
    return isinstance(tree, int)

def is_node(tree):
    if len(tree) == 3 and isinstance(left_subtree(tree), (list, int)) and isinstance(right_subtree(tree), (list, int)):
        return True
    return False

def create_tree(left_tree, key, right_tree):
    return [left_tree, key, right_tree]

	
def left_subtree(tree):
    return tree[0]

def node(tree):
    return tree[1]

def right_subtree(tree):
    return tree[2]

# ----------------------------------------------------------------------

# def empty_tree_fn():
#     return 0

# def leaf_fn(leaf_key):
#     return leaf_key**2

# def inner_node_fn(inner_node_key, left_value, right_value):
#     return inner_node_key + left_value

"""Huvudfunktion"""
# def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
#     if is_empty_tree(tree):
#         return empty_tree_fn()
#     elif isinstance(left_subtree(tree), list):
#         return inner_node_fn(node(tree), leaf_fn(traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)), right_subtree(tree))

#     else:
#         return inner_node_fn(node(tree), leaf_fn(left_subtree(tree)), right_subtree(tree))

def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
    if is_empty_tree(tree):
        return empty_tree_fn()
    
    elif is_leaf(tree):
        return leaf_fn(tree)
    
    elif is_node(tree):
        left_branch = traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)

        right_branch = traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)

        return inner_node_fn(node(tree), left_branch, right_branch)


def contains_key(search_value, tree):
    
    def inner_node_fn(tree, left_branch, right_branch):
        if search_value == tree or left_branch or right_branch:#in {tree, left_branch, right_branch}
            return True 
        return False
            

    def leaf_fn(tree):
        return search_value == tree
            
    
    def empty_tree_fn():
        return False
    
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)