if __name__=="__main__":
    year = input("Enter a year: ")
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
           if year % 400 == 0:
               print("%i is a leap year." % (year))
           else:
                print("%i Is not a leap year." % (year))
        else:
            print("%i Is not a leap year." % (year))
    else:
        print("%i Is not a leap year." % (year))

   