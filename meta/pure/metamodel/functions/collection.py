class TreeNode:

    def __init__(self, children_data: list["TreeNode"] = None):
        self.children_data = [] if children_data is None else children_data

