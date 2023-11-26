from node.Node import Node, NodeType
class DefineNode(Node):
    def __init__(self, name : Node, value : Node, lex_node):
        super().__init__(str(lex_node), lex_node, NodeType.DEFINE)
        self.name = name
        self.value = value
