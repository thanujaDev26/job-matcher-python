import jwt

go_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRoYW51amFwcml5YWRhcnNoYW5lMEBnbWFpbC5jb20iLCJleHAiOjE3NDg3NTc1NTl9.z4AixArkrWKVbEwru59CrvSshlGLZVJh65mb4QwmkP0"
SECRET = "bb557692062675bf9dc8f4711ae2a57f55dcb28d1443d0f3ee377c36be15fbdc43a7f8f5f201f9772b0022304de9fd81ad3ad011b47fa2f905ccab1fd7ff1a18"

try:
    decoded = jwt.decode(go_token, SECRET, algorithms=["HS256"])
    print("✅ Go token valid. Payload:", decoded)
except jwt.InvalidTokenError as e:
    print("❌ Failed to decode Go token:", str(e))
