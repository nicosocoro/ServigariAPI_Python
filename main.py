from Configurations import SetUp
SetUp.Initial()

from Database.TestingQuery import Main as tq_main

# Main program
def Main():
    try:
        tq_main()
    except Exception as e:
        print(e)


Main()