from odoo import models, fields, api

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        (
            'estate_property_tag_name_unique',
            'UNIQUE(name)',
            'Tag name must be unique.'
        ),
    ]
