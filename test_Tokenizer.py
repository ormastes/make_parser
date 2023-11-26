import unittest
from Common import CommonProcessor, TokenNode
from Preprocessor import Preprocess
from Types import TokenNodeType, extra_tokens, tokens
from Tokenizer import Tokenizer

class TokenizerTests(unittest.TestCase):
    def test_tokenize_nodes(self):
        node_lines = [
            ['TARGET = ', TokenNode('main.c', TokenNodeType.STRING_LITERAL)],
            ['CC = ', TokenNode('gcc', TokenNodeType.STRING_LITERAL)],
            ['CFLAGS = -Wall -Werror'],
            ['LIBS = -lm'],
            ['all: $(TARGET)', TokenNode('\t', TokenNodeType.LEAD_TAB), '$(CC) $(CFLAGS) -o $(TARGET) $(LIBS)']
        ]
        check_tokens = ['TARGET', 'CC']
        expected = [
            [TokenNode('TARGET', TokenNodeType.PARSED_TEXT), ' = ', TokenNode('main.c', TokenNodeType.STRING_LITERAL)],
            [TokenNode('CC', TokenNodeType.PARSED_TEXT),' = ', TokenNode('gcc', TokenNodeType.STRING_LITERAL)],
            ['CFLAGS = -Wall -Werror'],
            ['LIBS = -lm'],
            ['all: $(', TokenNode('TARGET', TokenNodeType.PARSED_TEXT),')', TokenNode('\t', TokenNodeType.LEAD_TAB), '$(',
             TokenNode('CC', TokenNodeType.PARSED_TEXT),') $(CFLAGS) -o $(', TokenNode('TARGET', TokenNodeType.PARSED_TEXT),') $(LIBS)']
        ]
        result = Tokenizer.tokenize_nodes(node_lines, check_tokens)
        self.assertEqual(result, expected)

    def test_remove_bare_strings(self):
        node_lines = [
            [TokenNode('TARGET', TokenNodeType.PARSED_TEXT), ' = ', TokenNode('main.c', TokenNodeType.STRING_LITERAL)],
            [TokenNode('CC', TokenNodeType.PARSED_TEXT),' = ', TokenNode('gcc', TokenNodeType.STRING_LITERAL)],
            ['CFLAGS = -Wall -Werror'],
            ['LIBS = -lm'],
            ['all: $(', TokenNode('TARGET', TokenNodeType.PARSED_TEXT),')', TokenNode('\t', TokenNodeType.LEAD_TAB), '$(',
             TokenNode('CC', TokenNodeType.PARSED_TEXT),') $(CFLAGS) -o $(', TokenNode('TARGET', TokenNodeType.PARSED_TEXT),') $(LIBS)']
        ]
        expected = [
            [TokenNode('TARGET', TokenNodeType.PARSED_TEXT), TokenNode('='), TokenNode('main.c', TokenNodeType.STRING_LITERAL)],
            [TokenNode('CC', TokenNodeType.PARSED_TEXT),TokenNode('='), TokenNode('gcc', TokenNodeType.STRING_LITERAL)],
            [TokenNode('CFLAGS = -Wall -Werror')],
            [TokenNode('LIBS = -lm')],
            [TokenNode('all: $('), TokenNode('TARGET', TokenNodeType.PARSED_TEXT),TokenNode(')'), TokenNode('\t', TokenNodeType.LEAD_TAB), TokenNode('$('),
             TokenNode('CC', TokenNodeType.PARSED_TEXT),TokenNode(') $(CFLAGS) -o $('), TokenNode('TARGET', TokenNodeType.PARSED_TEXT),TokenNode(') $(LIBS)')]
        ]
        result = Tokenizer.remvoe_bare_strings(node_lines)
        self.assertEqual(result, expected)    
    

    def test_tokenize(self):
        text = '''
# This is a Makefile
TARGET = "#main.c" # This is the target file
CC = '#gcc' # compiler,
CFLAGS = -Wall -Werror\\
LIBS = -lm

all: $(TARGET)
\t$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c $(LIBS)
'''
        expected = [
            [TokenNode('TARGET'), TokenNode('=', TokenNodeType.PARSED_TEXT), TokenNode('#main.c', TokenNodeType.STRING_LITERAL)],
            [TokenNode('CC'), TokenNode('=', TokenNodeType.PARSED_TEXT), TokenNode('#gcc', TokenNodeType.STRING_LITERAL)],
            [TokenNode('CFLAGS'), TokenNode('=', TokenNodeType.PARSED_TEXT), TokenNode('-Wall -WerrorLIBS'), TokenNode('=', TokenNodeType.PARSED_TEXT),
                TokenNode('-lm')],
            [TokenNode('all'),TokenNode(':', TokenNodeType.PARSED_TEXT), 
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('TARGET'), TokenNode(')', TokenNodeType.PARSED_TEXT),
                TokenNode('\t', TokenNodeType.LEAD_TAB), 
                #'$(CC) 
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('CC'), TokenNode(')', TokenNodeType.PARSED_TEXT),
                #$(CFLAGS) 
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('CFLAGS'), TokenNode(')', TokenNodeType.PARSED_TEXT),
                TokenNode("-o"),
                #$(TARGET) 
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('TARGET'), TokenNode(')', TokenNodeType.PARSED_TEXT),
                # $(TARGET).c 
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('TARGET'), TokenNode(')', TokenNodeType.PARSED_TEXT),TokenNode('.c'),
                #$(LIBS)
                TokenNode('$(', TokenNodeType.PARSED_TEXT), TokenNode('LIBS'), TokenNode(')', TokenNodeType.PARSED_TEXT)
             ]
        ]
        result = Tokenizer.tokenize(text)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()