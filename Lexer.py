from Common import CommonProcessor, LexerNode, TokenNode
from Types import LexerNodeType, TokenNodeType, assign_tokens, rule_tokens, specifier_tokens

# Lexer for Makefile It process parenthesis, then define, conditional
# TODO: specifier is not implemented yet
class Lexer(CommonProcessor):
    """
    The Lexer class is responsible for lexing the input code and generating a parse tree.

    Args:
        CommonProcessor (class): The base class for common processing operations.

    Methods:
        lex_parenthese(root: LexerNode): Lexes the parentheses in the code.
        lex_simple(parent: LexerNode, token: str, type: NodeType, cur_node_stack: list=[]): Lexes simple tokens in the code.
        lex_multi_line(parent: LexerNode, cur_node_stack: list=[]): Lexes multi-line blocks in the code.
        _lex_line(parent: LexerNode, target_tokens, lexer_type): Helper method to lex a line of code.
        lex_line(parent, cur_node_stack: list=[]): Lexes a line of code.
        lex_expression(parent: LexerNode, cur_node_stack: list=[]): Lexes expressions in the code.
        check_lex_node(parent: LexerNode): Checks if the lexed nodes are valid.
        lexing(node_line: list): Performs the lexing operation on the input code and returns the root of the parse tree.
    """
    
    def lex_parenthese(root: LexerNode):
        """
        Lexes the parentheses in the given root node.

        Args:
            root (LexerNode): The root node to process.

        Raises:
            Exception: If an invalid Makefile is encountered.

        Returns:
            None
        """
        cur_parenthese = []
        new_node_lines = []
        for line in root.children():
            new_node_line = []
            for node in line:
                if node.type == TokenNodeType.PARSED_TEXT:
                    if node.text in ['$(', '@(', '(']:
                        CommonProcessor.open_parenthese(node, cur_parenthese, new_node_line)
                    elif node.text == ')':
                        CommonProcessor.close_parenthese(node, cur_parenthese)
                    else:
                        CommonProcessor.append_simple_node(new_node_line, cur_parenthese, node)
                else:
                    CommonProcessor.append_simple_node(new_node_line, cur_parenthese, node)
            if len(cur_parenthese) != 0:
                raise Exception('Invalid Makefile')
            new_node_lines.append(new_node_line)
        root.set_children(new_node_lines)
    
    def lex_simple(parent: LexerNode, token: str, type: LexerNodeType, cur_node_stack: list=[]):
        """
        Lexes a simple token in the lexer tree.

        Args:
            parent (LexerNode): The parent node in the lexer tree.
            token (str): The token to be lexed.
            type (NodeType): The type of the new lexer node.
            cur_node_stack (list, optional): The current node stack. Defaults to [].
        """
        cur_node_stack.append(parent)
        new_node_lines = []
        for line in parent.children():
            new_node_line = []
            for idx, node in enumerate(line):
                if isinstance(node, TokenNode) and node.text == token:
                    new_node = LexerNode(node.text, type, node)
                    new_node.set_children(line[idx+1:])
                    new_node_line.append(new_node)
                    break
                else:
                    new_node_line.append(node)
            new_node_lines.append(new_node_line)
        parent.set_children(new_node_lines)
        cur_node_stack.pop()


    def lex_multi_line(parent: LexerNode, cur_node_stack: list=[]):
        """
        Lexes multi-line nodes in a Makefile.

        Args:
            parent (LexerNode): The parent node to process.
            cur_node_stack (list, optional): The stack of current nodes. Defaults to an empty list.

        Raises:
            Exception: If the Makefile is invalid.

        Returns:
            None
        """
        old_nodes = parent.children()
        new_node_lines = []
        for node_line in old_nodes:
            direct_child = False
            new_node_line = []
            for node_idx in range(len(node_line)):
                node = node_line[node_idx]
                if node.type == TokenNodeType.PARSED_TEXT:
                    if node.text in ['define', 'ifeq', 'ifneq', 'ifdef', 'ifndef']:
                        direct_child = True
                        CommonProcessor.open_block(new_node_line, cur_node_stack, node)
                    elif node.text == 'else':
                        CommonProcessor.else_block(new_node_line, cur_node_stack, node)
                    elif node.text in ['endif', 'endef']:
                        CommonProcessor.close_block(new_node_line, cur_node_stack, node)
                    elif direct_child:
                        cur_node_stack[-1].direct_children().append(node)
                    else:
                        if cur_node_stack[-1].type != LexerNodeType.LINE:
                            line = LexerNode('', LexerNodeType.LINE)
                            cur_node_stack[-1].append_child(line)
                            cur_node_stack.append(line)
                        CommonProcessor.append_simple_node(new_node_line, cur_node_stack, node)
                else:
                    if direct_child:
                        cur_node_stack[-1].direct_children.append(node)
                    else:
                        if cur_node_stack[-1].type != LexerNodeType.LINE:
                            line = LexerNode('', LexerNodeType.LINE)
                            cur_node_stack[-1].append_child(line)
                            cur_node_stack.append(line)
                        CommonProcessor.append_simple_node(new_node_line, cur_node_stack, node)
            if len(cur_node_stack)>0 and cur_node_stack[-1].type == LexerNodeType.LINE:
                cur_node_stack.pop()
            if len(new_node_line)>0:
                new_node_lines.append(new_node_line)
        parent.set_children(new_node_lines)
        if len(cur_node_stack) != 0:
            raise Exception('Invalid Makefile')
        
    def _lex_line(parent: LexerNode, target_tokens, lexer_type):
        """
        Lexes a line of code and returns a new LexerNode.

        Args:
            parent (LexerNode): The parent node.
            target_tokens (list): The list of target tokens.
            lexer_type: The lexer type.

        Returns:
            LexerNode: The new LexerNode.
        """
        ndix = 0
        for node in parent.children():
            if node.text in target_tokens:
                break
            ndix += 1
        new_node = LexerNode(parent.children()[ndix].text, lexer_type, children=parent.children()[ndix+1:])
        new_node.direct_children = parent.children()[:ndix]
        return new_node

    def lex_line(parent, cur_node_stack: list=[]):
        """
        Lexes a line of the Makefile and updates the parent node with the lexed nodes.

        Args:
            parent: The parent node to update with the lexed nodes.
            cur_node_stack: A list representing the current node stack.

        Returns:
            None

        Raises:
            Exception: If the Makefile is invalid.
        """
        new_node_lines = []
        cur_children = parent.children()
        cur_node_stack.append(parent)
        idx = 0
        for node in cur_children:
            new_node_line = []
            if node.type in [LexerNodeType.DEFINE, LexerNodeType.CONDITIONAL]:
                Lexer.lex_line(node, cur_node_stack)
            elif node.type == LexerNodeType.LINE:
                assign_nodes = [1 if node.text in assign_tokens else 0 for node in node.children()]
                rule_nodes = [1 if node.text in rule_tokens else 0 for node in node.children()]
                if sum(assign_nodes) >1:
                    raise Exception('Invalid Makefile')
                if sum(rule_nodes) >1:
                    raise Exception('Invalid Makefile')
                if sum(assign_nodes) == 1 and sum(rule_nodes) == 1:
                    raise Exception('Invalid Makefile')
                if sum(assign_nodes) == 1:
                    new_node_line = Lexer._lex_line(node, assign_tokens, LexerNodeType.ASSIGN)
                elif sum(rule_nodes) == 1:
                    new_node_line = Lexer._lex_line(node, rule_tokens, LexerNodeType.RULE)
                elif len(node.children()) == 1:
                    new_node_line = node.children()[0]
                else:
                    raise Exception('Invalid Makefile')
            else:
                raise Exception('Invalid Makefile')
            new_node_lines.append(new_node_line)
        parent.set_children(new_node_lines)

    def lex_expression(parent: LexerNode, cur_node_stack: list=[]):
        """
        Lexically analyzes an expression and constructs a lexer node hierarchy.

        Args:
            parent (LexerNode): The parent node of the expression.
            cur_node_stack (list, optional): The current node stack. Defaults to an empty list.

        Raises:
            Exception: If the Makefile is invalid.

        Returns:
            None
        """
        cur_node_stack.append(parent)
        new_node_lines = []
        for idx in range(len(parent.children())):
            node = parent.children()[idx]
            if node.type == LexerNodeType.PARENTHESIS and node.text == '$(': # function
                new_node = LexerNode(node.text, LexerNodeType.FUNCTION, node)
                new_node.set_children(node.children()[idx+1:])
                new_node.direct_children = parent.children()[:idx]
                new_node_lines.append(new_node)
                Lexer.lex_expression(node, cur_node_stack)
            elif isinstance(node, TokenNode) :
                if node.type == TokenNodeType.TEXT:
                    if len(node.children())>0:
                        raise Exception('Invalid Makefile') 
                    new_node = LexerNode(node.text, LexerNodeType.TEXT, node)
                    new_node_lines.append(new_node)
                else:
                    raise Exception('Invalid Makefile')
            elif isinstance(node, LexerNode):
                if node.type in [LexerNodeType.PARENTHESIS, LexerNodeType.ASSIGN, LexerNodeType.RULE, LexerNodeType.FUNCTION, 
                                 LexerNodeType.CONDITIONAL, LexerNodeType.DEFINE, LexerNodeType.INCLUDE, LexerNodeType.EXPORT]:
                    new_node_lines.append(node)
                    Lexer.lex_expression(node, cur_node_stack)
                else:
                    raise Exception('Invalid Makefile')
            else:
                raise Exception('Invalid Makefile')
            
        parent.set_children(new_node_lines)
        cur_node_stack.pop()

    def lex_function_from_parenthese(parent: LexerNode):
        """
        Lexes a function from the parentheses in the given parent node.

        Args:
            parent (LexerNode): The parent node to process.
        """
        new_node_lines = []
        for node_line in parent.children():
            new_node_line = []
            for node in node_line:
                if node.type == LexerNodeType.PARENTHESIS and node.text == '$(':
                    new_node = LexerNode(node.text, LexerNodeType.FUNCTION, node)
                    new_node.set_children(node.children())
                    new_node_line.append(new_node)
                else:
                    new_node_line.append(node)
            new_node_lines.append(new_node_line)
        parent.set_children(new_node_lines)
    def check_lex_node(parent: LexerNode):
        """
        Recursively checks if the given parent LexerNode and its children are valid.
        
        Args:
            parent (LexerNode): The parent LexerNode to check.
        
        Raises:
            Exception: If the parent is not an instance of LexerNode.
        """
        if not isinstance(parent, LexerNode):
            raise Exception('Invalid Makefile')
        for child in parent.children():
            Lexer.check_lex_node(child)

        
    def lexing(self, node_lines: list):
            """
            Perform lexical analysis on the given node_line.

            Args:
                node_line (list): The list of nodes representing a line of code.

            Returns:
                LexerNode: The root node of the lexical analysis tree.
            """
            root = LexerNode('', LexerNodeType.ROOT)
            root.set_children(node_lines)

            Lexer.lex_parenthese(root)

            #######################
            # simple cases
            Lexer.lex_simple(root, 'include', LexerNodeType.INCLUDE)
            Lexer.lex_simple(root, 'export', LexerNodeType.EXPORT)

            #######################
            # if 
            # define
            Lexer.lex_multi_line(root);

            #######################
            # function
            # rule
            Lexer.lex_line(root)

            #######################
            # text
            # function
            # TODO: specifier
            Lexer.lex_expression(root)

            Lexer.lex_function_from_parenthese(root)

            Lexer.check_lex_node(root)

            return root
