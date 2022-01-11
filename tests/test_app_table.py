"""File containing pytest tests"""
from collections import namedtuple

import anvil.users
from _anvil_designer.generate_apptable import yaml2apptable
from _anvil_designer.set_up_user import new_user_in_db
from anvil import tables
from anvil.tables import app_tables
import anvil.tables.query as q
import tests.pydal_def as mydal
from datetime import timedelta

from tests.common import *
from typing import Tuple


def test_apptables():
    yaml2apptable()
    mydal.define_tables_of_db()
    assert 0 < len(app_tables.contact.list_columns())
    assert 0 < len(app_tables.users.list_columns())
    assert 0 < len(app_tables.phone.list_columns())
    assert 0 < len(app_tables.email.list_columns())


def test_tables():
    assert tables


def test_order_by():
    tables.order_by()
    assert True


def insert_email_record(created_by, address: str, created_on: datetime, place: int) -> pydal.helpers.classes.Reference:
    db_row_ref = mydal.db.email.insert(address=address, created_by=created_by, created_on=created_on, place=place)
    mydal.db.commit()
    return db_row_ref


def insert_phone_record(created_by, number: str, created_on: datetime) -> pydal.helpers.classes.Reference:
    db_row_ref = mydal.db.phone.insert(number=number, created_by=created_by, created_on=created_on)
    mydal.db.commit()
    return db_row_ref


def insert_contact_record(**kwargs) -> pydal.helpers.classes.Reference:
    e_list = [insert_email_record(**e) for e in kwargs['email_list']]
    p = insert_phone_record(**kwargs['phone'])
    contact = mydal.db.contact.insert(
        name=kwargs['name'],
        email_list=e_list,
        phone=p,
        age=kwargs['age'],
        created_by=kwargs['created_by'],
        created_on=kwargs['created_on']
    )
    mydal.db.commit()
    return contact


class TestSearch:
    parameters = "name, age"
    variations = [
        ("L name", 33),
        ("D name", 12),
        ("X name", 54),
        ("M name", 67),
        ("Y name", 11),
        ("F name", 33),
        ("H name", 98),
        ("B name", 45),
        ("N name", 22),
        ("Z name", 23),
    ]

    def test_search(self):
        mydal.define_tables_of_db()
        user = new_user_in_db()
        anvil.users.force_login(user)
        created_on = datetime.now() # + timedelta(seconds=2)  # so as not to clash with previous tests
        # create records
        Parameter = namedtuple("Parameter", self.parameters)
        for _v in self.variations:
            para = Parameter(*_v)
            insert_contact_record(created_by=user, name=para.name,
                                  email_list=[generate_email_instance(user)],
                                  phone=generate_phone_instance(user),
                                  created_on=created_on, age=para.age)
        ######################################
        db_rows = app_tables.contact.search(q.all_of(created_by=user, created_on=created_on))
        ######################################
        for ix, contact in enumerate(db_rows):
            assert created_on.replace(microsecond=0) == db_rows[ix]['created_on']
            assert user == contact['created_by']
        ######################################
        a_contact = app_tables.contact.search(
            tables.order_by('age', ascending=False),
            q.all_of(name="B name", created_by=user, created_on=created_on))
        contacts = app_tables.contact.search(
            tables.order_by('age', ascending=False), q.all_of(created_by=user, created_on=created_on))
        ######################################
        assert 1 == len(a_contact)
        assert "B name" == a_contact[0]['name']
        assert len(self.variations) == len(contacts)
        date_time_expected = created_on.replace(microsecond=0)
        for ix, contact in enumerate(contacts):
            if ix != 0:
                assert contact['age'] <= contacts[ix - 1]['age']
            assert date_time_expected == contact['created_on']
            assert user == contact['created_by']
        anvil.users.logout()
        return user

    def test_search_operators(self):
        # generate new user
        mydal.define_tables_of_db()
        user = new_user_in_db()
        anvil.users.force_login(user)
        # generate some new records with this user
        user = TestSearch().test_search()
        #####################
        rows = app_tables.contact.search(q.all_of(created_by=user, age=q.greater_than(33)))
        #####################
        assert 0 < len(rows)
        for row in rows:
            assert 33 < row['age']
        rows = app_tables.contact.search(q.all_of(created_by=user, age=q.greater_than_or_equal_to(33)))
        assert 0 < len(rows)
        for row in rows:
            assert 33 <= row['age']
        rows = app_tables.contact.search(q.all_of(created_by=user, age=q.less_than(33)))
        assert 0 < len(rows)
        for row in rows:
            assert 33 > row['age']
        rows = app_tables.contact.search(q.all_of(created_by=user, age=q.less_than_or_equal_to(33)))
        assert 0 < len(rows)
        for row in rows:
            assert 33 >= row['age']
        rows = app_tables.contact.search(q.all_of(created_by=user, age=q.less_than_or_equal_to(33)))
        assert 0 < len(rows)
        for row in rows:
            assert 33 >= row['age']
        rows = app_tables.contact.search(q.all_of(created_by=user, age=q.not_(33)))
        assert 0 < len(rows)
        for row in rows:
            assert 33 != row['age']
        anvil.users.logout()

    def test_search_any_of(self):
        # generate new user and login
        mydal.define_tables_of_db()
        user = new_user_in_db()
        anvil.users.force_login(user)
        # generate some new records with this user
        user = TestSearch().test_search()
        rows = app_tables.contact.search(q.all_of(q.any_of(age=45, name="N name"), created_by=user))
        assert 2 == len(rows)
        for row in rows:
            assert (45 == row['age'] or "N name" == row['name']) and (user == row['created_by'])
        anvil.users.logout()


