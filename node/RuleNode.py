from node.Node import Node, NodeType

class RuleNode(Node):
    def __init__(self, name : Node, depends : list, commands: list, lex_node):
        super().__init__(str(lex_node), lex_node, NodeType.RULE)
        self.name = name
        self.depends = depends
        self.commands = commands

    def evaluate(self, root, env, execute=False, include=True):
        self.name.evaluate(root, env, execute, include)
        for depend in self.depends:
            depend.evaluate(root, env, execute, include)
        for command in self.commands:
            command.evaluate(root, env, execute, include)
        self._evaluation = self