from node.Node import Node, NodeType


class RootNode(Node):
    def __init__(self, file_name:str, nodes : list, lex_node):
        super().__init__(str(lex_node), lex_node,  NodeType.ROOT)
        self.file_name = file_name
        self._children = nodes

    def evaluate(self, root, env, execute=False, include=True):
        for node in self.children():
            node.evaluate(root, env, execute, include)
        self._evaluation = self

    def get_name(self):
        return self.file_name