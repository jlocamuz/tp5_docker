import unittest
from parameterized import parameterized
from personService import PersonService
from person import Person
from repository import Repository


class TestPersonService(unittest.TestCase):
    @parameterized.expand([
        ("Julia", "Locamuz", 20, 0),
        ("Mariano", "Saez", 25, 1),
        ("Guadalupe", "Mendez", 26, 2)
    ])
    def test_add_person(self, name, surname, age, key):
        person = Person(name, surname, age)
        service = PersonService()
        service.add_person(person)
        self.assertEqual(Repository.diccionarioPerson[key], person.__dict__)
# .__dict__ agarra objeto  y nombre de las variables tipo name
# es key y valores q le paso contenido de la key
# name : JULIA


if __name__ == "__main__":
    unittest.main()
