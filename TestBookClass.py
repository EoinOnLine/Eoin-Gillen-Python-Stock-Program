'''
Created on 16 Jul 2013

@author: Eoin Gillen
'''
import unittest
from BookClass import Book


class TestBook(unittest.TestCase):
    
    def setUp(self):
        print '*Entering setUp method*'
        '''This will create a Book instance that can be used throughout the
        TestBook class. Please input price as 1 and the release date as
        02012012.'''
        self.Book1 = Book()
    
    def test_storageCost (self):
        print '*Entering test_storageCost method*'
        '''Please input purchase price as 1. This method will then check that storage cost
        is 5% of 1, plus an extra 1 cost for storing books.'''
        storage = self.Book1.calculateStorageCost()
        self.assertEqual(storage,1.05)

    def test_IsAPreRelease(self):
        print '*Entering test_IsAPreRelease method*'
        '''When creating an instance for this method, make the release date 02012013 and
        make the current date 01012013. The user must input these dates for the test to work
        properly.'''
        self.assertTrue(self.Book1.IsAPreRelease())
        
    def tearDown(self):
        print '*Entering tearDown method*'
        pass
    
if __name__ == '__main__':
    '''#unittest.main()'''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBook)
    unittest.TextTestRunner(verbosity=2).run(suite)