from Common import CommonProcessor, TokenNode
from Preprocessor import Preprocess
from Types import TokenNodeType, extra_tokens, tokens

# Tokenizer for Makefile 
class Tokenizer(CommonProcessor):
    def tokenize_nodes(node_lines: list, check_tokens: list):
        """
        Tokenizes the given node lines based on the check tokens.

        Args:
            node_lines (list): List of node lines to be tokenized.
            check_tokens (list): List of tokens to check for matching.

        Returns:
            list: Tokenized node lines.
        """
        new_node_lines = []
        for node_line in node_lines:
            new_node_line = []
            for node in node_line:
                if not isinstance(node, str):
                    new_node_line.append(node)
                    idx += 1
                    continue
                idx = 0
                while idx < len(node):
                    cur = node[idx:]
                    token_found = None
                    for token in check_tokens:
                        # check currrent with token
                        if cur.startswith(token):
                            token_found = token
                            break
                    if token_found is None:
                        idx += 1
                        CommonProcessor.append_str_end(new_node_line, node[idx-1])
                        
                    else:
                        idx += len(token_found)
                        new_node_line.append(TokenNode(token_found, TokenNodeType.PARSED_TEXT))

            new_node_lines.append(new_node_line)
        return new_node_lines
    
    def remvoe_bare_strings(node_lines: list):
        # loop by idx
        line_idx = 0
        while line_idx < len(node_lines):
            node_idx = 0
            new_line = []
            while node_idx < len(node_lines[line_idx]):
                node = node_lines[line_idx][node_idx]
                if isinstance(node, str):
                    if len(node.strip())>0:
                        new_line.append(TokenNode(node.strip(), TokenNodeType.TEXT))
                else:
                    new_line.append(node)
                node_idx += 1
            node_lines[line_idx] = new_line
            line_idx += 1
        return node_lines
                    

    def tokenize(text: str):
        """
        Tokenizes the given text.

        Args:
            text (str): Text to be tokenized.

        Returns:
            list: Tokenized node lines.
        """
        node_lines = Preprocess.preprocess(text)

        node_lines = Tokenizer.tokenize_nodes(node_lines, extra_tokens)

        node_lines = Tokenizer.tokenize_nodes(node_lines, tokens)

        node_lines = Tokenizer.remvoe_bare_strings(node_lines)

        return node_lines