import unittest
from src.validator import validate_attendee

class TestValidator(unittest.TestCase):

    def test_valid_attendee(self):
        attendee = {
            "name": "Sara Palacios",
            "email": "sara@example.com",
            "age": 25,
            "ticket_type": "vip",
            "registration_code": "EV-1023"
        }
        self.assertEqual(validate_attendee(attendee), [])

    def test_invalid_email(self):
        attendee = {
            "name": "Juan",
            "email": "juanexample.com",
            "age": 20,
            "ticket_type": "general",
            "registration_code": "EV-0001"
        }
        self.assertIn("Invalid email", validate_attendee(attendee))

    def test_underage_attendee(self):
        attendee = {
            "name": "Ana",
            "email": "ana@example.com",
            "age": 16,
            "ticket_type": "student",
            "registration_code": "EV-9876"
        }
        self.assertIn("Attendee must be 18 or older", validate_attendee(attendee))

    def test_invalid_registration_code(self):
        attendee = {
            "name": "Luis",
            "email": "luis@example.com",
            "age": 23,
            "ticket_type": "general",
            "registration_code": "EV12"
        }
        self.assertIn("Invalid registration code", validate_attendee(attendee))

    def test_registration_code_examples(self):
        valid_attendee = {
            "name": "Elena",
            "email": "elena@example.com",
            "age": 29,
            "ticket_type": "general",
            "registration_code": "EV-1234"
        }
        self.assertNotIn("Invalid registration code", validate_attendee(valid_attendee))

        invalid_attendee = {
            "name": "Marco",
            "email": "marco@example.com",
            "age": 30,
            "ticket_type": "vip",
            "registration_code": "EV-12"
        }
        self.assertIn("Invalid registration code", validate_attendee(invalid_attendee))

if __name__ == "__main__":
    unittest.main()