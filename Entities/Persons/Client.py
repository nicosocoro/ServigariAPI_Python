from Entities.Persons import Person as Pe

class Client(Pe.Person):
    def __init__(self, pID, pName, pLastname, pLocation, pAdress, pEmail, pBirthdate, pUserRegistry, pDateRegistry):
        super().__init__(pID, pName, pLastname, pLocation, pAdress, pEmail, pBirthdate, pUserRegistry, pDateRegistry)
