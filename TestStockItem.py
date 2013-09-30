'''
Created on 16 Jul 2013

@author: Eoin Gillen
'''
import unittest
from StockItemClass import StockItem


class StockItemTest(unittest.TestCase):
    
    def setUp(self):
        print '*Entering setUp method*'
        '''This will create a StockItem instance that can be used throughout the
        StockItemTest class.'''
        self.Stock1 = StockItem()
        
    def test__add__(self):
        print '*Entering test__add__ method*'
        '''This will create a new StockItem instance that the user should input the purchase
        price as 1. This function will then check that __add__ method makes 1 + 1 = 2'''
        Stock2 = StockItem()
        addition = self.Stock1.__add__(Stock2)
        self.assertEqual(addition, 2)
    
    def test_storageCost (self):
        print '*Entering test_storageCost method*'
        '''Please input purchase price as 1. This method will then check that storage cost
        is 5% of 1.'''
        storage = self.Stock1.calculateStorageCost()
        self.assertEqual(storage,0.05)
    
    def test_mul (self):
        print '*Entering test_mul method*'
        '''Make sure that user inputs 1 as unit price for this method to
        properly be able to test __mul__ method'''
        multi = self.Stock1.__mul__(2.2)
        self.assertAlmostEquals(multi,2.2)
        
    def tearDown(self):
        print '*Entering tearDown method*'
        pass
    
if __name__ == '__main__':
    '''#unittest.main()'''
    suite = unittest.TestLoader().loadTestsFromTestCase(StockItemTest)
    unittest.TextTestRunner(verbosity=2).run(suite)