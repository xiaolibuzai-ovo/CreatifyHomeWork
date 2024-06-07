users_db = {}
user_id_counter = 1  # 用于模拟用户ID的计数器

def get_user(email):
    for user in users_db.values():
        if user["email"] == email:
            return user
    return None

def create_user(email, password):
    global user_id_counter
    user = {"id": user_id_counter, "email": email, "password": password}
    users_db[user_id_counter] = user
    user_id_counter += 1
    return user

def authenticate_user(email, password):
    user = get_user(email)
    if user and user["password"] == password:
        return user
    return None
