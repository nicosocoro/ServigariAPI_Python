from Entities.Audit import AuditData as AD

# AD.AuditRegistry to heritage User and Data of registration
class Person(AD.AuditRegistry):
    def __init__(self, pID, pName, pLastname, pAdress, pLocation, pEmail, pBirthdate, pUserRegistry, pDateRegistry):
        super().__init__(pUserRegistry, pDateRegistry) # Audit information
        self.ID = pID
        self.Name = pName
        self.Lastname = pLastname
        self.Adress = pAdress
        self.Location = pLocation
        self.Email = pEmail
        self.Birthdate = pBirthdate