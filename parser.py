# AST Nodes
class ASTNode:
    pass

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

class IdentifierNode(ASTNode):
    def __init__(self, name):
        self.name = name

class BinOpNode(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right



class AssignNode(ASTNode):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value
    def __repr__(self):
        return f"AssignNode(identifier : '{self.identifier}', VALUE: {self.value})"
class IfKeywordNode(ASTNode):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value
    def __repr__(self) -> str:
        return f"IFKeywordNone(identifier = {self.identifier}, self.value = {self.value})"
class FuncDefNode(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body
class StructDefNode(ASTNode):
    def __init__(self, name, body):
        self.name = name
        self.body = body
class CallNode(ASTNode):
    def __init__(self, function, arguments):
        self.function = function
        self.arguments = arguments
class TypeNode(ASTNode):
    def __init__(self, name):
        self.name = name
class StringNode(ASTNode):
    def __init__(self, value):
        self.value = value
class BooleanNode(ASTNode):
    def __init__(self, value):
        self.value = int(value)
class DeclarationNode(ASTNode):
    def __init__(self, identifier, type_node, value):
        self.identifier = identifier
        self.var_type = type_node
        self.value = value
class FunctionNode(ASTNode):
    def __init__(self, name, args, return_type, body):
        self.name = name
        self.args = args
        self.return_type = return_type
        self.body = body
class ReturnNode(ASTNode):
    def __init__(self, value):
        self.value = value
class IncludeCommandNode:
    def __init__(self, identifier):
        self.path = identifier
class CallNode:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return f"CallNode(name={self.name}, args={self.args})"

class ClassDefNode(ASTNode):
    def __init__(self, name, body):
        self.name = name
        self.body = body

# Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.built_in_functions = {'printc'}
    def parse(self):
        statements = []
        while self.position < len(self.tokens):
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return statements

    def parse_statement(self):
        token = self.tokens[self.position]
        if token.type == 'VAR':
            stmt = self.parse_declaration()
        elif token.type == "STRUCT":
            stmt = self.parse_struct()
        elif token.type == "FUNC":
            stmt = self.parse_function_declaration()
        elif token.type == "RETURNC":
            stmt = self.parse_returnc()
        elif token.type == "INCLUDEC":
            stmt = self.parse_include_command()
        elif token.type == 'IDENTIFIER' and self.peek(1) and self.peek(1).type == 'EQUALS':
            stmt = self.parse_assignment()
        elif token.type == 'IDENTIFIER' and self.peek(1) and self.peek(1).type == 'LPAREN':
            stmt = self.parse_function_call(token.value)
        elif token.type == "MASS":
            stmt = self.parse_class()
        else:
            stmt = self.parse_expression()
        if self.peek() and self.peek().type == 'SEMICOLON':
            self.position += 1

        return stmt

    def parse_declaration(self):
        # let <identifier> : <type> = <expression>;
        self.position += 1
        identifier = self.tokens[self.position]
        self.position += 1  # Skip identifier
        self.position += 1  # Skip ':'
        type_token = self.tokens[self.position]
        self.position += 1  # Skip type
        self.position += 1  # Skip '='
        expr = self.parse_expression()
        self.position += 1  # Skip ';'
        
        return DeclarationNode(identifier.value, type_token.value, expr)
    def parse_struct(self):
        #print(f"Parsing struct declaration at position: {self.position}")
        self.position += 1

        if self.tokens[self.position].type != 'IDENTIFIER':
            raise Exception("Expected struct name (identifier)")
        func_name = self.tokens[self.position].value
        self.position += 1
        #POINTER DCOLON Struct1::StructParent
        # if self.tokens[self.position].type == 'DCOLON':
        #     raise Exception("Expected '(' after function name")
        # self.position += 1 

        if self.position >= len(self.tokens) or self.tokens[self.position].type != 'LBRACE':
            raise Exception("Expected '{' for function body")
        self.position += 1

        body = []
        while self.position < len(self.tokens) and self.tokens[self.position].type != 'RBRACE':
            stmt = self.parse_statement()
            body.append(stmt)
        if self.position >= len(self.tokens) or self.tokens[self.position].type != 'RBRACE':
            raise Exception("Expected '}' to close function body")
        self.position += 1
        #print(f"Parsed Struct '{func_name}', Body: {body}")
        return StructDefNode(func_name,body)
    def parse_function_declaration(self):
        #print(f"Parsing function declaration at position: {self.position}")
        self.position += 1

        if self.tokens[self.position].type != 'IDENTIFIER':
            raise Exception("Expected function name (identifier)")
        func_name = self.tokens[self.position].value
        self.position += 1

        if self.tokens[self.position].type != 'LPAREN':
            raise Exception("Expected '(' after function name")
        self.position += 1 

        args = []
        while self.position < len(self.tokens) and self.tokens[self.position].type != 'RPAREN':
            if self.tokens[self.position].type != 'IDENTIFIER':
                raise Exception("Expected parameter name in function parameter")
            arg_name = self.tokens[self.position].value
            self.position += 1

            if self.position < len(self.tokens) and self.tokens[self.position].type == 'COLON':
                self.position += 1
            else:
                raise Exception("Expected ':' after parameter name")

            
            if self.position < len(self.tokens) and self.tokens[self.position].type.startswith("TYPE"):
                arg_type = self.tokens[self.position].value
                self.position += 1
            else:
                raise Exception("Expected type in function parameter")

            args.append((arg_name, arg_type))

           
            if self.position < len(self.tokens) and self.tokens[self.position].type == 'COMMA':
                self.position += 1
        if self.position >= len(self.tokens) or self.tokens[self.position].type != 'RPAREN':
            raise Exception("Expected ')' after function parameters")
        self.position += 1

        if self.position >= len(self.tokens) or self.tokens[self.position].type != 'ARROW':
            raise Exception("Expected '->' after function parameters")
        self.position += 1

        if self.position >= len(self.tokens) or not self.tokens[self.position].type.startswith("TYPE"):
            raise Exception("Expected return type after '->'")
        return_type = self.tokens[self.position].value
        self.position += 1

        if self.position >= len(self.tokens) or self.tokens[self.position].type != 'LBRACE':
            raise Exception("Expected '{' for function body")
        self.position += 1

        body = []
        while self.position < len(self.tokens) and self.tokens[self.position].type != 'RBRACE':
            stmt = self.parse_statement()  # Parse statements in the body of the function
            body.append(stmt)
        if self.position >= len(self.tokens) or self.tokens[self.position].type != 'RBRACE':
            raise Exception("Expected '}' to close function body")
        self.position += 1

        #print(f"Function parsed: {func_name} with args {args} and return type {return_type}")
        return FunctionNode(func_name, args, return_type, body)

    def parse_assignment(self):
        var_token = self.tokens[self.position]
        self.position += 2
        expr = self.parse_expression()
        self.position += 1
        return AssignNode(var_token.value, expr)
    def parse_returnc(self):
        self.position += 1
        return_value = self.tokens[self.position]
        self.position += 1
        return ReturnNode(return_value)
    def parse_expression(self):
        left = self.parse_term()
        while self.peek() and self.peek().type in ['PLUS', 'MINUS']:
            op = self.tokens[self.position]
            self.position += 1
            right = self.parse_term()
            left = BinOpNode(left, op, right)

        if self.peek() and self.peek().type == 'COMMA':
            self.position += 1

        return left


    def parse_term(self):
        left = self.parse_factor()
        while self.peek() and self.peek().type in ['STAR', 'SLASH']:
            operator = self.tokens[self.position]
            self.position += 1
            right = self.parse_factor()
            left = BinOpNode(left, operator, right)
        return left

    def parse_factor(self):
        token = self.peek()
        
        if token.type == 'NUMBER':
            self.position += 1
            return NumberNode(token.value)
        elif token.type == 'STRING':
            self.position += 1
            return StringNode(token.value)
        elif token.type == 'IDENTIFIER':
            self.position += 1
            if self.position < len(self.tokens) and self.tokens[self.position].type == 'LPAREN':
                return self.parse_function_call(token.value)
            return IdentifierNode(token.value)
        elif token.type == 'LPAREN':
            self.position += 1
            expr = self.parse_expression()
            if self.position < len(self.tokens) and self.tokens[self.position].type == 'RPAREN':
                self.position += 1
                return expr
            else:
                raise Exception("Expected ')' after expression")
        else:
            raise Exception(f"Unexpected token: {token}")


    def parse_function_call(self, func_name):
        args = []

        while self.position < len(self.tokens) and self.tokens[self.position].type != 'RPAREN':
            # Handle arguments (identifiers, numbers, etc.)
            if self.tokens[self.position].type in ['IDENTIFIER', 'NUMBER', 'STRING']:
                args.append(self.tokens[self.position].value)
                self.position += 1
            elif self.tokens[self.position].type == 'COMMA':
                # Skip commas
                self.position += 1
            elif self.tokens[self.position].type == 'LPAREN':
                # Skip commas
                self.position += 1
            else:
                raise Exception(f"Unexpected token '{self.tokens[self.position].type}' in function parameters")

        if self.position >= len(self.tokens) or self.tokens[self.position].type != 'RPAREN':
            raise Exception("Expected ')' after function parameters")
        
        self.position += 1
        return CallNode(func_name, args)



    def parse_include_command(self):
        self.position += 1
        path = None
        if self.tokens[self.position].type == 'STRING':
            path = self.tokens[self.position].value
        else:
            path = None
        self.position += 1

        return IncludeCommandNode(path)
    def parse_class(self):
        self.position += 1
        class_name = self.tokens[self.position].value
        self.position += 1
        
        if self.tokens[self.position].type != 'LBRACE':
            raise Exception("Expected '{' for class body")
        self.position += 1

        body = []
        while self.position < len(self.tokens) and self.tokens[self.position].type != 'RBRACE':
            stmt = self.parse_statement()
            body.append(stmt)
        if self.position >= len(self.tokens) or self.tokens[self.position].type != 'RBRACE':
            raise Exception("Expected '}' to close class body")
        self.position += 1

        return ClassDefNode(class_name, body)
    def peek(self, offset=0):
        if self.position + offset < len(self.tokens):
            return self.tokens[self.position + offset]
        return None