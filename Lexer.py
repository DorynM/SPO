import re


class Lexer(object):
    def __init__(self):
        self.token = {"IF": "if", "ELSE": "else", "WHILE": "while",
                      "OP": "[-+*/]", "LOGICAL_OP": r"==|>|>=|<|<=",
                      "LBreaket": "[(]", "RBreaket": "[)]", "END_COM": ";",
                      "LFBreaket": "[{]", "RFBreaket": "[}]",
                      "ASSIGN_OP": "=$", "ENDCOM": ";",
                      "NUMBER": r"0|([1-9][0-9]*)",
                      "WS": r"\s+", "STR": r"'[^']*'",
                      "VAR": "[a-zA-Z0-9_]+", "UNDEFINED": ".*"}

        self.list_tokens = []

    def __set_token(self, item):
        for key in self.token.keys():
            if re.fullmatch(self.token[key], item):
                self.list_tokens.append({key: item})
                break

    def get_term(self, file):
        with open(file) as file_handler:
            for line in file_handler:

                if "'" in line:
                    ll = line.split("'")
                    list_line = ll[0].split(' ') + ["'" + ll[1] + "'"] +\
                                [ll[2]]
                else:
                    list_line = line.split(' ')

                for item in list_line:
                    if len(item):
                        item = item.strip()
                        if '(' in item or ')' in item:
                            items = list(item)
                            for it in items:
                                self.__set_token(it)
                            continue
                        if ';' in item:
                            items = list(item)
                            for it in items:
                                self.__set_token(it)
                            continue
                        self.__set_token(item)
