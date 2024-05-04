# Copyright 2020-2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import fields, models


class ResPartnerMembership(models.Model):
    _name = "res.partner.membership"
    _description = "Woo Membership"

    name = fields.Char(
        string="Odoo Membership Name",
        copy=False,
        required=True,
    )
    woo_name = fields.Char(
        string="Woo Membership Name",
        copy=False,
        required=True,
    )
    pricelist_id = fields.Many2one("product.pricelist", "Pricelist")

    _sql_constraints = [
        (
            "woo_membership_name_uniq",
            "unique(woo_name)",
            "Woo Membership name must be unique!",
        ),
    ]
