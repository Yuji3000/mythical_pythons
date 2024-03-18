import pytest
from ogre import Ogre
from human import Human

def test_ogre_has_a_name():
    ogre = Ogre('Brak')
    assert ogre.name == 'Brak'

def test_ogre_live_somewhere_by_default():
    ogre = Ogre('Brak')
    assert ogre.home == 'Swamp'

def test_ogre_does_not_have_to_live_in_a_swamp():
    ogre = Ogre('Brak', 'Castle')
    assert ogre.home == 'Castle'

def test_ogre_can_meet_humans():
    ogre = Ogre('Brak')
    human = Human()
    assert human.name == 'Jane'

    ogre.encounter(human)
    assert human.encounter_counter == 0

def test_humans_notice_ogre_every_third_encounter():
    ogre = Ogre('Brak')
    human = Human()

    ogre.encounter(human)
    ogre.encounter(human)
    assert human.notices_ogre() == False

    ogre.encounter(human)
    assert human.notices_ogre() == True

def test_humans_notice_ogre_on_the_sixth_encounter():
    ogre = Ogre('Brak')
    human = Human()

    for x in range(0, 6):
        ogre.encounter(human)
    assert human.notices_ogre() == True

def test_ogre_can_swing_a_club():
    ogre = Ogre('Brak')
    human = Human()
    ogre.swing_at(human)
    assert ogre.swings == 0

def test_ogre_automatically_swings_its_club_when_noticed_by_a_human():
    ogre = Ogre('Brak')
    human = Human()
    ogre.encounter(human)
    assert ogre.swings == 0

    for x in range(0, 2):
        ogre.encounter(human)
    assert human.notices_ogre() == True
    assert ogre.swings == 1

def test_ogre_manages_to_hit_human_every_second_swing():
    ogre = Ogre('Brak')
    human = Human()

    for x in range(0, 6):
        ogre.encounter(human)
    assert human.encounter_counter == 6
    assert ogre.swings == 2
    assert human.is_knocked_out() == True 

# def test_ogre_apologizes_for_violence_and_the_human_wakes_up():
#     ogre = Ogre('Brak')
#     human = Human()
#     for x in range(0, 6):
#         ogre.encounter(human)
#     assert human.is_knocked_out() == True

#     ogre.apologize(human)
#     assert human.is_knocked_out == False