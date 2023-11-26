from node.Node import Node, NodeType
class UndefineNode(Node):
    def __init__(self, name : Node, lex_node):
        super().__init__(str(lex_node), lex_node, NodeType.UNDEFINE)
        self.name = name