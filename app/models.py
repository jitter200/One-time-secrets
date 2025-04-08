from pydantic import BaseModel
from typing import Optional

class SecretCreateRequest(BaseModel):
    secret: str
    passphrase: Optional[str] = None
    ttl_seconds: Optional[int] = None

class SecretResponse(BaseModel):
    secret_key: str

class RevealResponse(BaseModel):
    secret: str

class StatusResponse(BaseModel):
    status: str