# estate/models/property_type.py
from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        (
            'estate_property_type_name_unique',
            'UNIQUE(name)',
            'Property type name must be unique.'
        ),
    ]


    property_ids = fields.One2many(
        comodel_name="estate.property",
        inverse_name="property_type_id",
        string="Properties",
    )