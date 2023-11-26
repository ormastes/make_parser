from Types import LexerNodeType, TokenNodeType


class Nodable:
    def __init__(self, text: str, type, children: list):
        self.text = text
        self._children = [] if children is None else children
        self.type = type

    def __str__(self):
        return self.text+ '(' + str(self.type) + ')'

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Nodable):
            return False
        if not self.text == __value.text or not self.type == __value.type:
            return False
        if len(self.children()) != len(__value.children()):
            return False
        for i in range(len(self.children())):
            if not self.children()[i] == __value.children()[i]:
                return False
        return True
    
    def children(self):
        return self._children
    def set_children(self, children):
        self._children = children
    def append_child(self, child):
        self._children.append(child)

class TokenNode(Nodable):
    def __init__(self, text: str, type: TokenNodeType=TokenNodeType.TEXT, children: list=None):
        super().__init__(text, type, children)


class LexerNode(Nodable):
    def __init__(self, text:str, type: LexerNodeType, token: TokenNode=None, children: list=None):
        super().__init__(text, type, children)
        self.token = token
        self.direct_children = []
        self.secondary_children = []

    def actual_children(self):
        return self._children

    def children(self):
        return self.direct_children + self.secondary_children + self._children

class CommonProcessor:
    def __init__(self):
        pass

    def isProcessed(self, node):
        if isinstance(node, LexerNode):
            return True
        if isinstance(node, TokenNode) and node.type != TokenNodeType.TEXT:
            return True
        return False
    
    def append_str_end(node_line: list, text: str):
        if len(node_line) == 0 or not isinstance(node_line[-1], str):
            node_line.append(text)
        elif isinstance(node_line[-1], str):
            node_line[-1] += text

    def open_parenthese(token: TokenNode, cur_prenthesis_stack, new_line: list):
        node = LexerNode(token.text, LexerNodeType.PARENTHESIS, token)
        if len(cur_prenthesis_stack) == 0:
            new_line.append(node)
            cur_prenthesis_stack.append(node)
        else:
            new_line[-1].append_child(node)
            cur_prenthesis_stack.append(node)

    def close_parenthese(token: TokenNode, cur_parenthese: list):
        if len(cur_parenthese) == 0:
            raise Exception('Invalid Makefile')
        else:
            new_node = TokenNode(token.text, TokenNodeType.PARSED_TEXT)
            assert cur_parenthese[-1].type == LexerNodeType.PARENTHESIS
            # cur_parenthese[-1].append_child(new_node)
            cur_parenthese.pop()

    def append_simple_node(new_node_line: list, cur_node_stack: list, node: Nodable):
        if len(cur_node_stack) == 0:
            new_node_line.append(node)
        else:
            cur_node_stack[-1].append_child(node)

    def open_block(new_node_line:list, cur_node_stack:list, node: LexerNode):
        if node.text == 'define':
            new_node = LexerNode(node.text, LexerNodeType.DEFINE, node)
        elif node.text == 'undefine':
            new_node = LexerNode(node.text, LexerNodeType.UNDEFINE, node)
        else:
            new_node = LexerNode(node.text, LexerNodeType.CONDITIONAL, node)
            
        if len(cur_node_stack) == 0:
            new_node_line.append(new_node)
        else:
            cur_node_stack[-1].append_child(new_node)
        cur_node_stack.append(new_node)
    def else_block(new_node_line:list, cur_node_stack:list, node):
        if len(cur_node_stack)==0 or cur_node_stack[-1].type != LexerNodeType.CONDITIONAL or cur_node_stack[-1].text not in  ['ifeq', 'ifneq', 'ifdef', 'ifndef']:
            raise Exception('Invalid Makefile')
        new_node = LexerNode(node.text, LexerNodeType.CONDITIONAL, node)
        cur_node_stack[-1].append_child(new_node)
        cur_node_stack.append(new_node)

    def close_block(new_node_line:list, cur_node_stack:list, node: LexerNode):
        if len(cur_node_stack)==0:
            raise Exception('Invalid Makefile')
        if cur_node_stack[-1].type == LexerNodeType.CONDITIONAL:
            if cur_node_stack[-1].text == 'else':
                cur_node_stack.pop()
            if len(cur_node_stack) == 0:
                raise Exception('Invalid Makefile')
            if cur_node_stack[-1].text in ['ifeq', 'ifneq', 'ifdef', 'ifndef']:
                cur_node_stack.pop()
            else:
                raise Exception('Invalid Makefile')
        elif cur_node_stack[-1].type == LexerNodeType.DEFINE:
            if cur_node_stack[-1].text == 'define':
                cur_node_stack.pop()
            else:
                raise Exception('Invalid Makefile')
        elif cur_node_stack[-1].type == LexerNodeType.UNDEFINE:
            if cur_node_stack[-1].text == 'undefine':
                cur_node_stack.pop()
            else:
                raise Exception('Invalid Makefile')
        else:
            raise Exception('Invalid Makefile')