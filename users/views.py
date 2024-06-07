from rest_framework.response import Response
from rest_framework.decorators import api_view
from .jwt_utils import encode_token, decode_token
from .models import create_user, authenticate_user, users_db

@api_view(["POST"])
def signup(request):
    try:
        email = request.data["email"]
        password = request.data["password"]
    except KeyError:
        return Response({"error": "Email and password are required"}, status=400)
    
    user = create_user(email, password)
    return Response({"id": user["id"], "email": user["email"]})

@api_view(["POST"])
def signin(request):
    try:
        email = request.data["email"]
        password = request.data["password"]
    except KeyError:
        return Response({"error": "Email and password are required"}, status=400)
    
    user = authenticate_user(email, password)
    if not user:
        return Response({"error": "Invalid credentials"}, status=400)
    
    access_token = encode_token(user["id"])
    refresh_token = encode_token(user["id"])  # For simplicity, we're using the same token for refresh_token
    return Response({"access_token": access_token, "refresh_token": refresh_token})

@api_view(["GET"])
def me(request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return Response({"error": "Authorization header is missing or malformed"}, status=401)
    
    token = auth_header.split(" ")[1]
    payload = decode_token(token)
    if not payload:
        return Response({"error": "Invalid or expired token"}, status=401)
    
    user_id = payload["user_id"]
    user = next((user for user in users_db.values() if user["id"] == user_id), None)
    if not user:
        return Response({"error": "User not found"}, status=404)
    
    return Response({"id": user["id"], "email": user["email"]})
