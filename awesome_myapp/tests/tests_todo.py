from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from datetime import date

class TestTodoItem(TransactionCase):
    def setUp(self):
        super().setUp()
        self.Todo = self.env["awesome.todo"]
        self.user = self.env.ref("base.user_admin")

    def test_create_valid_todo(self):
        """Créer une tâche valide"""
        todo = self.Todo.create({
            "name": "Acheter du café",
            "is_done": False,
            "priority": "1",
            "user_id": self.user.id,
            "due_date": date.today(),
        })
        self.assertTrue(todo.id)
        self.assertEqual(todo.name, "Acheter du café")

    def test_create_invalid_todo_name(self):
        """Essayer de créer une tâche avec un titre trop court"""
        with self.assertRaises(ValueError):
            self.Todo.create({
                "name": "ok",  # moins de 3 caractères
                "is_done": False,
                "priority": "1",
                "user_id": self.user.id,
            })
