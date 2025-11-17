from odoo import models, fields


class GpecProperty(models.Model):
    _name = "gpec.property"
    _description = "GPEC : Gestion prévisionnelle des emplois et compétences"
    _rec_name = "nom_salarie"

    # Identité du salarié
    nom_salarie = fields.Char(string="Nom du salarié")
    prenom_salarie = fields.Char(string="Prénom du salarié")

    # Dates
    date_entree = fields.Date(string="Date d'entrée")
    date_sortie = fields.Date(string="Date de sortie")
    date_retraite = fields.Date(string="Date de retraite")

    # Autres infos
    rappel_recrutement = fields.Char(string="Rappel de recrutement")
    description = fields.Text(string="Description")
    description_poste = fields.Text(string="Description du poste")

    type_contrat = fields.Selection(#menu déroulant
        [
            ('cdd', 'CDD'),
            ('cdi', 'CDI'),
            ('alternance', 'Alternance'),
            ('stage', 'Stage'),
        ],
        string="Type de contrat",
    )

    state = fields.Selection(
        [
            ('en_cours', 'En cours de recrutement'),
            ('employe', 'Employé'),
            ('en_retraite', 'En retraite'),
            ('licencie', 'Licencié'),
        ],
        string="Status",
        required=True,
        copy=False,
        default='en_cours',
    )

    def action_next_state(self):
        order = ['en_cours', 'employe', 'en_retraite', 'licencie']

        for rec in self:
            if rec.state in order:
                idx = order.index(rec.state)
                if idx < len(order) - 1:
                    rec.state = order[idx + 1]


competence_ids = fields.One2many(
    "gpec.competence",
    "employee_id",
    string="Compétences",
)
