# Copyright 2020-2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Res Partner Membership",
    "summary": """
        This module add Membership functionality on partner and display it on
         both Contact record and Sales Order.
        """,
    "version": "17.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://sodexis.com/",
    "author": "Sodexis",
    "license": "OPL-1",
    "installable": True,
    "application": False,
    "images": ["images/main_screenshot.jpg"],
    "depends": [
        "sale",
        "contacts",
    ],
    "data": [
        "data/membership_data.xml",
        "security/membership_security.xml",
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/sale_views.xml",
    ],
}
