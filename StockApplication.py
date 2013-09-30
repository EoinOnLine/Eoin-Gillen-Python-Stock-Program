'''
Created on 14 Jul 2013

@author: Eoin Gillen
'''
from CDclass import CD
from BookClass import Book
from StockRepository import StockRepository
import unittest

class Run(object):
    '''Class instances of CD() and Book() made.'''
    CD1 = CD()
    CD2 = CD()
    CD3 = CD()
    CD4 = CD()
    CD5 = CD()

    Book1 = Book()
    Book2 = Book()
    Book3 = Book()  
    Book4 = Book()
    Book5 = Book()
    
    '''print out class variable that will add up the price of all stock
    items created.'''
    print Book5.pricePerUnitCount
    
    '''add the price of Book5 and CD1'''
    print Book5+CD1
    
    '''Multiply price of Book5 by 7.'''
    print Book5*7
    
    '''print the cost of storing CD1'''
    print CD1.calculateStorageCost()
    
    '''Print out information about a CD'''
    CD1.__str__()
    
    '''Find CD release date'''
    print CD1.GetDateReleased()
    
    '''Is this CD a preRelease?'''
    print CD1.IsAPreRelease()
    
    '''Multiply CD by 7, and get the cost of 7 CDs with the discount
    for bulk buying applied.'''
    print CD1*(7)
    
    '''print out information about a book'''
    Book5.__str__()
    
    '''find out the release date of the book'''
    print Book5.GetDateReleased()
    
    '''Is this CD a preRelease?'''
    print CD1.IsAPreRelease()
    
    '''Calculate the storage cost for this book. Books cost 1 extra
    to store, on top of normal price'''
    print Book5.calculateStorageCost()
    
    
    '''I have Repository1 print out its stockCollection class attribute.
     The stockCollection records a dictionary of IDs and warehouse locations.'''
    Repository1 = StockRepository()
    print Repository1.stockCollection
    
    '''Make an instance of StockRepository class. Use the moveStock method
    on it to move the warehouse locations of specific IDs. The moveStock
    method can take a single ID as an input, or a list of IDs; both must 
    be entered in list format ([]). The second passing argument for moveStock 
    is the warehouse number that we wish to move the stock to. This new 
    information will be stored in the StockCollection dictionary.'''
    stockRepo1 = StockRepository()
    stockRepo1.moveStock([1,2], 2)
    stockRepo1.moveStock([3], 2)
    print stockRepo1.stockCollection
    
    '''The deleteStock method deletes sets from the stockCollection dictionary.
    It take an ID number or a list of ID numbers as an argument.'''
    stockRepo1.deleteStock([1,2])
    stockRepo1.deleteStock([3])
    print stockRepo1.stockCollection
    
    '''The enterStock method deletes sets from the stockCollection dictionary.
    It takes an ID number or a list of ID numbers as an argument.'''
    stockRepo1.enterStock()
    print stockRepo1.stockCollection

    '''the addAllStockInWarehouse method returns the quantity of stockItems
    in a particular warehouse.'''
    print stockRepo1.addAllStockInWarehouse(1)
    
run1 = Run()