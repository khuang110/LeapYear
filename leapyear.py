if __name__=="__main__":
    while True:
        try:
            year = input("Enter a year: ")
            year = int(year)
            break
        except ValueError:
            print("Not a valid input!")
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

   