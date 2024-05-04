# Copyright 2020-2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    membership_name = fields.Char(
        related="partner_id.membership_id.name",
    )
