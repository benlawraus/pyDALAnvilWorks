import string
import random
from datetime import datetime
from typing import Dict
import pydal


def random_number(size=3):
    return ''.join(random.choice(string.digits) for count in range(size))


def random_name(size=5, chars=string.ascii_lowercase):
    half_of = int(size / 2)
    first_part = ''.join(random.choice(chars) for count in range(half_of))
    last_part = ''.join(random.choice(chars) for count in range(half_of))
    first_name = first_part + random.choice('aeiou') + last_part
    return first_name.capitalize()


def name_generator() -> str:
    """Returns a random string in the form of 'first_name space last_name'."""
    size1 = random.choice((3, 4, 5, 6, 7))
    size2 = random.choice((3, 4, 5, 6, 7))
    return random_name(size1) + " " + random_name(size2)


def phone_generator() -> str:
    """Returns a random 10 digit number as a string."""
    return "(" + random_number() + ")" + random_number() + " " + random_number(4)


def email_generator() -> str:
    """Returns a string of characters in the form of 'str@str.com'"""
    return random_name(8) + "@" + random_name(8) + ".com"


def location_generator() -> str:
    """Returns a string of characters in the form of '5-digits space name, name"""
    return random_number(5) + " " + random_name(6) + "," + random_name(7)


def user_generator() -> Dict:
    """Returns a dict of user attributes.

    `last_login` and `signed_up` are the same time."""
    time_now = datetime.now()
    return dict(
        name=name_generator(),
        email=email_generator(),
        enabled=True,
        signed_up=time_now,
        password_hash=random_name(32),
        confirmed_email=True,
        email_confirmation_key=random_name(32),
        last_login=time_now,
        remembered_logins=random_name(16))


def generate_phone_instance(user):
    return dict(
        number=phone_generator(),
        created_by=user,
        created_on=datetime.now()
    )


def generate_email_instance(user):
    return dict(
        address=email_generator(),
        place=1,
        created_by=user,
        created_on=datetime.now()
    )


def generate_contact_instance(user: pydal.objects.Row) -> Dict:
    """Returns a dict, using the input strings. One element in the lists.
    """
    ph = generate_phone_instance(user)
    em = [generate_email_instance(user) for _ in range(3)]
    return dict(
        name=name_generator(),
        phone=ph,
        email_list=em,
        age=random.choice(range(72)),
        created_by=user,
        created_on=datetime.now())
