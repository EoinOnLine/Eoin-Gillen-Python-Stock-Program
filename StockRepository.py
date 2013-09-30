'''
Created on 14 Jul 2013

@author: Eoin Gillen
'''
from StockExceptionClass import StockException
ExceptionCatcher = StockException()

class StockRepository(object):
    '''Dictionary created which I will use to store stock items and warehouse
    locations. It is updated by the updateStock function in the StockItem class
    and by the delete, move and enter function in the StockRepository class.'''
    stockCollection = {}
    
    '''I made the __init__ function a pass because I did not want to have to add
    a new stock item to my stock dictionary every time I needed to access the inventory.
    This allows me to create StockRepository Instances to move, delete or add all stock
    without needing to create a new stock item each time.'''
    def __init__(self):
        print '\n'
        print '**Entering __init__ StockRepository method**'
        pass
    
    
    def enterStock(self):
        print '**Entering enterStock StockRepository method**'
        '''Function to enter a new stockItem to the class attribute stockCollection dictionary.
        This code is used to make sure the same ID is never entered twice. Also allows for 
        warehouse number to be stored too.'''
        ID = int(raw_input('Please enter the ID number of the new stock item: '))
        warehouseNum = raw_input('Please enter the warehouse number that the new stock is stored in (1-4): ')
        while True:
            if ExceptionCatcher.warehouseCheck(warehouseNum) == True:
                break
            else:
                warehouseNum = raw_input('Please enter the warehouse it is stored in (1-4): ')
                    
        if not ID in StockRepository.stockCollection:
            StockRepository.stockCollection.update({ID:int(warehouseNum)})
        else:
            print 'This ID is already used for another stock item. Please enter a unique ID.'
        return StockRepository.stockCollection
    
    
    def moveStock(self, ID = 0, newWarehouseNum = 0):
        print '**Entering moveStock StockRepository method**'
        '''This function will take the ID value of stock and change the warehouse
        location number to the newWarehouseNum. The ID number must be entered as a list
        format ([]), even if only a single StockItem is to be moved.'''
        
        for i in ID:
            if i in StockRepository.stockCollection:
                StockRepository.stockCollection[i] = newWarehouseNum
                
        
    def deleteStock(self, ID = 0,):
        print '**Entering deleteStock StockRepository method**'
        '''This function will take the ID value of stock and delete the dictionary set associated
        with it. Single or multiple IDs may be used but must all be in list format.'''
        for i in ID:
            if i in StockRepository.stockCollection:
                del StockRepository.stockCollection[i]
        
        
    def addAllStockInWarehouse(self, warehouseNum):
        print '**Entering addAllStockInWarehouse StockRepository method**'
        '''Function to count all the stock items in a particular warehouse
        and return the total number.'''
        warehouseCount = 0
        for key, value in StockRepository.stockCollection.iteritems():
            if value == warehouseNum:
                warehouseCount += 1
        return warehouseCount
