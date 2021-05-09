import re


class Lexer(object):
    def __init__(self):
        self.token = {"IF": "^if$", "ELSE": "^else$", "WHILE": "^while$",
                      "OP": "^[-+*/]$", "LOGICAL_OP": r"^==|>|>=|<|<=$",
                      "LBreaket": "^[(]$", "RBreaket": "^[)]$",
                      "END_COM": "^;$", "LFBreaket": "^[{]$",
                      "RFBreaket": "^[}]$", "ASSIGN_OP": "^=$",
                      "ENDCOM": "^;$", "NUMBER": r"^0|([1-9][0-9]*)$",
                      "STR": r"'[^']*'", "VAR": "^[a-zA-Z0-9_]+$",
                      "UNDEFINED": r".*[^.]*"}

        self.list_tokens = []

    def __set_token(self, item):
        for key in self.token.keys():
            if re.fullmatch(self.token[key], item):
                return key

    def get_term(self, file):
        with open(file) as file_handler:
            buffer = ''
            for line in file_handler:
                for char in line:
                    if not len(buffer) and char == "'":
                        buffer += char
                        continue
                    elif len(buffer) and not buffer.count("'") == 2:
                        if buffer[0] == "'":
                            buffer += char
                            continue
                    last_token = self.__set_token(buffer)

                    buffer += char
                    token = self.__set_token(buffer)

                    if token == "UNDEFINED":
                        if len(buffer) and not last_token == "UNDEFINED":
                            self.list_tokens.append({last_token: buffer[:-1]})
                        if not (buffer[-1] == ' ' or buffer[-1] == '\n'):
                            buffer = buffer[-1]
                        else:
                            buffer = ''
