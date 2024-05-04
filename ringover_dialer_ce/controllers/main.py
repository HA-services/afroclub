import logging

from odoo import http
from odoo.addons.ringover_dialer_ce.models.res_config_settings import ResConfigSettings

_logger = logging.getLogger(__name__)


class Main(http.Controller):

    @http.route('/ringover_dialer_ce/settings/get', type='json', auth='user')
    def get_dialer_settings(self, *args, **kwargs):
        dialer_model = http.request.env['res.config.settings']
        return dialer_model.get_conf_param_dialer()
