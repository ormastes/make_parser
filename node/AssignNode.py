from node.Node import Node, NodeType, EnvVar


class AssignNode(Node):
    def __init__(self, name : Node, value : Node, lex_node):
        super().__init__(str(lex_node), lex_node, NodeType.ASSIGN)
        self.name = name
        self.value = value

    def get_name(self):
        return str(self.name)

    def evaluate(self, root, env, execute=False, include=True):
        self.name.evaluate(root, env, execute, include)
        self.value.evaluate(root, env, execute, include)
        if self.lexer_node.text == '==':
            env[self.name.text] = EnvVar([], self.value)
        elif self.lexer_node.text == '+=':
            if not isinstance(env[self.name.text].body, list):
                val = [env[self.name.text]]
            env[self.name.text].body.append(self.value)
        self._evaluation = self

    def children(self):
        return [self.name, self.value]
