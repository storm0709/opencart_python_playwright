import random
import string

def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits) -> str:
    return ''.join(random.choice(chars) for x in range(size))