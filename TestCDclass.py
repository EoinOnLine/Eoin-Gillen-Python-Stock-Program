'''
Created on 16 Jul 2013

@author: Eoin Gillen
'''
import unittest
from CDclass import CD


class TestCD(unittest.TestCase):
    
    def setUp(self):
        print '*Entering setUp method*'
        '''This will create a CD instance that can be used throughout the
        TestCD class. The user must put price as 1 and the release date as
        02012013, but otherwise they may proceed to put in any valid inputs 
        in the other fields.'''
        self.CD1 = CD()
        
    def test_mul (self):
        print '*Entering test_mul method*'
        '''Make sure that user inputs 1 as unit price for this method to
        properly be able to test __mul__ method'''
        multi = self.CD1.__mul__(10)
        self.assertAlmostEquals(multi,9)
        
    def test_IsAPreRelease(self):
        print '*Entering test_IsAPreRelease method*'
        '''When creating an instance for this method, make the release date 02012013 and
        make the current date 01012013. The user must input these dates for the test to work
        properly.'''
        preRelease = self.CD1.IsAPreRelease()
        self.assertTrue(preRelease)
        
    
if __name__ == '__main__':
    '''#unittest.main()'''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCD)
    unittest.TextTestRunner(verbosity=2).run(suite)