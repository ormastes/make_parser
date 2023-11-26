from Common import CommonProcessor, LexerNode
from Types import LexerNodeType
from node.AssignNode import AssignNode
from node.DefineNode import DefineNode
from node.ExportNode import ExportNode
from node.ExpressionNode import ExpressionNode
from node.FunctionNode import FunctionNode
from node.IfNode import IfNode
from node.IncludeNode import IncludeNode
from node.Node import Node
from node.RootNode import RootNode
from node.RuleNode import RuleNode
from node.UndefineNode import UndefineNode
from node.TextNode import TextNode
from node.StatementsNode import StatementsNode


class Parser(CommonProcessor):
    """
    The Parser class is responsible for parsing the input and generating the parse tree.
    """
        
    def parse_expression(lexer_nodes):
        """
        Parses the given lexer nodes and returns an expression node.

        Args:
            lexer_nodes (LexerNode or list): The lexer nodes to be parsed.

        Returns:
            ExpressionNode: The parsed expression node.

        Raises:
            AssertionError: If the lexer_nodes argument is not of type LexerNode or list.
        """
        if isinstance(lexer_nodes, LexerNode):
            if lexer_nodes.children() is None or len(lexer_nodes.children()) == 0:
                lexer_nodes = [lexer_nodes]
            else:
                lexer_nodes = lexer_nodes.children()
        elif isinstance(lexer_nodes, list):
            pass
        else:
            assert False
        children = []
        for node in lexer_nodes:
            if node.type == LexerNodeType.TEXT:
                children.append(TextNode(node.text, node))
                continue
            elif node.type == LexerNodeType.FUNCTION:
                children.append(FunctionNode(node.text, node))
                continue
            else:
                assert False
        if len(children) == 1:
            return children[0]
        else:
            return ExpressionNode(children)

    def parse_assign(lexer_node: LexerNode):
        """
        Parses an assignment statement from the given lexer node.

        Args:
            lexer_node (LexerNode): The lexer node representing the assignment statement.

        Returns:
            AssignNode: The parsed assignment node.

        """
        if lexer_node.type != LexerNodeType.ASSIGN:
            return None
        name = Parser.parse_expression(lexer_node.direct_children)
        value = Parser.parse_expression(lexer_node.actual_children())
        node = AssignNode(name, value, lexer_node)
        return node
    
    def parse_rule(child: LexerNode):
        """
        Parses a rule from the given LexerNode.

        Args:
            child (LexerNode): The LexerNode representing the rule.

        Returns:
            RuleNode: The parsed RuleNode object.

        """
        if child.type != LexerNodeType.RULE:
            return None
        name = Parser.parse_expression(child.direct_children)
        depends = [Parser.parse_expression(c) for c in child.secondary_children]
        commands = [Parser.parse_expression(c) for c in child.actual_children()]
        node = RuleNode(name, depends, commands, child)
        return node
    
    def parse_if(child: LexerNode):
        """
        Parses an 'if' statement from the given LexerNode.

        Args:
            child (LexerNode): The LexerNode representing the 'if' statement.

        Returns:
            IfNode: The parsed IfNode object representing the 'if' statement.
        """
        if child.type != LexerNodeType.CONDITIONAL:
            return None
        condition = Parser.parse_expression(child.direct_children)
        then_ = None
        else_ = None
        if child.actual_children is not None and (child.actual_children()[-1].type == LexerNodeType.CONDITIONAL and child.actual_children()[-1].text == 'else'):
            then_ = child.actual_children()[:-1]
            else_ = child.actual_children()[-1].actual_children()
        else:
            then_ = child.actual_children()
            else_ = []
        then_nodes = []
        else_nodes = []
        Parser.parse_statement(then_nodes, then_)
        Parser.parse_statement(else_nodes, else_)
        then_node = StatementsNode(then_nodes)
        else_node = StatementsNode(else_nodes)
        node = IfNode(condition, then_node, else_node, child)
        return node

    def parse_include(node: LexerNode):
        """
        Parses an include node from the lexer node.

        Args:
            node (LexerNode): The lexer node to parse.

        Returns:
            IncludeNode: The parsed include node.
        """
        if node.type != LexerNodeType.INCLUDE:
            return None
        new_node = IncludeNode(Parser.parse_expression(node), node)
        return new_node

    def parse_export(node: LexerNode):
        """
        Parses an export node from the lexer and returns a new ExportNode object.

        Args:
            node (LexerNode): The lexer node to parse.

        Returns:
            ExportNode: The parsed ExportNode object.

        """
        if node.type != LexerNodeType.EXPORT:
            return None
        new_node = ExportNode(Parser.parse_expression(node), node)
        return new_node
    
    def parse_define(node: LexerNode):
        """
        Parses a DEFINE node from the lexer and returns a new DefineNode object.

        Args:
            node (LexerNode): The DEFINE node to be parsed.

        Returns:
            DefineNode: The parsed DefineNode object.

        Raises:
            None

        """
        if node.type != LexerNodeType.DEFINE:
            return None
        assert len(node.children()) == 2
        new_node = DefineNode(Parser.parse_expression(node.children()[0]), Parser.parse_expression(node.children()[1]), node)
        return new_node

    def parse_undefine(node: LexerNode):
        """
        Parses an 'undefine' node from the lexer and returns a new UndefineNode object.

        Args:
            node (LexerNode): The lexer node to parse.

        Returns:
            UndefineNode: The parsed UndefineNode object.

        Raises:
            None

        """
        if node.type != LexerNodeType.UNDEFINE:
            return None
        new_node = UndefineNode(Parser.parse_expression(node), node)
        return new_node

    def parse_text(node: LexerNode):
        """
        Parses a LexerNode of type TEXT and returns a new TextNode.

        Args:
            node (LexerNode): The LexerNode to be parsed.

        Returns:
            TextNode: The parsed TextNode.

        """
        if node.type != LexerNodeType.TEXT:
            return None
        new_node = TextNode(node.text, node)
        return new_node

    def parse_statement(children: list, lexer_nodes: list):
        """
        Parses a statement from the lexer node and appends the parsed node to the given children list.

        Args:
            children (list): The list of children nodes.
            lexer_nodes (list): The lexer node to parse.

        Returns:
            None
        """
        for child in lexer_nodes:
            if child.type == LexerNodeType.ASSIGN:
                new_node = Parser.parse_assign(child)
                if new_node is not None:
                    children.append(new_node)
                    continue
            elif child.type == LexerNodeType.RULE:
                new_node = Parser.parse_rule(child)
                if new_node is not None:
                    children.append(new_node)
                    continue
            elif child.type == LexerNodeType.CONDITIONAL:
                new_node = Parser.parse_if(child)
                if new_node is not None:
                    children.append(new_node)
                    continue
            elif child.type == LexerNodeType.INCLUDE:
                new_node = Parser.parse_include(child)
                if new_node is not None:
                    children.append(new_node)
                    continue
            elif child.type == LexerNodeType.EXPORT:
                new_node = Parser.parse_export(child)
                if new_node is not None:
                    children.append(new_node)
                    continue
            elif child.type == LexerNodeType.DEFINE:
                new_node = Parser.parse_define(child)
                if new_node is not None:
                    children.append(new_node)
                    continue
            elif child.type == LexerNodeType.UNDEFINE:
                new_node = Parser.parse_undefine(child)
                if new_node is not None:
                    children.append(new_node)
                    continue
            elif child.type == LexerNodeType.TEXT:
                new_node = TextNode(child.text, child)
                children.append(new_node)
                continue
            else:
                print('Invalid Makefile', child.type, child.text)
                assert False
        

    def parse(lexer_root: LexerNode):
        """
        Parses the input using the specified lexer and generates the parse tree.

        Returns:
            None
        """
        children = []
        Parser.parse_statement(children, lexer_root.children())
        root = RootNode(lexer_root.text, children, lexer_root)
        return root