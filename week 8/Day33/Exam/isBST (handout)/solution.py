def is_bst(tree: dict) -> bool:
    def check_bst(node, min_val, max_val):
        if node is None:
            return True

        node_value = node["value"]
        children = node["children"]

        if not (min_val < node_value < max_val):
            return False
        
        if len(children) > 2:
            return False
        
        left_child = children[0] if len(children) > 0 else None
        right_child = children[1] if len(children) > 1 else None
        
        return (
            check_bst(left_child, min_val, node_value) and
            check_bst(right_child, node_value, max_val)
        )
    
    return check_bst(tree, float('-inf'), float('inf'))


d = eval(input())
print(is_bst(d))