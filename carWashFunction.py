#FUNCTIONS & IF-ELSE STATEMENT
def wash_car(amount_paid):
    #Premium Car Wash
    if (amount_paid == 12):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    #Basic Car Wash
    if (amount_paid == 6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

wash_car(6) #Calling "Basic Car Wash" Function