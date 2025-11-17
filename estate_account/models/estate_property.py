# -*- coding: utf-8 -*-
from odoo import models, Command


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_set_sold(self):
        # Appel du comportement original
        res = super().action_set_sold()

        for property in self:
            if not property.buyer_id:
                continue

            # 6% du prix de vente
            commission_amount = property.selling_price * 0.06
            admin_fees = 100.0

            self.env["account.move"].create({
                "partner_id": property.buyer_id.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [
                    # Ligne 1 : commission 6%
                    Command.create({
                        "name": "6% Commission",
                        "quantity": 1,
                        "price_unit": commission_amount,
                    }),
                    # Ligne 2 : frais administratifs
                    Command.create({
                        "name": "Administrative fees",
                        "quantity": 1,
                        "price_unit": admin_fees,
                    }),
                ],
            })

        return res
