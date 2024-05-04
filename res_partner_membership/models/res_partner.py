# Copyright 2020-2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    membership_id = fields.Many2one(
        comodel_name="res.partner.membership",
        copy=False,
    )
    membership_name = fields.Char(related="membership_id.name")

    @api.onchange("membership_id")
    def _onchange_membership(self):
        if self.membership_id and self.membership_id.pricelist_id:
            self.property_product_pricelist = self.membership_id.pricelist_id.id
