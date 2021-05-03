# -*- coding: utf-8 -*-
# © 2021 onDevelop.sa
# Autor: Idelis Gé Ramírez
# Part of onDevelop.SA. See LICENSE file for full copyright and licensing details.
{
    'name': "Pick Serial Numbers Massive Update",
    'summary': """Massive Upload the Lot/ Serial Number of the stock move line.""",
    'description': """ Update the Lot/Serial Numbers in the lines of specific
    stock move using the import default process.
    """,
    'author': "onDevelop.SA",
    'website': "https://ondevelop.tech/",
    'category': 'Operations/Inventory',
    'version': '14.0.1',
    'license': 'LGPL-3',
    'currency': 'USD',
    'support': "ondevelop.sa@gmail.com",
    'depends': ['base', 'stock'],
    'images': ['static/description/pick_serial_number_update_cover.png'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/templates.xml',
    ],
    'demo': ['demo/demo.xml'],
    'installable': True,
    'auto_install': False
}