class TestUser:
    def test_get_user(self):
        """Tests anvil.works  `anvil.users.get_user()`"""
        mydal.define_tables_of_db()
        # test anvil.users.get_by_id()
        user_ref = new_user_in_db()
        anvil.users.force_login(user_ref)

        ######################################
        user = anvil.users.get_user()  # gets logged in user
        ######################################
        assert user_ref == user
        # logout user
        anvil.users.logout()
        user = anvil.users.get_user()  # gets logged in user
        ######################################
        assert None == user
        return

    def test_user_get_by_id(self):
        """Tests anvil.works  `anvil.users.get_by_id(id)`"""
        # generate new user and login
        mydal.define_tables_of_db()
        user = new_user_in_db()
        user_ref =         anvil.users.force_login(user)
        ######################################
        user_act = anvil.users.get_by_id(user_ref)
        ######################################
        user_row = mydal.db.users(user_ref)
        assert user_row == user_act
        anvil.users.logout()


class TestID:

    def test_get_id(self):
        """Tests anvil.works `Row.get_id()` and `app_tables.table.get_by_id(id)`"""
        # generate new user and login
        mydal.define_tables_of_db()
        user = new_user_in_db()
        user_ref =         anvil.users.force_login(user)


        contact_ref = insert_contact_record(**generate_contact_instance(user))
        ######################################
        contact_row = app_tables.contact.get_by_id(contact_ref)
        ######################################
        contact_expected = mydal.db.contact(contact_ref)
        assert contact_expected.name == contact_row['name'] and \
               contact_expected.created_on == contact_row['created_on'] and \
               contact_expected == contact_row
        ######################################
        contact_id = contact_row.get_id()
        ######################################
        # test for Row class
        assert contact_ref == contact_id
        # test for Reference class
        assert contact_id == contact_ref['id']
        # test for referenced field
        assert isinstance(contact_ref['phone'], pydal.helpers.classes.Reference)
        assert contact_ref['phone'] == contact_ref['phone'].get_id()
        anvil.users.logout()


def insert_get_contact_row_ref(user) -> Tuple[pydal.objects.Row, pydal.helpers.classes.Reference]:
    # insert a contact
    instance = generate_contact_instance(user)
    contact_ref = insert_contact_record(**instance)
    #################################################
    contact_row = app_tables.contact.get(name=instance['name'], age=instance['age'])
    #################################################
    return contact_row, contact_ref


