'''
Created on 15 Jul 2013

@author: Eoin Gillen
'''
class StockException(Exception):
    
    def __init__(self):
        print '**Entering __init__ StockException method**'
        pass
    
    
    def priceCheck (self, price):
        print '**Entering priceCheck StockException method**'
        '''Check that the price input is the right format.'''
        try:
            price = float(price)
            if price >= 0:
                return True
            else:
                print 'Please enter a number as price per unit. Negative numbers are not allowed.'
                return False
        except:
            print 'Input error: Please enter a number or float value for price'
            return False
            
            
    def warehouseCheck (self, warehouse):
        print '**Entering warehouseCheck StockException method**'
        '''Check that warehouse number is an integer between 1 and 4.'''
        try:
            warehouse = int(warehouse)
            if warehouse < 5 and warehouse > 0:
                return True
            else:
                print 'You must enter a number between 1 and 4, no other number will be accepted.'
                return False
        except ValueError:
            print 'Please enter a number between 1 and 4.'
            return False
            
            
    def addCheck(self, class2):
        print '**Entering addCheck StockException method**'
        '''Check that only appropriate class instances are passed to __add__ function.'''
        try:
            if class2.pricePerUnit ==  int(class2.pricePerUnit) or class2.pricePerUnit == float(class2.pricePerUnit):
                return True
            else:
                print 'Only stock class instances can be added together to find combined price of units. Please try again.'
                return False
        except:
            print 'Only stock class instances can be added together to find combined price of units. Please try again.'
            return False
    
        
    def mulCheck(self, x):
        print '**Entering mulCheck StockException method**'
        '''Check that only integers or floats are given as arguments.'''
        try:
            if x == int(x) or x ==float(x):
                return True
        except:
            print 'The class can only be multiplied by an integer or float.' 
            print 'Re-enter a number for the class to be be multiplied by.'
            return False
        
        
    def nameCheck(self, name):
        print '**Entering nameCheck StockException method**'
        '''Check that inputed names are above 1 character and
        below 100 characters long.'''
        if len(name)>100:
            print "Too many characters given"
            return False
        elif len(name)<1:
            print "Too few characters given"
            return False
        else:
            return True
    
    
    def dateCheck(self, date):
        print '**Entering dateCheck StockException method**'
        '''Check that date is entered in right format'''
        try:
            if any( [ i>'9' or i<'0' for i in date]):
                print "Error: Input may only contain numbers"
                return False
            elif len(date)>8:
                print "Too many characters given"
                return False
            elif len(date)<8:
                print "Too few characters given"
                return False
            else:
                return True
        except:
            print 'You have made an input error. Please try again.'
            return False
