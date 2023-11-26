import unittest
from Common import TokenNode, TokenNodeType
from Preprocessor import Preprocess

class PreprocessTests(unittest.TestCase):
    def test_remove_comments(self):
        lines = [
            'TARGET = main.c # This is the target file',
            'CC = gcc # Compiler',
            'CFLAGS = -Wall -Werror # Compiler flags',
            'LIBS = -lm # Libraries',
            'all: $(TARGET) # Build all targets',
            '\t$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c $(LIBS) # Compile and link the target'
        ]
        expected = [
            'TARGET = main.c ',
            'CC = gcc ',
            'CFLAGS = -Wall -Werror ',
            'LIBS = -lm ',
            'all: $(TARGET) ',
            '\t$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c $(LIBS) '
        ]
        result = Preprocess.remove_comments(lines)
        self.assertEqual(result, expected)
    # remove comments if it is not in "" or '' and it is in the middle of the line
    def test_remove_comments_quates(self):
        lines = [
            'TARGET = "#main.c" # This is the target file',
            "CC = '#gcc' # compiler",
        ]
        expected = [
            'TARGET = "#main.c" ',
            "CC = '#gcc' "
        ]
        result = Preprocess.remove_comments(lines)
        self.assertEqual(result, expected)
        

    def test_process_string_literals(self):
        lines = [
            'TARGET = "main.c"',
            "CC = 'gcc'",
            'CFLAGS = -Wall -Werror',
            'LIBS = -lm',
            'all: $(TARGET)',
            '\t$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c $(LIBS)'
        ]
        expected = [
            ['TARGET = ', TokenNode('main.c', TokenNodeType.STRING_LITERAL)],
            ['CC = ', TokenNode('gcc', TokenNodeType.STRING_LITERAL)],
            ['CFLAGS = -Wall -Werror'],
            ['LIBS = -lm'],
            ['all: $(TARGET)', TokenNode('\t', TokenNodeType.LEAD_TAB), '$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c $(LIBS)']
        ]
        result = Preprocess.process_string_literals(lines)
        self.assertEqual(result, expected)

    def test_apply_linked_lines(self):
        text = '''
TARGET = main.c \\
utils.c \\
helper.c
CC = gcc
CFLAGS = -Wall -Werror \\
-O2
LIBS = -lm
'''
        expected = [
            '',
            'TARGET = main.c utils.c helper.c',
            'CC = gcc',
            'CFLAGS = -Wall -Werror -O2',
            'LIBS = -lm'
            ''
        ]
        result = Preprocess.apply_linked_lines(text)
        self.assertEqual(result, expected)


    def test_preprocess(self):
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
            ['TARGET = ', TokenNode('#main.c', TokenNodeType.STRING_LITERAL)],
            ['CC = ', TokenNode('#gcc', TokenNodeType.STRING_LITERAL)],
            ['CFLAGS = -Wall -WerrorLIBS = -lm'],
            ['all: $(TARGET)', TokenNode('\t', TokenNodeType.LEAD_TAB), '$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c $(LIBS)']
        ]

        result = Preprocess.preprocess(text)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
