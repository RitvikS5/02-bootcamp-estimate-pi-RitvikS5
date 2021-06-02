import math
import unittest
import random

def wallis(i):
    sum=1   
    for x in range(1,i):
        sum=sum*(4*(x**2))/(4*(x**2)-1) 
    return 2*sum
    
def monte_carlo(i):
    circle_ar=0
    total_ar=0
    prob=0
    for j in range(0,i):
        x=random.random()
        y=random.random()  
        dist=(x**2+y**2)**0.5
        if dist<=1:
            circle_ar+=1
            total_ar+=1
            prob=4*circle_ar/total_ar
        else:
            total_ar+=1
            prob=4*circle_ar/total_ar
    return prob
         
    
class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
