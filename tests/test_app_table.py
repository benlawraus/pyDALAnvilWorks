"""File containing pytest tests"""
from collections import namedtuple

import pydal.helpers.classes

import anvil.users
from anvil import tables
from anvil.tables import app_tables
import tests.pydal_def as mydal
from datetime import timedelta
from tests.common import *


def test_tables():
    tables
    assert True


def test_order_by():
    tables.order_by()
    assert True


def insert_email_record(user, email: str, created_on: datetime) -> pydal.helpers.classes.Reference:
    db_row_ref = mydal.db.email.insert(address=email, created_by=user, created_on=created_on)
    mydal.db.commit()
    return db_row_ref


def insert_phone_record(user, phone: str, created_on: datetime) -> pydal.helpers.classes.Reference:
    db_row_ref = mydal.db.phone.insert(number=phone, created_by=user, created_on=created_on)
    mydal.db.commit()
    return db_row_ref


def insert_contact_record(user, name, email_list, phone, created_on) -> pydal.helpers.classes.Reference:
    e_list = [insert_email_record(user, e, created_on) for e in email_list]
    p = insert_phone_record(user, phone, created_on)
    contact = mydal.db.contact.insert(
        name=name,
        email_list=e_list,
        phone=p,
        age=33,
        created_by=user,
        created_on=created_on
    )
    mydal.db.commit()
    return contact


def test_search():
    PARAMETERS = "name,email_list, phone"
    VARIATIONS = [
        ("L name", ['a@a.com', 'b@a.com'], "444 Phone"),
        ("D name", ['s@a.com', 'd@a.com'], "222 Phone"),
        ("M name", ['f@a.com', 'g@a.com'], "333 Phone"),
    ]
    mydal.define_tables_of_db()
    user = anvil.users.get_user()
    created_on = datetime.now() + timedelta(seconds=1)  # so as not to clash with previous tests
    # create records
    Parameter = namedtuple("Parameter", PARAMETERS)
    for _v in VARIATIONS:
        para = Parameter(*_v)
        insert_contact_record(user, para.name, para.email_list, para.phone, created_on)
    db_rows = app_tables.contact.search(created_on=created_on)
    assert created_on.replace(microsecond=0) == db_rows[0]['created_on']

    contacts = app_tables.contact.search(
        tables.order_by('name', ascending=False), created_on=created_on)
    assert len(VARIATIONS) == len(contacts)
    date_time_expected = created_on.replace(microsecond=0)
    assert all([date_time_expected == contact['created_on'] for contact in contacts])
    assert all(['M name' == contacts[0]['name'],
                'L name' == contacts[1]['name'],
                'D name' == contacts[2]['name']])


def get_user():
    user_ref = mydal.db.users.insert(**user_generator())
    mydal.db.commit()
    return user_ref  # gets last inserted user


def test_get_by_id():
    mydal.define_tables_of_db()
    # test anvil.users.get_by_id()
    user_ref = get_user()
    user_act = anvil.users.get_by_id(user_ref)
    user_row = mydal.db.users(user_ref)
    assert user_row == user_act

    # test app_tables.contact.get_by_id
    email_list = [email_generator() for count in range(3)]
    contact_ref = insert_contact_record(user_ref,
                                        name_generator(),
                                        email_list,
                                        phone_generator(),
                                        datetime.now().replace(microsecond=0))
    contact_row = app_tables.contact.get_by_id(contact_ref)
    contact_expected = mydal.db.contact(contact_ref)
    assert contact_expected.name == contact_row['name'] and \
           contact_expected.created_on == contact_row['created_on'] and \
           contact_expected == contact_row


class TestRow:
    def test_add_row(self):
        """Tests single_link and multi-link lists in record"""
        mydal.define_tables_of_db()
        # get user (run test_get_user at least once)
        user = get_user()
        created_on = datetime.now()
        email_list = [insert_email_record(user, email_generator(), created_on=created_on) \
                      for ix in range(2)]
        assert all(email_list)
        phone_row = insert_phone_record(user, phone_generator(), created_on)
        assert phone_row
        # write a contact
        contact_d = dict(
            name="Rex Eagle's Brother",
            email_list=email_list,
            phone=phone_row,
            age=55,
            created_by=user,
            created_on=created_on
        )
        contact_row = app_tables.contact.add_row(**contact_d)
        assert email_list[0].address == contact_row['email_list'][0]['address']

        assert contact_row
