# Part of Tech Terminologie. See LICENSE file for full copyright & licensing details.
{
    'name': 'Theme Fintech',
    'description': 'Theme Fintech',
    'summary': 'Theme Fintech',
    'category': 'theme',
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/homepage.xml',
        'views/about_us.xml',
        'views/faq.xml',
        'views/footer.xml',
        'views/header.xml',
        'views/pricing.xml',
        'views/services.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'theme_fintech/static/src/scss/primary_variables.scss'),
       ],
        'web.assets_frontend': [
            # 'theme_fintech/static/src/scss/primary_variables.scss',
            'theme_fintech/static/src/scss/style.scss',
        ],
    },
    'images': [
        'static/description/images/fintech-banner.png',
        'static/description/fintech-portrait.png',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 99.99,
    'currency': 'USD',
}
