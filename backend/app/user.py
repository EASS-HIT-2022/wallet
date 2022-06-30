from pydantic import BaseModel, EmailStr

class User(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr

    
    def toJson(self):
        data = {
            "firstName" : self.firstName,
             "lastName" : self.lastName, 
             "email": self.email
              }
        return data