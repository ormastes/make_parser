import os

from node.Node import Node, NodeType
from node.RootNode import RootNode


class IncludeNode(Node):
    def __init__(self, file : Node, lex_node):
        super().__init__(str(lex_node), lex_node, NodeType.INCLUDE)
        self.file = file
        self.root = None

    def get_name(self):
        return str(self.file)

    def evaluate(self, root:RootNode, env:dict, execute=False, include=True):
        from Lexer import Lexer
        from Parser import Parser
        from Preprocessor import Preprocess
        from Tokenizer import Tokenizer

        if self.root is None and include:
            cur_file_name = root.file_name
            cur_dir = os.path.dirname(cur_file_name)
            include_file_name = ''
            if len(self.file.children()) == 0:
                include_file_name = self.file.evaluate(root, env, execute, include)
            else:
                for val in self.children():
                    include_file_name += val.evaluate(root, env, execute, include)
            include_file_name = os.path.join(cur_dir, include_file_name)
            # read all file contents
            with open(include_file_name, 'r') as f:
                include_text = f.read()

                result = Preprocess.preprocess(include_text)
                tokens = [Tokenizer.tokenize(line) for line in result]
                lex_root = Lexer.lexing(tokens)
                include_root = Parser(lex_root).parse()
                self.root = RootNode(include_file_name, include_root, lex_root)

            self.file.evaluate(root, env, False, False)
            if self.root is not None:
                self.root.evaluate(self.root, env, execute, include)
                self._evaluation = self.root.get_evaluation()
