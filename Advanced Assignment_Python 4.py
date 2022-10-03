#!/usr/bin/env python
# coding: utf-8
1. First of all, the concept of method overloading can be classified into two different concepts, Overloading user-defined functions. Overloading default functions.

2. Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because ‘+’ operator is overloaded by int class and str class. You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. 

3. "setslice" and "delslice" are deprecated, if you want to do the interception you need to work with python slice objects passed to "setitem" and "delitem". If you want to intecept both slices and ordinary accesses this code works perfectly in python.

4. Python provides the operator x += y to add two objects in-place by calculating the sum x + y and assigning the result to the first operands variable name x . You can set up the in-place addition behavior for your own class by overriding the magic “dunder” method __iadd__(self, other) in your class definition.

5. The purpose of operator overloading is to provide a special meaning of an operator for a user-defined data type. With the help of operator overloading, you can redefine the majority of the C++ operators. You can also use operator overloading to perform different operations using one operator.