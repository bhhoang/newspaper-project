import re
import bcrypt
from model.dbquery import Database

def limit_word(text:str, limit:int)->str:
    return ' '.join(text.split())[:limit]

def validate_word_limit(text:str, limit:int)->bool:
    return len(text.split()) <= limit

def validate_email(email:str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def hash_password(password:str)->str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

def check_password(password:str, hashed_password:str)->bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def compare_strings(string1:str, string2:str)->bool:
    return string1 == string2

def check_category(category:str)->bool:
    return category in ['Economy', 'Politics', 'Traffic', 'Medical', 'Sport', 'Travel', 'Entertain', 'Science & Technology']