"""Hjälpfunktioner"""
def is_empty_tree(tree):
    return isinstance(tree, list) and not tree


def is_leaf(tree):
    return isinstance(tree, int)


def is_inner_node(tree):
    if len(tree) == 3 and isinstance(left_subtree(tree), (list, int))\
                      and isinstance(right_subtree(tree), (list, int)):
        return True
    return False


def create_tree(left_tree, key, right_tree):
    return [left_tree, key, right_tree]

	
def left_subtree(tree):
    return tree[0]


def tree_key(tree):
    return tree[1]


def right_subtree(tree):
    return tree[2]

# ----------------------------------------------------------------------


def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
    """A general function for traversing a binary tree and applying
       given functions"""

    if is_empty_tree(tree):
        return empty_tree_fn()
    
    elif is_leaf(tree):
        return leaf_fn(tree)
    
    elif is_inner_node(tree):
        left_branch = traverse(left_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)

        right_branch = traverse(right_subtree(tree), inner_node_fn, leaf_fn, empty_tree_fn)

        return inner_node_fn(tree_key(tree), left_branch, right_branch)


def contains_key(search_value, tree):
    """Defines functions for searching for a given value in a binary tree"""

    def inner_node_fn(tree, left_branch, right_branch):
        if search_value == tree or left_branch or right_branch:
            return True 
        return False
            

    def leaf_fn(tree):
        return search_value == tree
            
    
    def empty_tree_fn():
        return False
    
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)
    


def tree_size(tree):
    """Defines functions for returning the size of binary tree"""

    def inner_node_fn(tree, left_branch, right_branch):
        return 1 + left_branch + right_branch


    def leaf_fn(tree):
        return 1


    def empty_tree_fn():
        return 0

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def tree_depth(tree):
    """Defines functions for returning the depth of a binary tree"""

    def inner_node_fn(tree, left_branch, right_branch):
        return 1 + max(left_branch, right_branch)


    def leaf_fn(tree):
        return 1


    def empty_tree_fn():
        return 0

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


if __name__ == '__main__':

    """Tests for the contains_key function"""
    assert contains_key(2, [1, 2, 3])
    assert contains_key(3, [[], 4, 3])
    assert contains_key(5, [[3, 7, []], 4, [[1, 2, 3], 8, [5, 6, []]]])

    assert contains_key(5, [1, 2, 3]) == False
    assert contains_key(93, [[], 4, 3]) == False
    assert contains_key(9, [[3, 7, []], 4, [[1, 2, 3], 8, [5, 6, []]]]) == False

    print("Contains_key past all tests")

#-----------------------------------------------------------------

    """Tests for the tree_size function"""
    assert tree_size(3) == 1
    assert tree_size([1, 3, []]) == 2
    assert tree_size([2, 4, 8]) == 3
    assert tree_size([[1, 2, []], 3, []]) == 3
    assert tree_size([[[1, 6, 1], 3, []], 1, [[1, 1, 1], 5, [6, 5, 5]]]) == 12

    print("Tree_size passed all the tests")

#-----------------------------------------------------------------

    """Tests for the tree_depth function"""
    assert tree_depth(4) == 1
    assert tree_depth([[], 3, [1, 2, 3]]) == 3
    assert tree_depth([[[1, 5, 2], 8, 3], 9, [3, 2, 1]]) == 4
    assert tree_depth([[1, 5, 2], 6, [[[1, 2, 3], 1, 5], 6, 7]]) == 5

    print("Tree_depth has passed all the tests")