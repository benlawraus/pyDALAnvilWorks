"""File containing pytest tests"""
from collections import namedtuple

import anvil.users
from anvil import tables
from anvil.tables import app_tables
import tests.pydal_def as mydal
from datetime import datetime, timedelta
import pytest


def test_tables():
    tables
    assert True


def test_order_by():
    tables.order_by()
    assert True


def test_get_user():
    mydal.define_tables_of_db()
    # write a user
    user_d = dict(
        name="Rex Eagle",
        email="my_email@address.com",
        enabled=True,
        signed_up=datetime.now(),
        password_hash="adsfasdf",
        confirmed_email=True,
        email_confirmation_key="dfgrgdf",
        last_login=datetime.now())
    assert anvil.users.add_row(**user_d) is not None
    # get a user
    user = anvil.users.get_user()
    assert "Rex Eagle" == user.name


def email_records(user):
    # write two email records
    email_d = dict(
        address='firstname.lastname@email.com',
        created_by=user
    )
    row1 = app_tables.email.add_row(**email_d)
    email_d = dict(
        address='2ndemail.Eagle@email.com',
        created_by=user
    )
    row2 = app_tables.email.add_row(**email_d)
    return [row1, row2]


def phone_record(user):
    phone_d = dict(
        number="(888) 808 0808",
        created_by=user
    )
    return app_tables.phone.add_row(**phone_d)


def test_add_row():
    """Tests single_link and multi-link lists in record"""
    mydal.define_tables_of_db()
    # get user (run test_get_user at least once)
    user = anvil.users.get_user()
    assert "Rex Eagle" == user['name']
    email_list = email_records(user)
    assert all(email_list)
    phone_row = phone_record(user)
    assert phone_row
    # write a contact
    contact_d = dict(
        name="Rex Eagle's Brother",
        email_list=email_list,
        phone=phone_row,
        created_by=user,
        created_on=datetime.now()
    )
    contact_row = app_tables.contact.add_row(**contact_d)
    assert contact_row


def insert_email_record(user, email, created_on):
    db_row_id = mydal.db.email.insert(address=email, created_by=user, created_on=created_on)
    mydal.db.commit()
    return db_row_id


def insert_phone_record(user, phone, created_on):
    db_row_id = mydal.db.phone.insert(number=phone, created_by=user, created_on=created_on)
    mydal.db.commit()
    return db_row_id


def insert_contact_record(user, name, email_list, phone, created_on):
    e_list = [insert_email_record(user, e, created_on) for e in email_list]
    p = insert_phone_record(user, phone, created_on)
    contact = mydal.db.contact.insert(
        name=name,
        email_list=e_list,
        phone=p,
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
    created_on = datetime.now()+timedelta(seconds=1) # so as not to clash with previous tests
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
    date_time_expected=created_on.replace(microsecond=0)
    assert all([date_time_expected == contact['created_on'] for contact in contacts])
    assert all(['M name' == contacts[0]['name'],
                'L name' == contacts[1]['name'],
                'D name' == contacts[2]['name']])
