# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    # _description = 'Ringover dialer settings'

    ringover_dialer_tray_icon = fields.Boolean(
        string='Tray icon',
        default=False,
        config_parameter='ringover_dialer.ringover_dialer_tray_icon'
    )

    ringover_dialer_size = fields.Selection(
        [
            ('big', 'Big'),
            ('medium', 'Medium'),
            ('small', 'Small')
        ],
        string='Dialer size',
        default='medium',
        config_parameter='ringover_dialer.ringover_dialer_size'
    )

    ringover_dialer_position = fields.Selection(
        [
            ('tr', 'Top right'),
            ('br', 'Bottom right'),
            ('bl', 'Bottom left'),
            ('tl', 'Top left'),

        ],
        string='Dialer position',
        default='br',
        config_parameter='ringover_dialer.ringover_dialer_position'
    )

    @api.model
    def get_conf_param_dialer(self, param1=''):
        size = self.env['ir.config_parameter'].sudo().get_param('ringover_dialer.ringover_dialer_size', 'medium')
        pos = self.env['ir.config_parameter'].sudo().get_param('ringover_dialer.ringover_dialer_position', 'br')
        tray_icon = self.env['ir.config_parameter'].sudo().get_param('ringover_dialer.ringover_dialer_tray_icon', False)
        result = {
            'size': size,
            'position': pos,
            'trayicon': tray_icon
        }
        print('dialer conf --->', result)
        return result
