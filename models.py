from pydantic import BaseModel

class Nasabah(BaseModel):
    no_rek: str
    nama: str
    saldo: int
