#!/usr/bin/env python

import solution
from solution import *
import doctest
import codewars_test as test

doctest.testmod(solution,globs=globals())

class Foo(object, metaclass = Meta):
    def __init__(self, x):
        self.x = x

    def bar(self, v):
        return (self.x, v)

a = Foo(1)
a.bar(2)

calls = Debugger.method_calls

test.assert_equals(len(calls), 2)

test.describe("Test collected method calls")

test.it("Call to init should be collected")
test.assert_equals(calls[0]['args'], (a, 1))

test.it("Call to bar should be collected")
test.assert_equals(calls[1]['args'], (a, 2))

test.describe("Test collected attribute accesses")
accesses = Debugger.attribute_accesses
print(Debugger.method_calls)

test.assert_equals(len(accesses), 3)

test.it("Attribute set in init should be collected")
test.assert_equals(accesses[0]['action'], 'set')
test.assert_equals(accesses[0]['attribute'], 'x')
test.assert_equals(accesses[0]['value'], 1)

test.it("Method get should be collected too")
test.assert_equals(accesses[1]['action'], 'get')
test.assert_equals(accesses[1]['attribute'], 'bar')

test.it("Attribute get should be collected")
test.assert_equals(accesses[2]['action'], 'get')
test.assert_equals(accesses[2]['attribute'], 'x')