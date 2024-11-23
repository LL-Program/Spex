import re


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
        self.imported_keywords = []
    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0

    def tokenize(self):
        tokens = []
        while self.position < len(self.code):
            current_char = self.code[self.position]
            if current_char.isdigit():
                tokens.append(self.tokenize_number())
            elif current_char.isalpha():
                tokens.append(self.tokenize_identifier_or_keyword())
            elif current_char == '+':
                tokens.append(Token('PLUS', current_char))
                self.position += 1
            elif current_char == '-':
                if self.position + 1 < len(self.code) and self.code[self.position + 1] == '>':
                    tokens.append(Token('ARROW', '->'))
                    self.position += 2 
                else:
                    tokens.append(Token('MINUS', current_char))
                    self.position += 1
            elif current_char == '*':
                tokens.append(Token('STAR', current_char))
                self.position += 1
            elif current_char == '/':
                if self.position + 1 < len(self.code) and self.code[self.position + 1] == '/':
                    self.skip_comment()
                else:
                    tokens.append(Token('SLASH', current_char))
                    self.position += 1
            elif current_char == '=':
                tokens.append(Token('EQUALS', current_char))
                self.position += 1
            elif current_char == '(':
                tokens.append(Token('LPAREN', current_char))
                self.position += 1
            elif current_char == ')':
                tokens.append(Token('RPAREN', current_char))
                self.position += 1
            elif current_char == ';':
                tokens.append(Token('SEMICOLON', current_char))
                self.position += 1
            elif current_char == ':':
                if self.position + 1 < len(self.code) and self.code[self.position + 1] == ':':
                   tokens.append(Token('DCOLON', '::'))
                   self.position += 2 
                else:
                    tokens.append(Token('COLON', current_char))
                    self.position += 1
            elif current_char == '"':
                tokens.append(self.tokenize_string())
            elif current_char == '{':
                tokens.append(Token('LBRACE', current_char))
                self.position += 1
            elif current_char == '}':
                tokens.append(Token('RBRACE', current_char))
                self.position += 1
            elif current_char == '>':
                tokens.append(Token('GREATER', current_char))
                self.position += 1
            elif current_char == ',':
                tokens.append(Token('COMMA', current_char))
                self.position += 1
            elif current_char == '_':
                tokens.append(Token('IDENTIFIER', '_'))
                self.position += 1
            elif current_char == ' ' or current_char == '\n':
                self.position += 1
            else:
                raise Exception(f"Unexpected character: {current_char}")

        return tokens

        return tokens


    def tokenize_number(self):
        start = self.position
        has_decimal = False

        while self.position < len(self.code) and (self.code[self.position].isdigit() or self.code[self.position] == '.'):
            if self.code[self.position] == '.':
                if has_decimal:
                    raise Exception("Unexpected second decimal point in number.")
                has_decimal = True
            self.position += 1

        number_str = self.code[start:self.position]
        if has_decimal:
            return Token('NUMBER', float(number_str))
        else:
            return Token('NUMBER', int(number_str))

    def tokenize_identifier_or_keyword(self):
        start_pos = self.position
        while (self.position < len(self.code) and
               (self.code[self.position].isalnum() or self.code[self.position] == '.')):
            self.position += 1

        identifier = self.code[start_pos:self.position]

        if identifier == "var":
            return Token("VAR", identifier)
        elif identifier == "return":
            return Token("RETURNC", identifier)
        elif identifier == "struct":
            return Token("STRUCT", identifier)
        elif identifier == "SpexSystemWrapper":
            return Token("OBJID0", identifier)
        elif identifier == "func":
            return Token("FUNC", identifier)
        elif identifier == "match":
            return Token("MATCH", identifier)
        elif identifier == "mass":
            return Token("MASS", identifier)
        elif identifier == "include":
            return Token("INCLUDEC", identifier)
        elif identifier == "int":
            return Token("TYPE_INT", identifier)
        elif identifier == "string":
            return Token("TYPE_STRING", identifier)
        elif identifier == "bool":
            return Token("TYPE_BOOL", identifier)
        else:
            return Token("IDENTIFIER", identifier)

    def tokenize_string(self):
        self.position += 1
        start = self.position
        while self.position < len(self.code) and self.code[self.position] != '"':
            self.position += 1
        string_value = self.code[start:self.position]
        self.position += 1
        return Token('STRING', string_value)
    def skip_comment(self):
        while self.position < len(self.code) and self.code[self.position] != '\n':
            self.position += 1
        self.position += 1
