from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services import BankService

app = FastAPI()

# Model untuk request body
class TransaksiRequest(BaseModel):
    no_rek: str
    jumlah: int

# Endpoint penyetoran dana
@app.post("/setor")
def setor_dana(request: TransaksiRequest):
    try:
        result = BankService.setor_dana(request.no_rek, request.jumlah)
        return {"no_rek": request.no_rek, "nama": result["nama"], "saldo": result["saldo"]}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint penarikan dana
@app.post("/tarik")
def tarik_dana(request: TransaksiRequest):
    try:
        result = BankService.tarik_dana(request.no_rek, request.jumlah)
        return {"no_rek": request.no_rek, "nama": result["nama"], "saldo": result["saldo"]}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