class TestRow:
    def test_add_row(self):
        """Tests single_link and multi-link lists in record"""
        # generate new user and login
        mydal.define_tables_of_db()
        user = new_user_in_db()
        anvil.users.force_login(user)
        created_on = datetime.now()
        email_list = [insert_email_record(user, email_generator(), created_on=created_on, place=1)
                      for _ in range(2)]
        assert all(email_list)
        phone_row = insert_phone_record(user, phone_generator(), created_on)
        assert phone_row
        # write a contact
        contact_d = dict(
            name=name_generator(),
            email_list=email_list,
            phone=phone_row,
            age=55,
            created_by=user,
            created_on=created_on
        )
        ######################################
        contact_ref = app_tables.contact.add_row(**contact_d)
        ######################################
        assert contact_ref
        assert email_list[0].address == contact_ref['email_list'][0]['address']
        contact_d['name'] = name_generator()
        ######################################
        contact_ref2 = app_tables.contact.add_row(**contact_d)
        ######################################
        assert contact_ref2
        assert email_list[0].address == contact_ref2['email_list'][0]['address']
        contact_row = mydal.db.contact(name=contact_ref.name)
        contact_row2 = mydal.db.contact(name=contact_ref2.name)
        assert contact_row.id != contact_row2.id
        anvil.users.logout()

    def test_delete(self):
        """Tests anvil.works `row.delete()`"""
        created_on = datetime.now().replace(microsecond=0)
        # generate new user and login
        mydal.define_tables_of_db()
        user = new_user_in_db()
        anvil.users.force_login(user)
        # Test Reference object
        number = phone_generator()
        phone_ref = insert_phone_record(user, number, created_on)
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert 1 == len(phone_rows)
        ######################################
        assert phone_ref.delete() is None
        ######################################
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert 0 == len(phone_rows)
        # Test Row object
        number = phone_generator()
        insert_phone_record(user, number, created_on)
        # check that it is there
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert 1 == len(phone_rows)
        ph_rows = mydal.db(mydal.db.phone).select()
        nr_records_before_delete = len(ph_rows)
        # delete and check that is it missing, and only that one
        ######################################
        assert phone_rows[0].delete() is None
        ######################################
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert 0 == len(phone_rows)
        ph_rows = mydal.db(mydal.db.phone).select()
        assert nr_records_before_delete - 1 == len(ph_rows)
        anvil.users.logout()

    def test_update(self):
        """Tests `Row.update(**kwargs)`"""
        created_on = datetime.now().replace(microsecond=0)
        # generate new user and login
        mydal.define_tables_of_db()
        user = new_user_in_db()
        anvil.users.force_login(user)
        # Test Reference object
        phone_ref = insert_phone_record(user, phone_generator(), created_on)
        number = phone_generator()
        ######################################
        phone_ref.update(number=number)
        ######################################
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert number == phone_rows[0].number
        # Test Row object
        phone_ref = insert_phone_record(user, phone_generator(), created_on)
        phone_row = mydal.db.phone(phone_ref)
        number = phone_generator()
        ######################################
        phone_row.update(number=number)
        ######################################
        phone_rows = mydal.db(mydal.db.phone.number == number).select()
        assert number == phone_rows[0].number
        anvil.users.logout()

    def test_get(self):
        # generate new user and login
        mydal.define_tables_of_db()
        user = new_user_in_db()
        anvil.users.force_login(user)
        # insert a contact
        instance = generate_contact_instance(user)
        contact_ref = insert_contact_record(**instance)
        ######################################
        contact_row = app_tables.contact.get(name=instance['name'], age=instance['age'])
        ######################################
        assert instance['name'] == contact_row['name']
        assert contact_ref['id'] == contact_row('id')
        anvil.users.logout()

    def test_dict_row(self):
        # generate new user and login
        mydal.define_tables_of_db()
        user = new_user_in_db()
        anvil.users.force_login(user)
        contact_row, contact_ref = insert_get_contact_row_ref(user)
        assert dict(contact_row)
        assert contact_row.as_dict()
        anvil.users.logout()

class TestListColumns:
    def test_list_columns(self):
        col = app_tables.contact.list_columns()
        contact_dict = dict(
            name='string',
            phone='link_single',
            email_list='link_multiple',
            age='number',
            created_by='link_single',
            created_on='datetime',
            family='simpleObject',
            uid='number',
            father='link_single',
        )
        li_col = app_tables.contact.list_columns()
        assert len(contact_dict) == len(li_col)
        for item in li_col:
            assert item['name'] in contact_dict.keys()
            assert item['type'] in contact_dict.values()