import jwt
import time


SECRET = "bb557692062675bf9dc8f4711ae2a57f55dcb28d1443d0f3ee377c36be15fbdc43a7f8f5f201f9772b0022304de9fd81ad3ad011b47fa2f905ccab1fd7ff1a18"


payload = {
    "email": "thanujapriyadarshane0@gmail.com",
    "exp": time.time() + 3600 
}

token = jwt.encode(payload, SECRET, algorithm="HS256")

print("\nGenerated JWT Token:\n", token)


try:
    decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
    print("\n✅ Token is valid. Decoded payload:\n", decoded)
except jwt.ExpiredSignatureError:
    print("❌ Token expired")
except jwt.InvalidTokenError as e:
    print("❌ Invalid token:", e)
