import pytest
from hobbit import Hobbit

def test_it_has_a_name():
    hobbit = Hobbit('Bilbo')
    assert(hobbit.name) == 'Bilbo'

def test_it_can_have_another_name():
    hobbit = Hobbit('Peregrin')
    assert(hobbit.name) == 'Peregrin'

def test_it_has_an_unadventurous_disposition():
    hobbit = Hobbit('Samwise')
    assert(hobbit.disposition) == 'homebody'

def test_it_can_have_a_different_disposition():
    hobbit = Hobbit('Frodo', 'adventurous')
    assert(hobbit.disposition) == 'adventurous'

def test_it_can_grow_older_when_celebrating_birthdays():
    hobbit = Hobbit('Meriadoc')
    assert(hobbit.age) == 0

    for i in range(5):
        hobbit.celebrate_birthday()

    assert(hobbit.age) == 5

def test_it_is_considered_a_child_at_32():
    hobbit = Hobbit('Gerontius')

    for i in range(32):
        hobbit.celebrate_birthday()

    assert(hobbit.is_adult()) == False

def test_it_comes_of_age_at_33():
    hobbit = Hobbit('Gerontius')

    for i in range(32):
        hobbit.celebrate_birthday()

    assert(hobbit.is_adult()) == False

    # Check to see if Hobbit is still an adult one year later
    hobbit.celebrate_birthday()
    assert(hobbit.is_adult()) == True


# Create your own tests:

# Test that it is old at the age of 101
#     Create a Hobbit
#     Have Hobbit age 101 years
#     Check to see that hobbit.is_old() returns True
def test_its_old_at_101():
    hobbit = Hobbit('Gerontius')

    for i in range(100):
        hobbit.celebrate_birthday()

    assert(hobbit.is_old()) == False

    hobbit.celebrate_birthday()
    assert(hobbit.is_old()) == True
# Test that it has a ring if its name is Frodo
#     Create a Hobbit named Frodo
#     Create a second Hobbit named Sam
#     Check to see if has_ring() for Frodo returns True
#     Check to see if has_ring() for Sam returns True

# Test that they are short
#     Create a Hobbit
#     Check to see if is_short() returns True
