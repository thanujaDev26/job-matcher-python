import jwt
import os
from fastapi import Depends, Header, HTTPException
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = "bb557692062675bf9dc8f4711ae2a57f55dcb28d1443d0f3ee377c36be15fbdc43a7f8f5f201f9772b0022304de9fd81ad3ad011b47fa2f905ccab1fd7ff1a18"

# def verify_token(authorization: str = Header(...)):
#     print("Auth Header Received: ", authorization)
#     try:
#         scheme, token = authorization.split()
#         if scheme.lower() != "bearer":
#             raise HTTPException(status_code=401, detail="Invalid token scheme")
#         decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
#         return decoded.get("email")
#     except Exception as e:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")

def verify_token(authorization: str = Header(...)):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid token scheme")

        decoded = jwt.decode(
            token,
            JWT_SECRET,  
            algorithms=["HS256"]
        )
        print("Decoded payload:", decoded)
        return decoded.get("email")
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except jwt.InvalidTokenError as e:
        print("JWT Decode Error:", e)
        raise HTTPException(status_code=401, detail="Invalid or expired token")
