import unittest
from Common import CommonProcessor, LexerNode, LexerNodeType
from Parser import Parser
from node.Node import NodeType, Node

class ParserTests(unittest.TestCase):
    def test_parse_expression_single_node(self):
        lexer_node = LexerNode("Hello", LexerNodeType.TEXT)
        result = Parser.parse_expression(lexer_node)
        result_str = str(result)
        self.assertEqual(str(result), "Hello")
        self.assertEqual(len(result.children()), 0)

    def test_parse_expression_multiple_nodes(self):
        lexer_nodes = [
            LexerNode("Hello", LexerNodeType.TEXT),
            LexerNode("world()", LexerNodeType.TEXT)
        ]
        result = Parser.parse_expression(lexer_nodes)
        self.assertEqual(str(result), "Helloworld()")
        self.assertEqual(len(result.children()), 2)
        self.assertEqual(str(result.children()[0]), "Hello")
        self.assertEqual(str(result.children()[1]), "world()")

    def test_parse_assign(self):
        lexer_node = LexerNode("=", LexerNodeType.ASSIGN)
        lexer_node.direct_children = LexerNode("x", LexerNodeType.TEXT)
        lexer_node.set_children([LexerNode("10", LexerNodeType.TEXT)])
        result = Parser.parse_assign(lexer_node)
        self.assertEqual(result.type, NodeType.ASSIGN)
        self.assertEqual(result.lexer_node.text, "=")
        self.assertEqual(len(result.children()), 2)
        self.assertEqual(str(result.name), "x")
        self.assertEqual(str(result.value), "10")

    def test_parse_rule(self):
        lexer_node = LexerNode("rule", LexerNodeType.RULE)
        lexer_node.direct_children = LexerNode("target", LexerNodeType.TEXT)
        lexer_node.secondary_children = [
            LexerNode("dep1", LexerNodeType.TEXT),
            LexerNode("dep2", LexerNodeType.TEXT)
        ]
        lexer_node.set_children( [
            LexerNode("command1", LexerNodeType.TEXT),
            LexerNode("command2", LexerNodeType.TEXT)
        ])
        result = Parser.parse_rule(lexer_node)
        self.assertEqual(result.name.text, "target")
        self.assertEqual(len(result.depends), 2)
        self.assertEqual(result.depends[0].text, "dep1")
        self.assertEqual(str(result.depends[1]), "dep2")
        self.assertEqual(len(result.commands), 2)
        self.assertEqual(result.commands[0].text, "command1")
        self.assertEqual(result.commands[1].text, "command2")

    def test_parse_if(self):
        lexer_node = LexerNode("if", LexerNodeType.CONDITIONAL)
        lexer_node.direct_children = LexerNode("condition", LexerNodeType.TEXT)
        lexer_node_else = LexerNode("else", LexerNodeType.CONDITIONAL)
        lexer_node_else.set_children ( [
            LexerNode("else1", LexerNodeType.TEXT),
            LexerNode("else2", LexerNodeType.TEXT)
        ])
        lexer_node.set_children( [
            LexerNode("then1", LexerNodeType.TEXT),
            LexerNode("then2", LexerNodeType.TEXT),
            lexer_node_else
        ])
        result = Parser.parse_if(lexer_node)
        self.assertEqual(result.condition.text, "condition")

        self.assertEqual(len(result.then_node.children()), 2)
        self.assertEqual(result.then_node.children()[0].text, "then1")
        self.assertEqual(result.then_node.children()[1].text, "then2")

        self.assertEqual(len(result.else_node.children()), 2)
        self.assertEqual(result.else_node.children()[0].text, "else1")
        self.assertEqual(result.else_node.children()[1].text, "else2")

    def test_parse_include(self):
        lexer_node = LexerNode("include", LexerNodeType.INCLUDE)
        lexer_node.set_children([LexerNode("file.mk", LexerNodeType.TEXT)])
        result = Parser.parse_include(lexer_node)
        self.assertEqual(str(result.file), "file.mk")

    def test_parse_export(self):
        lexer_node = LexerNode("export", LexerNodeType.EXPORT)
        lexer_node.set_children([LexerNode("variable", LexerNodeType.TEXT)])
        result = Parser.parse_export(lexer_node)
        self.assertEqual(str(result.name), "variable")

    def test_parse_define(self):
        lexer_node = LexerNode("define", LexerNodeType.DEFINE)
        lexer_node.direct_children = [LexerNode("name", LexerNodeType.TEXT)]
        lexer_node.set_children([ LexerNode("value", LexerNodeType.TEXT)])

        result = Parser.parse_define(lexer_node)
        self.assertEqual(result.name.text, "name")
        self.assertEqual(result.value.text, "value")

    def test_parse_undefine(self):
        lexer_node = LexerNode("undefine", LexerNodeType.UNDEFINE)
        lexer_node.set_children([LexerNode("name", LexerNodeType.TEXT)])
        result = Parser.parse_undefine(lexer_node)
        self.assertEqual(str(result.name), "name")

    def test_parse_text(self):
        lexer_node = LexerNode("Hello", LexerNodeType.TEXT)
        result = Parser.parse_text(lexer_node)
        self.assertEqual(str(result.text), "Hello")

    def test_parse_statement(self):
        children = []
        lexer_assign_node = LexerNode("=", LexerNodeType.ASSIGN)
        lexer_assign_node.direct_children = [LexerNode("x", LexerNodeType.TEXT)]
        lexer_assign_node.set_children([LexerNode("10", LexerNodeType.TEXT)])


        lexer_rule_node = LexerNode("rule", LexerNodeType.RULE)
        lexer_rule_node.direct_children = LexerNode("target", LexerNodeType.TEXT)


        lexer_rule2_node = LexerNode("rule", LexerNodeType.RULE)
        lexer_rule2_node.direct_children = LexerNode("target", LexerNodeType.TEXT)
        lexer_rule2_node.secondary_children = [
            LexerNode("dep1", LexerNodeType.TEXT),
            LexerNode("dep2", LexerNodeType.TEXT)
        ]
        lexer_rule2_node.set_children( [
            LexerNode("command1", LexerNodeType.TEXT),
            LexerNode("command2", LexerNodeType.TEXT)
        ])

        
        lexer_if_node = LexerNode("if", LexerNodeType.CONDITIONAL)
        lexer_if_node.direct_children = LexerNode("condition", LexerNodeType.TEXT)
        lexer_node_else = LexerNode("else", LexerNodeType.CONDITIONAL)
        lexer_node_else.set_children ( [
            LexerNode("else1", LexerNodeType.TEXT),
            LexerNode("else2", LexerNodeType.TEXT)
        ])
        lexer_if_node.set_children( [
            LexerNode("then1", LexerNodeType.TEXT),
            LexerNode("then2", LexerNodeType.TEXT),
            lexer_node_else
        ])
        Parser.parse_statement(children, [lexer_assign_node, lexer_rule_node, lexer_rule2_node, lexer_if_node])
        self.assertEqual(len(children), 4)

        self.assertEqual(children[0].name.text, "x")
        self.assertEqual(children[0].value.text, "10")
        self.assertEqual(children[1].name.text, "target")

        self.assertEqual(children[2].name.text, "target")
        self.assertEqual(len(children[2].depends), 2)
        self.assertEqual(children[2].depends[0].text, "dep1")
        self.assertEqual(str(children[2].depends[1]), "dep2")
        self.assertEqual(len(children[2].commands), 2)
        self.assertEqual(children[2].commands[0].text, "command1")
        self.assertEqual(children[2].commands[1].text, "command2")

        self.assertEqual(children[3].condition.text, "condition")

        self.assertEqual(len(children[3].then_node.children()), 2)
        self.assertEqual(children[3].then_node.children()[0].text, "then1")
        self.assertEqual(children[3].then_node.children()[1].text, "then2")

        self.assertEqual(len(children[3].else_node.children()), 2)
        self.assertEqual(children[3].else_node.children()[0].text, "else1")
        self.assertEqual(children[3].else_node.children()[1].text, "else2")


    def test_parse(self):
        
        lexer_root = LexerNode("lexer_root", LexerNodeType.ROOT)
        lexer_assign_node = LexerNode("=", LexerNodeType.ASSIGN)
        lexer_assign_node.direct_children = [LexerNode("x", LexerNodeType.TEXT)]
        lexer_assign_node.set_children([LexerNode("10", LexerNodeType.TEXT)])

        lexer_root.set_children([lexer_assign_node])

        root = Parser.parse(lexer_root)
        self.assertEqual(root.file_name, "lexer_root")
        self.assertEqual(len(root.children()), 1)
        self.assertEqual(root.children()[0].type, NodeType.ASSIGN)

if __name__ == '__main__':
    unittest.main()