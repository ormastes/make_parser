import unittest
from Common import LexerNode, TokenNode
from Lexer import Lexer
from Types import LexerNodeType, TokenNodeType

class LexerTests(unittest.TestCase):
    def test_lex_parenthesis(self):
        # Test case 1: Valid Makefile with parentheses
        lines = [
            [             
                #$(TARGET) 
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('TARGET'), TokenNode(')', TokenNodeType.PARSED_TEXT)
            ],
            [   # $(TARGET).c 
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('TARGET'), TokenNode(')', TokenNodeType.PARSED_TEXT),
                #$(LIBS)
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('LIBS'), TokenNode(')', TokenNodeType.PARSED_TEXT)
            ]
        ]
        root = LexerNode('', LexerNodeType.ROOT)
        root.set_children(lines)

        expected = [
            [LexerNode('$(', LexerNodeType.PARENTHESIS, [TokenNode('TARGET')])],
            [LexerNode('$(', LexerNodeType.PARENTHESIS, [TokenNode('TARGET')]), LexerNode('$(', LexerNodeType.PARENTHESIS, [TokenNode('LIBS')])]
        ]
        expected[0][0].set_children([TokenNode('TARGET')])
        expected[1][0].set_children([TokenNode('TARGET')])
        expected[1][1].set_children([TokenNode('LIBS')])
        Lexer.lex_parenthese(root)
        children = root.children()
        self.assertEqual(children, expected)

    def test_lex_parenthese_invalid(self): 
        # Test case 2: Invalid Makefile with unmatched parentheses
        lines = [
            [             
                #$(TARGET) 
                LexerNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('TARGET'), TokenNode(')', TokenNodeType.PARSED_TEXT)
            ],
            [   # $(TARGET).c 
                LexerNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('TARGET'),
                #$(LIBS)
                LexerNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('LIBS'), TokenNode(')', TokenNodeType.PARSED_TEXT)
            ]
        ]
        
        root = LexerNode('', LexerNodeType.ROOT)
        root.set_children(lines)
        self.assertRaises(Exception, Lexer.lex_parenthese, root)

    def test_lex_parenthese_nested(self):
        # include parentheses 
        lines = [
            [             
                #$(TARGET) 
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('TARGET'), TokenNode(')', TokenNodeType.PARSED_TEXT)
            ],
            [   # $(TARGET
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('TARGET'), 
                #$(LIBS))
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('LIBS'), TokenNode(')', TokenNodeType.PARSED_TEXT,), TokenNode(')', TokenNodeType.PARSED_TEXT)
            ]
        ]
        root = LexerNode('', LexerNodeType.ROOT)
        root.set_children(lines)

        expected = [
            [LexerNode('$(', LexerNodeType.PARENTHESIS, [TokenNode('TARGET')])],
            [LexerNode('$(', LexerNodeType.PARENTHESIS, [TokenNode('TARGET'), LexerNode('$(', LexerNodeType.PARENTHESIS, [TokenNode('LIBS')])])]
        ]
        expected[0][0].set_children([TokenNode('TARGET')])
        expected[1][0].set_children([TokenNode('TARGET'), LexerNode('$(', LexerNodeType.PARENTHESIS, [TokenNode('LIBS')])])
        expected[1][0].children()[1].set_children([TokenNode('LIBS')])
        Lexer.lex_parenthese(root)
        self.assertEqual(root.children(), expected)

    def test_lex_simple(self):
        # Test case 1: Lexing a simple token
        lines = [
            [             
                #$(TARGET) 
                TokenNode('include', TokenNodeType.PARSED_TEXT), TokenNode('XXX')
            ],
        ]
        parent = LexerNode(lines, LexerNodeType.ROOT)
        parent.set_children(lines)
        expected = [[LexerNode('include', LexerNodeType.INCLUDE, children=[TokenNode('XXX')])]]
        Lexer.lex_simple(parent, 'include', LexerNodeType.INCLUDE)
        self.assertEqual(parent.children(), expected)

    def test_lex_multi_line_if(self):
        # Test if case
        lines = [
            [             
                TokenNode('ifeq', TokenNodeType.PARSED_TEXT), TokenNode('XXX')
            ],
            [             
                TokenNode('YYY')
            ],
            [             
                TokenNode('endif', TokenNodeType.PARSED_TEXT)
            ]
        ]
        parent = LexerNode(lines, LexerNodeType.ROOT)
        parent.set_children(lines)
        expected = [[LexerNode('ifeq', LexerNodeType.CONDITIONAL, children=[TokenNode('XXX'), LexerNode('',LexerNodeType.LINE,children=[ TokenNode('YYY')])])]]
        Lexer.lex_multi_line(parent)
        self.assertEqual(parent.children(), expected)
    def test_lex_multi_line_if_else(self):
        # Test if else case
        lines = [
            [             
                TokenNode('ifeq', TokenNodeType.PARSED_TEXT), TokenNode('XXX')
            ],
            [             
                TokenNode('YYY')
            ],
            [             
                TokenNode('else', TokenNodeType.PARSED_TEXT)
            ],
            [             
                TokenNode('ZZZ')
            ],
            [             
                TokenNode('endif', TokenNodeType.PARSED_TEXT)
            ]
        ]
        parent = LexerNode(lines, LexerNodeType.ROOT)
        parent.set_children(lines)
        expected = [[LexerNode('ifeq', LexerNodeType.CONDITIONAL, children=[TokenNode('XXX'), LexerNode('',LexerNodeType.LINE,children=[ TokenNode('YYY')]), 
                                                                            LexerNode('else', LexerNodeType.CONDITIONAL,
                                                                                       children=[LexerNode('',LexerNodeType.LINE,children=[ TokenNode('ZZZ')])])])]]
        Lexer.lex_multi_line(parent)
        self.assertEqual(parent.children(), expected)

    def test_lex_multi_line_define(self):
        # Test define case
        lines = [
            [             
                TokenNode('define', TokenNodeType.PARSED_TEXT), TokenNode('XXX')
            ],
            [             
                TokenNode('YYY')
            ],
            [             
                TokenNode('endef', TokenNodeType.PARSED_TEXT)
            ]
        ]
        parent = LexerNode(lines, LexerNodeType.ROOT)
        parent.set_children(lines)
        expected = [[LexerNode('define', LexerNodeType.DEFINE, children=[TokenNode('XXX'),LexerNode('',LexerNodeType.LINE,children=[ TokenNode('YYY')])])]]
        Lexer.lex_multi_line(parent)
        self.assertEqual(parent.children(), expected)


    def test_lex_line_assign(self):
        lines = [
            LexerNode('', LexerNodeType.LINE, children=[TokenNode('YYY'), TokenNode('=', TokenNodeType.PARSED_TEXT), TokenNode('XXX')]),
            LexerNode('', LexerNodeType.LINE, children=[TokenNode('XXX'), TokenNode('=', TokenNodeType.PARSED_TEXT), TokenNode('YYY')])
        ]
        parent = LexerNode(lines, LexerNodeType.ROOT)
        parent.set_children(lines)
        expected = [LexerNode('=', LexerNodeType.ASSIGN, children=[TokenNode('YYY'), TokenNode('XXX')]),
                    LexerNode('=', LexerNodeType.ASSIGN, children=[TokenNode('XXX'), TokenNode('YYY')])]
        Lexer.lex_line(parent)
        self.assertEqual(parent.children(), expected)

    def test_lex_line_rule(self):
        pass


    def test_lex_expression(self):
        # Test case 1: Valid Makefile with an expression
        parent = LexerNode('', LexerNodeType.ROOT)
        node1 = LexerNode('$(', LexerNodeType.FUNCTION)
        node2 = TokenNode('CC', TokenNodeType.TEXT)
        node1.set_children([node2])
        #node3 = LexerNode(')', TokenNodeType.PARENTHESIS)
        parent.set_children([node1])
        expected = [LexerNode('$(', LexerNodeType.FUNCTION, children=[LexerNode('CC', LexerNodeType.TEXT)])]
        Lexer.lex_expression(parent)
        self.assertEqual(parent.children(), expected)

        # Test case 2: Invalid Makefile with an invalid expression
        parent = LexerNode('', LexerNodeType.ROOT)
        node1 = LexerNode('$(', TokenNodeType.PARSED_TEXT)
        node2 = LexerNode('CC', TokenNodeType.TEXT)
        parent.set_children([[node1, node2]])
        self.assertRaises(Exception, Lexer.lex_expression, parent)

if __name__ == '__main__':
    unittest.main()