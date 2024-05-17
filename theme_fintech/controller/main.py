# Part of Tech Terminologie. See LICENSE file for full copyright & licensing details
from odoo import http, _
from odoo.http import request


class ThemefintechTemplates(http.Controller):

    @http.route(['/'], type='http', auth="public", website=True)
    def ThemeFintechHome(self, **kw):
        return request.render('theme_fintech.theme_fintech_home')

    @http.route(['/fintech/about-us'], type='http', auth="public", website=True)
    def ThemeFintechAboutUs(self, **kw):
        return request.render('theme_fintech.theme_fintech_about_us')

    @http.route(['/fintech/services'], type='http', auth="public", website=True)
    def ThemeFintechServices(self, **kw):
        return request.render('theme_fintech.theme_fintech_services')

    @http.route(['/fintech/pricing'], type='http', auth="public", website=True)
    def ThemeFintechPricing(self, **kw):
        return request.render('theme_fintech.theme_fintech_pricing')

    @http.route(['/fintech/faq'], type='http', auth="public", website=True)
    def ThemeFintechFAQ(self, **kw):
        return request.render('theme_fintech.theme_fintech_faq')
