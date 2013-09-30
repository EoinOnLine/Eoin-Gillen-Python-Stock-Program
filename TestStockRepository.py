'''
Created on 16 Jul 2013

@author: Eoin Gillen
'''
import unittest
from StockRepository import StockRepository


class TestStockRepository(unittest.TestCase):
    
    def setUp(self):
        print '*Entering setUp method*'
        '''This will create a StockItem instance that can be used throughout the
        StockItemTest class.'''
        self.StockRepo1 = StockRepository()
        
        
    def test1_enterStock(self):
        print '*Entering test_enterStock method*'
        '''Please enter the new stock item's ID as 1, and the warehouse number as 1.
        For the test to run correctly these values must be inputed by the user.'''
        newEntry = self.StockRepo1.enterStock()
        self.assertEqual(newEntry, {1: 1})
       
            
    def test2_moveStock(self):
        print '*Entering test_moveStock method*'
        '''Previously entered stockItem ID;1, will be changed from warehouse 1 to
        warehouse 2.'''
        self.StockRepo1.moveStock([1], 2)
        self.assertEqual(self.StockRepo1.stockCollection, {1: 2})
        
        
    def test3_addAllStockInWarehouse(self):
        print '*Entering test_addAllStockInWarehouse method*'
        '''This code will add all the stock in warehouse 2. The answer should
        be 1.'''
        self.assertEqual(self.StockRepo1.addAllStockInWarehouse(2), 1)
        
    def test4_deleteStock(self):
        print '*Entering test_deleteStock method*'
        '''Previously entered stockItem ID;1, will be deleted.'''
        self.StockRepo1.deleteStock([1])
        self.assertEqual(self.StockRepo1.stockCollection, {})
                
                
    def tearDown(self):
        print '*Entering tearDown method*'
        pass
    
if __name__ == '__main__':
    '''#unittest.main()'''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStockRepository)
    unittest.TextTestRunner(verbosity=2).run(suite)