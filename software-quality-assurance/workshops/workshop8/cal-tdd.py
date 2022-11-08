import unittest
import calculator

class TestCalc(unittest.TestCase):
    def testSubtract(self):
        self.assertEqual(2, calculator.subtract(4, 2), "Subtraction operation for 4-2 is = 2")
    
    def testAdd(self):
        self.assertEqual(6, calculator.add(4, 2), "Addition operation for 4+2 is = 6")
    
    def testMultiply(self):
        self.assertEqual(8, calculator.multiply(4, 2), "Multiplication operation for 4*2 is = 8")

    def testMultiplyByZero(self):
        self.assertEqual(0, calculator.multiply(4, 0), "Multiplication operation for 4*0 is = 0")

    def testDivide(self):
        self.assertEqual(2, calculator.divide(4, 2), "Division operation for 4/2 is = 2")

    def testDivideByZero(self): #test fail on purpose to showcase exception handling
        self.assertEqual(0, calculator.divide(4, 0), "Division operation for 4/0 is = 0")

if __name__ == '__main__': 
    unittest.main() 