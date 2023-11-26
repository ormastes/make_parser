from node.Node import Node, NodeType

class ExportNode(Node):
    def __init__(self, name : Node, lex_node):
        super().__init__(str(lex_node), lex_node, NodeType.EXPORT)
        self.name = name
