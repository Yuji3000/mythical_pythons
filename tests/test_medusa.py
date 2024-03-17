import pytest
from medusa import Medusa
from person import Person

def test_medusa_has_a_name():
    medusa = Medusa('Cassiopeia')
    assert medusa.name == 'Cassiopeia'

def test_medusa_has_no_statues_when_created():
    medusa = Medusa('Cassiopeia')
    assert len(medusa.statues) == 0

def test_medusa_gains_a_statue_when_staring_at_a_person():
    medusa = Medusa('Cassiopeia')
    victim = Person('Perseus')
    assert len(medusa.statues) == 0

    medusa.stare(victim)
    assert len(medusa.statues) == 1
    assert medusa.statues[0].name == 'Perseus'

def test_medusa_turns_a_person_to_stone_when_staring_at_them():
    medusa = Medusa('Cassiopeia')
    victim = Person('Perseus')

    assert victim.is_stoned() == False
    medusa.stare(victim)
    assert victim.is_stoned() == True

def test_medusa_can_only_have_three_victims():
    medusa = Medusa('Cassiopeia')
    victim1 = Person('Perseus')
    victim2 = Person('Sally')
    victim3 = Person('Sue')
    victim4 = Person('Steve')

    medusa.stare(victim1)
    assert victim1.is_stoned() == True
    medusa.stare(victim2)
    assert victim2.is_stoned() == True
    medusa.stare(victim3)
    assert victim3.is_stoned() == True
    medusa.stare(victim4)
    assert len(medusa.statues) == 3

def test_when_fourth_victim_is_stoned_the_first_victim_is_unstoned():
    medusa = Medusa('Cassiopeia')
    victim1 = Person('Perseus')
    victim2 = Person('Sally')
    victim3 = Person('Sue')
    victim4 = Person('Steve')

    medusa.stare(victim1)
    assert victim1.is_stoned() == True
    medusa.stare(victim2)
    assert victim2.is_stoned() == True
    medusa.stare(victim3)
    assert victim3.is_stoned() == True

    medusa.stare(victim4)
    assert victim4.is_stoned() == True
    assert victim1.is_stoned() == False
