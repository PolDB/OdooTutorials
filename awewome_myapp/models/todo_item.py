from odoo import models, fields, api

class TodoItem(models.Model):
    _name = "awesome.todo"
    _description = "Tâche"

    name = fields.Char("Titre", required=True)
    is_done = fields.Boolean("Fait")
    due_date = fields.Date("Échéance")
    priority = fields.Selection(
        [("0", "Basse"), ("1", "Normal"), ("2", "Haute")],
        default="1",
        string="Priorité",
    )
    user_id = fields.Many2one("res.users", string="Assigné à", default=lambda self: self.env.user)

    @api.constrains("name")
    def _check_name(self):
        for rec in self:
            if rec.name and len(rec.name) < 3:
                raise ValueError("Le titre doit faire au moins 3 caractères.")
