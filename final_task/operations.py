import operator

__all__ = (
    'STANDARD_OPERATORS',
    'OPERATOR_PRIORITIES',

)

STANDARD_OPERATORS = {
    "==": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le,
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "//": operator.floordiv,
    "unary-": operator.neg,
    "unary+": operator.pos,
    "^": operator.xor,
}


OPERATOR_PRIORITIES = {
    "==": 0,
    "!=": 0,
    ">": 1,
    ">=": 1,
    "<": 1,
    "<=": 1,
    "+": 2,
    "-": 2,
    "*": 3,
    "/": 3,
    "//": 3,
    "%": 3,
    "unary-": 4,
    "unary+": 4,
    "^": 5
}

REGEX_SPEC_SYMBOLS = ["*", "+", "^"]