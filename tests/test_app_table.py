"""File containing pytest tests"""
from collections import namedtuple

import pydal
import anvil.users
from anvil import tables
from anvil.tables import app_tables
import tests.pydal_def as mydal
from datetime import timedelta
from tests.common import *


def test_tables():
    assert tables


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
    parameters = "name,email_list, phone"
    variations = [
        ("L name", ['a@a.com', 'b@a.com'], "444 Phone"),
        ("D name", ['s@a.com', 'd@a.com'], "222 Phone"),
        ("M name", ['f@a.com', 'g@a.com'], "333 Phone"),
    ]
    mydal.define_tables_of_db()
    user = anvil.users.get_user()
    created_on = datetime.now() + timedelta(seconds=1)  # so as not to clash with previous tests
    # create records
    Parameter = namedtuple("Parameter", parameters)
    for _v in variations:
        para = Parameter(*_v)
        insert_contact_record(user, para.name, para.email_list, para.phone, created_on)
    db_rows = app_tables.contact.search(created_on=created_on)
    assert created_on.replace(microsecond=0) == db_rows[0]['created_on']

    contacts = app_tables.contact.search(
        tables.order_by('name', ascending=False), created_on=created_on)
    assert len(variations) == len(contacts)
    date_time_expected = created_on.replace(microsecond=0)
    assert all([date_time_expected == contact['created_on'] for contact in contacts])
    assert all(['M name' == contacts[0]['name'],
                'L name' == contacts[1]['name'],
                'D name' == contacts[2]['name']])


def get_user():
    user_ref = mydal.db.users.insert(**user_generator())
    mydal.db.commit()
    return user_ref  # gets last inserted user


class TestUser:
    def test_get_user(self):
        """Tests anvil.works  `anvil.users.get_user()`"""
        mydal.define_tables_of_db()
        # test anvil.users.get_by_id()
        user_ref = get_user()
        user = anvil.users.get_user()
        assert mydal.db.users(user_ref) == user

    def test_user_get_by_id(self):
        """Tests anvil.works  `anvil.users.get_by_id(id)`"""
        mydal.define_tables_of_db()
        # test anvil.users.get_by_id()
        user_ref = get_user()
        user_act = anvil.users.get_by_id(user_ref)
        user_row = mydal.db.users(user_ref)
        assert user_row == user_act


class TestID:

    def test_get_id(self):
        """Tests anvil.works `Row.get_id()` and `app_tables.table.get_by_id(id)`"""
        mydal.define_tables_of_db()
        # test app_tables.contact.get_by_id
        user = anvil.users.get_user()
        email_list = [email_generator() for _ in range(3)]
        contact_ref = insert_contact_record(user,
                                            name_generator(),
                                            email_list,
                                            phone_generator(),
                                            datetime.now().replace(microsecond=0))
        contact_row = app_tables.contact.get_by_id(contact_ref)
        contact_expected = mydal.db.contact(contact_ref)
        assert contact_expected.name == contact_row['name'] and \
               contact_expected.created_on == contact_row['created_on'] and \
               contact_expected == contact_row
        contact_id = contact_row.get_id()
        # test for Row class
        assert contact_ref == contact_id
        # test for Reference class
        assert contact_id == contact_ref['id']
        # test for referenced field
        assert isinstance(contact_ref['phone'], pydal.helpers.classes.Reference)
        assert contact_ref['phone'] == contact_ref['phone'].get_id()


class TestRow:
    def test_add_row(self):
        """Tests single_link and multi-link lists in record"""
        mydal.define_tables_of_db()
        # get user (run test_get_user at least once)
        user = get_user()
        created_on = datetime.now()
        email_list = [insert_email_record(user, email_generator(), created_on=created_on)
                      for _ in range(2)]
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
        assert contact_row
        assert email_list[0].address == contact_row['email_list'][0]['address']

    def test_delete(self):
        """Tests anvil.works `row.delete()`"""
        mydal.define_tables_of_db()
        created_on = datetime.now().replace(microsecond=0)
        user = get_user()
        # Test Reference object
        number = phone_generator()
        phone_ref = insert_phone_record(user, number, created_on)
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert 1 == len(phone_rows)
        assert phone_ref.delete() is None
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert 0 == len(phone_rows)
        # Test Row object
        number = phone_generator()
        insert_phone_record(user, number, created_on)
        # check that it is there
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert 1 == len(phone_rows)
        ph_rows=mydal.db(mydal.db.phone).select()
        nr_records_before_delete = len(ph_rows)
        # delete and check that is it missing, and only that one
        assert phone_rows[0].delete() is None
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert 0 == len(phone_rows)
        ph_rows=mydal.db(mydal.db.phone).select()
        assert nr_records_before_delete-1 == len(ph_rows)

    def test_update(self):
        """Tests `Row.update(**kwargs)`"""
        mydal.define_tables_of_db()
        created_on = datetime.now().replace(microsecond=0)
        user = get_user()
        # Test Reference object
        phone_ref = insert_phone_record(user, phone_generator(), created_on)
        number = phone_generator()
        phone_ref.update(number=number)
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert number == phone_rows[0].number
        # Test Row object
        phone_ref = insert_phone_record(user, phone_generator(), created_on)
        phone_row = mydal.db.phone(phone_ref)
        number = phone_generator()
        phone_row.update(number=number)
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert number == phone_rows[0].number


