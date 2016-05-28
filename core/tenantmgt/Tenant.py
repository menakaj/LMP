"""
Tenant is an isolated entity in the same server instance.
Has separate db ids..

"""


class Tenant:
    def __init__(self, id="", name=""):
        self.name = name
        self.id = id
