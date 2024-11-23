from parser import *
from lexer import Lexer
from debugger import SpexDebugger
import os
import importlib

class SpexInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.register = "__EXEC_MAIN__"
        self.debugger = SpexDebugger(self)
        self.imported_modules = {}
    def interpret(self, ast):
        for node in ast:
            self.evaluate(node)

    def evaluate(self, node):
        if isinstance(node, DeclarationNode):
            value = self.evaluate(node.value)

            if node.var_type == "int" and not isinstance(value, int):
                self.debugger.ThrowError(f"Expected int, got {type(value).__name__}", 0, "Type")
            elif node.var_type == "float" and not isinstance(value, float):
                self.debugger.ThrowError(f"Expected float, got {type(value).__name__}", 0, "Type")
            elif node.var_type == "string" and not isinstance(value, str):
                self.debugger.ThrowError(f"Expected string, got {type(value).__name__}", 0, "Type")
            elif node.var_type == "bool" and not isinstance(value, bool):
                self.debugger.ThrowError(f"Expected boolean, got {type(value).__name__}", 0, "Type")
            self.variables[node.identifier] = value
        elif isinstance(node, CallNode):
            print(f"CALLED FUNCTION {node.name} with value {node.args}")
            pass
            self.evaluate_function_call(node)
        elif isinstance(node, ReturnNode):
            print(f"RETURNED VALUE {node.value}")
            pass
        elif isinstance(node, IncludeCommandNode):
            print(f"Include Path {node.path}")
            self.evaluate_includec(node)
        elif isinstance(node, FunctionNode):
            self.functions[node.name] = {}
            self.functions[node.name]["args"] = node.args
            self.functions[node.name]["body"] = node.body
            self.functions[node.name]["returnDtype"] = node.return_type
            print(f"DECLARED FUNCTION '{node.name}', args: {node.args}, returnDtype: {node.return_type}")
        elif isinstance(node, AssignNode):
            if node.identifier not in self.variables:
                self.debugger.ThrowError(f"Variable '{node.identifier}' not declared", 0, "Name")
            expected_type = type(self.variables[node.identifier])
            value = self.evaluate(node.value)
            if not isinstance(value, expected_type):
                self.debugger.ThrowError(f"Expected {expected_type.__name__}, got {type(value).__name__}", 0, "Type")
            self.variables[node.identifier] = value
        elif isinstance(node, BinOpNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            return self.apply_operator(left, right, node.operator)
        elif isinstance(node, FunctionNode):

            self.functions[node.name] = node
        elif isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, StringNode):
            return node.value
        elif isinstance(node, IdentifierNode):
            return node.value
        elif isinstance(node, IdentifierNode):
            if node.name in self.variables:
                return self.variables[node.name]
            else:
                self.debugger.ThrowError(f"Undefined variable '{node.name}'", 0, "Name")
        elif isinstance(node, ClassDefNode):
            self.evaluate_class(node)

    def apply_operator(self, left, right, operator):
        if operator.type == 'PLUS':
            return left + right
        elif operator.type == 'MINUS':
            return left - right
        elif operator.type == 'STAR':
            return left * right
        elif operator.type == 'SLASH':
            return left / right
    def evaluate_includec(self, includec_node):
        if "SpexWrapper" in includec_node.path:
            package_name = includec_node.path.split('.')[1]
            try:
                module = importlib.import_module(package_name)
                self.imported_modules[package_name] = module
                #print(f"Imported package '{package_name}'")
                return
            except ImportError:
                self.debugger.ThrowError(f"Failed to import package '{package_name}'", 0, "Import")
        spex_file = os.getcwd() + '/' + includec_node.path
        if not os.path.isfile(spex_file):
            self.debugger.ThrowError(f"Failed to import file '{spex_file}'", 0, "Import")
        with open(spex_file, 'r') as file:
            script = file.read()
            self.executeScript_Main(script=script)
    def executeScript_Main(self, script):
        lexer = Lexer(script)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        self.interpret(ast)
        #print(self.functions)
        #print(self.variables)
        #print(self.imported_modules)

    def evaluate_class(self, class_node):
        class_name = class_node.name
        class_body = class_node.body
        self.functions[class_name] = {"body": class_body}
        #print(f"Class '{class_name}' defined with body: {class_body}")

    def evaluate_function_call(self, function_call_node):
        function_name = function_call_node.name
        arguments = [self.evaluate(arg) for arg in function_call_node.args]
        #print(arguments)
        if function_name.split(".")[0] in self.imported_modules :
            module = self.imported_modules[function_name.split(".")[0]]
            func = getattr(module,function_name.split(".")[1], None)
            if func:
                if arguments == [None]:
                    return func()
                else: return func(*arguments)
            else:
                self.debugger.ThrowError(f"Function '{function_name}' not found in module.", 0, "Name")
        else:
            func = self.functions.get(function_call_node.name)
            if not func:
                self.debugger.ThrowError(f"Function {function_call_node.name} not found.", 0, "Name")

            local_env = {}
            for arg, (param_type, param_name) in zip(function_call_node.args, func['args']):
                local_env[param_name] = self.evaluate(arg)

            for stmt in func['body']:
                result = self.evaluate(stmt)
            return result

