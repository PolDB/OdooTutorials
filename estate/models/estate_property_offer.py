from odoo import models, fields, api
from datetime import timedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    price = fields.Float(string="Price")

    status = fields.Selection(
        [
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        string="Status",
        copy=False,  
    )

    partner_id = fields.Many2one(
        'res.partner',
        string="Buyer",
        required=True,
    )

    property_id = fields.Many2one(
        'estate.property',
        string="Property",
        required=True,
    )
    validity = fields.Integer(
        string="Validity (days)",
        default=7,
    )

    date_deadline = fields.Date(
        string="Deadline",
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
        store=True,
    )

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for offer in self:
            # Fallback si create_date est vide (nouvel enregistrement non encore créé)
            create_date = offer.create_date or fields.Datetime.now()
            # On ne garde que la date
            create_date_date = fields.Date.to_date(create_date)
            offer.date_deadline = create_date_date + timedelta(days=offer.validity or 0)

    def _inverse_date_deadline(self):
        for offer in self:
            if offer.date_deadline:
                # Même fallback que dans le compute
                create_date = offer.create_date or fields.Datetime.now()
                create_date_date = fields.Date.to_date(create_date)
                delta = offer.date_deadline - create_date_date
                offer.validity = delta.days
    
    def action_accept(self):
        for offer in self:
            property = offer.property_id

            if property.state == 'sold':
                raise UserError("You cannot accept an offer on a sold property.")

            # Refuser toutes les autres offres de cette propriété
            other_offers = property.offer_ids - offer
            other_offers.write({'status': 'refused'})

            # Accepter celle-ci
            offer.status = 'accepted'

            # Mettre à jour la propriété
            property.selling_price = offer.price
            property.buyer_id = offer.partner_id
            property.state = 'offer_accepted'

    def action_refuse(self):
        for offer in self:
            if offer.status == 'accepted':
                pass
            offer.status = 'refused'

    _sql_constraints = [
        (
            'estate_property_offer_price_check',
            'CHECK(price > 0)',
            'The offer price must be strictly positive.'
        ),
    ]

