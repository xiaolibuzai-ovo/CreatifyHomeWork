import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your_secret_key'  # 替换为一个实际的密钥

def encode_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1)  # 令牌有效期1小时
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
