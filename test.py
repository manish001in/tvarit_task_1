import unittest 
from app import number_sum

class TestMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
    # Returns true for normal input of non teen numbers. 
    def test_accrate_numbers(self): 
        self.assertEqual( number_sum(['1','2','3']), 6) 

    # Returns true for non numeric numbers. 
    def test_non_numeric(self):         
        self.assertEqual( number_sum(['1','2','3a']), "All inputs must be numeric") 

    # Returns true for not exactly 3 numbers provided as input. 
    def test_non_3_number(self):         
        self.assertEqual( number_sum(['1','2']), "Exactly 3 numbers are required") 
   
    # Returns true for non 15,16 teen number where teen number is considered 0. 
    def test_teen_non_15_16_numbers(self): 
        self.assertEqual( number_sum(['1','2','13']), 3) 

    # Returns true for 15,16 teen number where the number is considered as its actual value. 
    def test_teen_15_16_numbers(self): 
        self.assertEqual( number_sum(['1','2','15']), 18) 
  
if __name__ == '__main__': 
    unittest.main() 

