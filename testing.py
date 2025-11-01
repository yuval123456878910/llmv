from tokenizer import tokenizer
from order import ordered_line
from ast_builder import AST_builder
token= tokenizer("func(1+1);",["func"])
ord_line = ordered_line(token)
print(AST_builder(ord_line).term.expr)
