from enum import Enum


# Magic variables
dummy = """
out.o: src.c src.h
  $@   # "out.o" (target)
  $<   # "src.c" (first prerequisite)
  $^   # "src.c src.h" (all prerequisites)
 
%.o: %.c
  $*   # the 'stem' with which an implicit rule matches ("foo" in "foo.c")
 
also:
  $+   # prerequisites (all, with duplication)
  $?    # prerequisites (new ones)
  $|    # prerequisites (order-only?)
 
  $(@D) # target directory
Command prefixes
-	Ignore errors
@	Don’t print command
+	Run even if Make is in ‘don’t execute’ mode

build:
    @echo "compiling"
    -gcc $< $@
"""

class TokenNodeType(Enum):
    TEXT = 0
    LEAD_TAB = 1
    STRING_LITERAL = 2
    PARSED_TEXT = 3


class LexerNodeType(Enum):
    ASSIGN = 0
    RULE = 1
    FUNCTION = 2
    CONDITIONAL = 3
    DEFINE = 4
    UNDEFINE = 5
    INCLUDE = 6
    EXPORT = 7
    PARENTHESIS = 8
    LINE = 9
    TEXT = 10
    ROOT = 11





define_tokens = [
    'define',
    'endef'
]
specifier_tokens = [
    'include',
    'export',
    'unexport',
    'override',
    'undefine',
]
assign_tokens = [
    '?=',
    '::='
    ':=',
    '+=',
    '!=',
    '='
]
rule_tokens = [
    '::',
    ':',
]
if_tokens = [
    'ifeq',
    'ifneq',
    'ifdef',
    'ifndef',
    'endif',
    'else',
]
function_tokens = [
    '$(@D)',
    '$(',
    '$@',
    '$<',
    '$^',
    '$*',
    '$+',
    '$?',
    '$|',
]
parenthese_tokens = [
    '(',
    ')',
]
comma_tokens = [',']
percent_tokens = ['%']
tokens = []
extra_tokens = [
    '\\\\',
    '\\@',
    '\\$',
    '\\:',
    '\\,',
    '\\(',
    '\\)',
    '\\#',
    '\\%',
    '\\+',
    '\\-',
    '\\.',
    '\\"',
    "\\'",
]
all_tokens = []


def init_tokens():
    if len(all_tokens) > 0:
        return
    tokens.extend(if_tokens)
    tokens.extend(define_tokens)
    tokens.extend(specifier_tokens)
    tokens.extend(assign_tokens)
    tokens.extend(rule_tokens)
    tokens.extend(function_tokens)
    tokens.extend(parenthese_tokens)
    tokens.extend(comma_tokens)

    all_tokens.extend(tokens)
    all_tokens.extend(extra_tokens)

init_tokens()