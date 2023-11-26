from Common import CommonProcessor, TokenNode
from Types import TokenNodeType

# Preprocessor for Makefile
# 1. remove comments if only if it is not in "" or ''
# 2. parse string literals
# 3. apply link lines wiht '\' at the end to remvoe '\' and join lines
class Preprocess(CommonProcessor):
    """This class represents a preprocessor for a Makefile file format.

    It provides methods for removing comments, processing string literals, and applying linked lines.
    """

    def remove_comments(lines: list):
        """Remove contents after '#' if it is not in "" or ''.

        Args:
            lines (list): The list of lines to process.

        Returns:
            list: The list of lines with comments removed.
        """
        for idx, line in enumerate(lines):
            if '#' in line:
                if "'" not in line and '"' not in line:
                    lines[idx] = line[:line.find('#')]
                else:
                    to_process = line
                    lines[idx] = ""
                    context = None
                    prev_char = None
                    for char in to_process:
                        if (char == '"' or char == "'") and (prev_char != '\\'):
                            if context is None:
                                context = char
                            elif context == char:
                                context = None
                        elif (char == '#' and context is None) and (prev_char != '\\'):
                            break
                        lines[idx] +=char
                        char = prev_char

            else:
                pass
        return lines

    def process_string_literals(lines: list):
        """Parse string literals in the given lines.

        Args:
            lines (list): The list of lines to process.

        Returns:
            list: The list of lines with string literals parsed.
        """
        node_lines = []
        last_line = None
        for line in lines:
            node_line = []
            if line.startswith('\t'):
                if last_line is None:
                    raise Exception('Invalid Makefile')
                else:
                    node_lines.pop()
                    node_line = last_line
                    node_line.append(TokenNode(line[:1], TokenNodeType.LEAD_TAB))
                    line = line[1:]

            context = None
            prev_char = None
            for char in line:
                if (char == '"' or char == "'") and (prev_char != '\\'):
                    if context is None:
                        node_line.append(TokenNode('', TokenNodeType.STRING_LITERAL))
                        context = char
                    elif context == char:
                        context = None
                elif context is None:
                    CommonProcessor.append_str_end(node_line, char)
                else:
                    if prev_char == '\\':
                        node_line[-1].text[-1] = char
                    else:
                        node_line[-1].text += char
                prev_char = char
            assert context is None
            node_lines.append(node_line)
            last_line = node_line

        return node_lines

    def preprocess(text: str):
        """Preprocess the given text.

        Args:
            text (str): The text to preprocess.

        Returns:
            list: The preprocessed lines.
        """
        # apply link lines with '\' at the end
        lines = Preprocess.apply_linked_lines(text)

        lines = Preprocess.remove_comments(lines)
        lines = [line.rstrip() for line in lines]
        lines = [line for line in lines if len(line) > 0]

        node_lines = Preprocess.process_string_literals(lines)


        return node_lines

    def apply_linked_lines(text):
        """Apply linked lines to the given text.

        Args:
            text (str): The text to process.

        Returns:
            list: The list of lines with linked lines applied.
        """
        text = text.replace('\\\r\n', '').replace('\\\n', '').replace('\\\r', '')
        lines = text.splitlines()
        return lines
