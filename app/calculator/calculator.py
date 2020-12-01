#!/usr/bin/python
class Calculator():

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract (x, y):
        return x - y
        
    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide (x, y):
        return x / y
    
    @staticmethod
    def calculate(operator, x, y):
        if (operator == 0):
            return Calculator.add(x,y)
        elif (operator == 1):
            return Calculator.subtract(x,y)
        elif (operator == 2):
            return Calculator.multiply(x,y)
        elif (operator == 3):
            return Calculator.divide(x,y)
