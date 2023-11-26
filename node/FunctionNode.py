from node.Node import Node, NodeType, Env
from node.RootNode import RootNode


class FunctionNode(Node):
    def __init__(self, name : Node, args : Node, lex_node):
        super().__init__(str(lex_node), lex_node, NodeType.FUNCTION)
        self.name = name
        self.args = args if args is not None else []

    def __str__(self):
        if self._evaluation is not None:
            return self._evaluation
        if len(self.args) == 0:
            return f"({self.name})"
        else:
            return f"({self.name} {self.args})"

    def evaluate(self, root:RootNode, env:dict, execute=False, include=True):
        self.name.evaluate(root, env, execute, include)
        for arg in self.args:
            arg.evaluate(root, env, execute, include)

        function = env[self.name.text]
        if function is None:
            return str(self)
        local_env = Env(env)
        assert len(function.args) == len(self.args)
        for i in range(len(self.args)):
            local_env[function.args[i]] = self.args[i]
        function.body.evaluate(root, local_env, execute, include)
        self._evaluation = function.body.get_evaluation()
