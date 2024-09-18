def identify_leaf_nodes(tree):
    leaf_nodes = []

    def traverse(node):
        if not node["children"]:
            leaf_nodes.append(node["value"])
        else:
            for child in node["children"]:
                traverse(child)

    traverse(tree)

    return leaf_nodes


t = eval(input())

print(identify_leaf_nodes(t))
