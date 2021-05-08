'''
CSC101 - Lab 7
Part 3: Days in the month with Boolean expressions
Tyler Smith
10/7/2020
'''



def main():
   
   month = int(input("Enter a month value (1 for Jan, 2 for Feb, etc.): "))
   
   if (month == 4 or month == 6 or month == 9 or month == 11):
      print ("days = 30")
      
   elif (month == 2):
      print ("days = 29")
      
   elif (month < 1):
      print ("days = -1")
      
   elif (month > 12):
      print ("days = -1")   
   
   else:
      print ("days = 31")
  
   
main()
