from .newspaper import Newspapers
from model.methods import check_account

np1 = Newspapers()
def get_instance() -> Newspapers:
    return np1
