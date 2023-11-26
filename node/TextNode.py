from node.Node import Node, NodeType

class TextNode(Node):
    def __init__(self, text : str, lex_node):
        super().__init__(text, lex_node, NodeType.TEXT)

    def __str__(self):
        return self.text
