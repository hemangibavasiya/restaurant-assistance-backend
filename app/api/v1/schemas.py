from pydantic import BaseModel

class SuperAdminBase(BaseModel):
    email: str

class SuperAdminCreate(SuperAdminBase):
    password: str

class SuperAdminResponse(SuperAdminBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
