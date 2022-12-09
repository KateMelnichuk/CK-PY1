
import  string
import random
def get_random_password() -> str:
    str_ = string.digits + string.ascii_letters
    password = "".join(random.sample(str_,8))
    return password

print(get_random_password())
#
