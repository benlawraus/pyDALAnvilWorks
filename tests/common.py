import string
import random
from datetime import datetime


def random_number(size=3):
    return ''.join(random.choice(string.digits) for count in range(size))


def random_name(size=5, chars=string.ascii_lowercase):
    half_of = int(size / 2)
    first_part = ''.join(random.choice(chars) for count in range(half_of))
    last_part = ''.join(random.choice(chars) for count in range(half_of))
    first_name = first_part + random.choice('aeiou') + last_part
    return first_name.capitalize()


def name_generator():
    size1 = random.choice((3, 4, 5, 6, 7))
    size2 = random.choice((3, 4, 5, 6, 7))
    return random_name(size1) + " " + random_name(size2)


def phone_generator():
    return "(" + random_number() + ")" + random_number() + " " + random_number(4)


def email_generator():
    return random_name(8) + "@" + random_name(8) + ".com"


def location_generator():
    return random_number(5) + " " + random_name(6) + "," + random_name(7)


def user_generator():
    return dict(
        name=name_generator(),
        email=email_generator(),
        enabled=True,
        signed_up=datetime.now(),
        password_hash=random_name(32),
        confirmed_email=True,
        email_confirmation_key=random_name(32),
        last_login=datetime.now(),
        remembered_logins=random_name(16))
