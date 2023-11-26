from node.Node import Node, NodeType

class ExpressionNode(Node):
    def __init__(self, children: list):
        super().__init__(str(children), None, NodeType.EXPRESSION)
        self.set_children(children)

    def __str__(self):
        if self._evaluation is not None:
            return str(self._evaluation)
        else:
            result = ""
            for child in self.children():
                result += str(child)
            return result