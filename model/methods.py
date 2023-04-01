import re
import bcrypt

def word_limit(text:str, limit:int)->str:
    return ' '.join(text.split())[:limit]

def validate_word_limit(text:str, limit:int)->bool:
    return len(text.split()) <= limit

def validate_email(email:str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def hash_password(password:str)->str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password:str, hashed_password:str)->bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

def compare_strings(string1:str, string2:str)->bool:
    return string1 == string2

