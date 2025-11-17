from odoo import models, fields

from odoo import models, fields


class GpecCompetence(models.Model):
    _name = "gpec.competence"
    _description = "Compétence du salarié"

    name = fields.Char(string="Compétence", required=True)

    niveau = fields.Selection(
        [
            ('debutant', 'Débutant'),
            ('intermediaire', 'Intermédiaire'),
            ('avance', 'Avancé'),
            ('expert', 'Expert'),
        ],
        string="Niveau",
    )

    employee_id = fields.Many2one(
        "gpec.property",
        string="Salarié",
        ondelete="cascade",
    )
