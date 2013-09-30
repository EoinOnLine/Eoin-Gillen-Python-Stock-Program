'''
Created on 13 Jul 2013

@author: Eoin Gillen
'''
from StockExceptionClass import StockException
from StockItemClass import StockItem
ExceptionCatcher = StockException()

class CD(StockItem):
    
    def __init__(self):
        print '\n'
        print '**Entering __init__ CD method**'
        StockItem.__init__(self)
        
        
        '''This loop will continuously re-prompt the user to enter the title if it is larger
        than 100 characters or has no characters at all. A message will also be displayed on 
        screen describing the errors.'''
        self.title = raw_input('Please enter the title of the CD: ')
        while True:
            if ExceptionCatcher.nameCheck(self.title) == True:
                break
            else:
                self.title = raw_input('Please enter the title of the CD: ')
        
        
        
        '''The user will only be allowed to enter a date in the correct integer format,
        otherwise they are caught in a loop forever being re-prompted to enter the date
        in the correct format''' 
        self.dateReleased = raw_input('Please enter the date of release in the following format DDMMYYYY: ')
        while True:
            if ExceptionCatcher.dateCheck(self.dateReleased) == True:
                break
            else:
                self.dateReleased = raw_input('Please enter the date of release in the following format DDMMYYYY: ')
            
                
        
        '''The user is asked to enter one of three genres. They must enter the genre option properly
        before they are allowed to proceed.'''
        while True:
            self.genre = raw_input('Please enter the genre. "rock", "metal", "blues" are the only allowed options: ')
            if self.genre == 'rock' or self.genre == 'metal' or self.genre == 'blues':
                break
            else:
                continue
        
        
        self.artist = raw_input('Please enter the name of the artist: ')
        while True:
            if ExceptionCatcher.nameCheck(self.artist) == True:
                break
            else:
                self.artist = raw_input('Please enter the name of the artist: ')  
        
    def __str__(self):
        print '**Entering __str__ CD method**'
        '''This method prints out all the information about the CD, including the __str__
        method from the StockItem superclass. The date is reformatted to make it more readable.'''
        
        day = str(self.dateReleased[0:2])
        month = str(self.dateReleased[2:4])
        year = str(self.dateReleased[4:8])
        print StockItem.__str__(self)
        print 'The CD title is "%s"' %(self.title)
        print 'The artist is %s' %(self.artist)
        print 'The genre is %s' %(self.genre)
        if month == '01':
            month = 'January'
        elif month == '02':
            month = 'February'
        elif month == '03':
            month = 'March'
        elif month == '04':
            month = 'April'
        elif month == '05':
            month = 'May'
        elif month == '06':
            month = 'June'
        elif month == '07':
            month = 'July'
        elif month == '08':
            month = 'August'
        elif month == '09':
            month = 'September' 
        elif month == '10':
            month = 'October'
        elif month == '11':
            month = 'November'
        elif month == '12':
            month = 'December'
        return 'The release date is %s/%s/%s' %(day, month, year)
      
        
    def GetDateReleased(self):
        print '**Entering GetDateReleased CD method**'
        '''Method to print out the date of release in an appealing fashion'''
        print '\n'
        self.dateReleased = str(self.dateReleased)
        day = str(self.dateReleased[0:2])
        month = str(self.dateReleased[2:4])
        year = str(self.dateReleased[4:8])
        if month == '01':
            month = 'January'
        elif month == '02':
            month = 'February'
        elif month == '03':
            month = 'March'
        elif month == '04':
            month = 'April'
        elif month == '05':
            month = 'May'
        elif month == '06':
            month = 'June'
        elif month == '07':
            month = 'July'
        elif month == '08':
            month = 'August'
        elif month == '09':
            month = 'September' 
        elif month == '10':
            month = 'October'
        elif month == '11':
            month = 'November'
        elif month == '12':
            month = 'December'
        return 'The release date is %s/%s/%s' %(day, month, year)
            
    
    def IsAPreRelease(self):
        print '\n'
        print '**Entering isAPreRelease CD method**'
        '''This method asks the user for today's date, which it then compares to the release date,
        if the Release date is in the future the method returns True, otherwise returns False. As
        with my other code, I have made it so that the user input must come in a very specific format.'''
        
        currentDate = raw_input("Please enter today's date in the following format DDMMYYYY: ")
        '''This code controls how the user inputs data.'''
        while True:
            if ExceptionCatcher.dateCheck(currentDate) == True:
                break
            else:
                currentDate = raw_input("Please enter today's date in the following format DDMMYYYY: ")
                
        currentDay = currentDate[0:2]
        currentMonth = currentDate[2:4]
        currentYear = currentDate[4:8]
        
        day = str(self.dateReleased[0:2])
        month = str(self.dateReleased[2:4])
        year = str(self.dateReleased[4:8])
        '''This code compares the current and release dates to find if it is a pre-release or not.'''
        if currentYear < year:
            return True
        elif currentMonth < month and currentYear == year:
            return True
        elif currentDay < day and currentMonth == month and currentYear == year:
            return True
        else:
            return False 

    def __mul__(self, x):
        print '**Entering __mul__ CD method**'
        '''Method to return the price of multiple copies of a CD with a 10% discount for bulk buying.'''
        
        price = StockItem.__mul__(self, x)
        discount = price * 0.1
        newPrice = price - discount
        return newPrice

