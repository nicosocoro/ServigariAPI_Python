from Utilities import DateHandler as DH

class AuditRegistry():
    def __init__(self, pUserRegistry, pDateRegistry):
        self.UserRegistry = pUserRegistry
        self.DateRegistry = pDateRegistry
