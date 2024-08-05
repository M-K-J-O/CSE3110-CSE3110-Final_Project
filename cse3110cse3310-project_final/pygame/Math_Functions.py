"""
Title: Math functions
Author: Marco Ou
Date: May 31st 2024
"""

import numpy
import math

e = numpy.e
pi = numpy.pi
ans = 0


def sin(x):
    return numpy.sin(x)


def cos(x):
    return numpy.cos(x)


def tan(x):
    return numpy.tan(x)


def asin(x):
    return numpy.arcsin(x)


def acos(x):
    return numpy.arccos(x)


def artan(x):
    return numpy.arctan(x)


def sinh(x):
    return numpy.sinh(x)


def cosh(x):
    return numpy.cosh(x)


def tanh(x):
    return numpy.tanh(x)


def asinh(x):
    return numpy.arcsinh(x)


def acosh(x):
    return numpy.arccosh(x)


def atanh(x):
    return numpy.arctanh(x)


def sec(x):
    return 1 / numpy.cos(x)


def csc(x):
    return 1 / numpy.sin(x)


def cot(x):
    return 1 / numpy.tan(x)


def asec(x):
    return numpy.arccos(1 / x)


def acsc(x):
    return numpy.arcsin(1 / x)


def acot(x):
    return numpy.arctan(1 / x)


def sech(x):
    return 1 / numpy.cosh(x)


def csch(x):
    return 1 / numpy.sinh(x)


def coth(x):
    return numpy.cosh(x) / numpy.sinh(x)


def acoth(x):
    return 0.5 * math.log((x + 1) / (x - 1), e)


def asech(x):
    return math.log((1 / x) + ((1 / x ** 2) - 1) ** 0.5, e)


def acsch(x):
    return math.log((1 / x) + ((1 / x ** 2) + 1) ** 0.5, e)


def log(x, b=10):
    if b == 10:
        return numpy.log10(x)
    elif b == 2:
        return numpy.log2(x)
    else:
        return math.log(x, b)


def ln(x):
    return numpy.log(x)


def floor(x):
    return numpy.floor(x)


def ceiling(x):
    return numpy.ceil(x)


def root(radicand, index=2, exponent=1):
    return radicand ** (exponent / index)


def cbr(x):
    return x ** (1 / 3)
