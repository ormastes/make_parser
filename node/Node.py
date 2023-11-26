from enum import Enum
from Common import Nodable, LexerNode

class NodeType(Enum):
    ROOT = 0
    ASSIGN = 1
    RULE = 2
    IF = 3
    INCLUDE = 4
    EXPORT = 5
    DEFINE = 6
    UNDEFINE = 7
    COMMAND = 8
    FUNCTION = 9
    STATEMENTS = 10
    EXPRESSION = 11
    TEXT = 12

class EnvVar:
    def __init__(self, args , body):
        self.args = args
        self.body = body
class Env(dict):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        elif self.parent is not None:
            return self.parent[key]
        else:
            raise KeyError(key)


class Writer:

    def write(self, text):
        pass
class DefaultWriter(Writer):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_out = open(file_name, 'w')

    def write(self, text):
        self.file_out.write(text)

class WriterMap(dict):
    def __init__(self, writer_class, parent=None):
        super().__init__()
        self.writer_class = writer_class
        self.parent = parent

    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        elif self.parent is not None:
            return self.parent[key]
        else:
            raise KeyError(key)

    def get_writer(self, key):
        val = self[key]
        if val is None:
            return None
        else:
            # create instance of writer_class
            return self.writer_class(val)

class Generator:
    def generate_pre(self, node, writer):
        pass
    def generate_post(self, node, writer):
        pass
class Node(Nodable):
    def __init__(self, text: str, lex_node:LexerNode, type: NodeType):
        super().__init__(text, type, None)
        self.lexer_node = lex_node
        self._evaluation = None

    def __str__(self):
        if self._evaluation is not None and self._evaluation != self:
            return str(self._evaluation)
        else:
            return self.text

    def get_name(self):
        assert False

    def evaluate(self, root, env:dict, execute=False, include=True):
        self.children().evaluate(root, env, execute, include)

    def get_evaluation(self):
        if self._evaluation is not None:
            return self._evaluation
        else:
            return self.children()[0] if len(self.children()) == 1 else self.children()

    def generate(self, root, env:dict, writer_map, generator, execute=False, include=True):
        self.evaluate(root, env, execute, include)
        writer = writer_map.get_writer(self)
        assert writer is not None
        generator.generate_pre(self, writer)
        self.children().generate(root, writer_map, include)
        generator.generate_post(self, writer)


