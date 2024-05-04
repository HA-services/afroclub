# -*- coding: utf-8 -*-
{
    'name': "Ringover",

    'summary': """
        Make and receive calls and SMS, sync contacts, 
        capture conversation history and recordings right from your Odoo Platform. 
        CE (Community Edition) only
    """,

    'description': """
        For Odoo 17 CE
    """,

    'author': "Ringover",
    'website': "https://www.ringover.com/",

    'category': 'Productivity',
    'version': '1.0',
    'application': True,
    'installable': True,


    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ringover_dialer_ce/static/src/**/*',
            'https://webcdn.ringover.com/resources/SDK/1.1.3/ringover-sdk.js',
        ]
    },
    'images': ['static/description/cover_thumbnail.png'],
    'license': 'OPL-1'
}
