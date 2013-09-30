'''
Created on 9 Jul 2013

@author: Eoin Gillen
'''
from StockRepository import StockRepository
from StockExceptionClass import StockException
'''I make an instance of stockException class, and use it to catch errors in code.'''
ExceptionCatcher = StockException()

class StockItem(object):
    '''IDcount will start the process of assigning unique IDs to each stock item'''
    IDcount = 1
    '''Price per Unit Count will calculate the running total of the price of all stock items'''
    pricePerUnitCount = 0


    
    def __init__(self):
        
        print '**Entering StockItem __init__ method**'
        '''Give each stock item a unique ID''' 
        self.ID = StockItem.IDcount

        '''The "_" indicates to anyone reading this code that _clientName is a private
        attribute.  I call the name check function to make sure the name is not too long or short.'''
        
        self._clientName = raw_input('Please enter the name of the client: ')
        while True:
            if ExceptionCatcher.nameCheck(self._clientName) == True:
                break
            else:
                self._clientName = raw_input('Please enter the name of the client: ')
                
        '''The user is asked to put in the price of the unit. Only integers are allowed. The user 
        will be continually re-prompted for price if they don't enter an integer. If 
        it is a positive number it is recorded without an issue. If it is a negative 
        number a message comes on screen informing the user the input has not been accepted.'''
        
        self.pricePerUnit = raw_input('Please enter the price of the unit: ')
        while True:
            if ExceptionCatcher.priceCheck(self.pricePerUnit) == True:
                break
            else:
                self.pricePerUnit = raw_input('Please enter the price of the unit: ')
     
        self.pricePerUnit = float(self.pricePerUnit)       
        
        '''the price per unit is added to the running count of the price of all items'''
        StockItem.pricePerUnitCount += self.pricePerUnit
        
        '''The user is asked to enter the warehouse that the unit is to be stored in. Only integers are 
        allowed. The user will be continually re-prompted the warehouse number if they don't enter an 
        integer. They are informed that the options are 1-4. If the user enters any number that is not 
        between 1 and 4, a message comes on screen telling them that only numbers 1-4 will be accepted.'''
        
        self.warehouseNum = raw_input('Please enter the warehouse it is stored in (1-4): ')
        while True:
            if ExceptionCatcher.warehouseCheck(self.warehouseNum) == True:
                break
            else:
                self.warehouseNum = raw_input('Please enter the warehouse it is stored in (1-4): ')
            
        '''I update a dictionary of all the stock items and their storage warehouse. The Key is the ID number,
        and the value is the warehouse number. This list is used by the StockRepository Class.'''
        self.stockUpdate(self.ID, int(self.warehouseNum))
        
        '''Add 1 to ID count so it is ready for the next stock item'''
        StockItem.IDcount += 1
        
        
    def stockUpdate(self, ID = 0, warehouseNum = 0):
        print '**Entering stockUpdate method**'
        '''Function to update the stockCollection class attribute of StockRepository class.
        This code is used to make sure the same ID is never entered twice.'''
        if not ID in StockRepository.stockCollection:
            StockRepository.stockCollection.update({ID:warehouseNum})
        else:
            print 'This ID is already used for another stock item. Please enter a unique ID.'
        return StockRepository.stockCollection
    
    
    def __add__(self, x):
        print '**Entering __add__ StockItem method**'
        '''Add the price per unit of two class instances'''
        addPrice = 0
        if ExceptionCatcher.addCheck(x) == True:
            addPrice = self.pricePerUnit + x.pricePerUnit
            return addPrice 

    
    def __mul__(self, x):
        print '**Entering __mul__ StockItem method**'
        '''multiplies the price of a unit by a user defined number'''
        unitPrice = self.pricePerUnit
        if ExceptionCatcher.mulCheck(x) == True:
            multiPrice = unitPrice * float(x)
            return multiPrice


    def calculateStorageCost(self):
        print '**Entering calculateStorageCost StockItem method**'
        '''Calculates the storage cost of an item; 5% of price per unit'''
        self.storeCost = self.pricePerUnit * 0.05
        return self.storeCost

    
    def __str__(self):
        print '**Entering __str__ StockItem method**'
        '''prints out information about a stock instance'''
        return "\nThe stock item's ID is %s \nThe price per unit is %s \nIt is stored in warehouse %s \nThe storage cost is %.2f" %(self.ID, self.pricePerUnit, self.warehouseNum, self.calculateStorageCost())
