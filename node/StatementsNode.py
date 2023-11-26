from node.Node import Node, NodeType

class StatementsNode(Node):
    def __init__(self, children: list):
        super().__init__(str(children), None, NodeType.STATEMENTS)
        self.set_children(children)