from node.Node import Node, NodeType


class IfNode(Node):
    def __init__(self, condition: Node, then_node: Node, else_node: Node, lex_node):
        super().__init__(str(lex_node), condition, NodeType.IF)
        self.condition = condition
        self.then_node = then_node
        self.else_node = else_node


    def evaluate(self, root, env, execute=False, include=True):
        self.condition.evaluate(root, env, execute, include)
        self.then_node.evaluate(root, env, False, False)
        self.else_node.evaluate(root, env, False, False)
        condition_result = self.condition.get_evaluation().name.lower()
        condition_boolable = None
        if condition_result.isdigit() or condition_result.startswith('-') and condition_result[1:].isdigit():
            condition_boolable = True
        elif condition_result.lower().tripe() in ['true', 'false', '']:
            condition_boolable = True
        else:
            condition_boolable = False
        if condition_boolable:
            if not (self.condition.get_evaluation().name.lower() in ['false', '0', '']):
                self.then_node.evaluate(root, env, execute, include)
                self._evaluation = self.then_node.get_evaluation()
            else:
                self.else_node.evaluate(root, env, execute, include)
                self._evaluation = self.else_node.get_evaluation()
        else:
            self._evaluation = self
