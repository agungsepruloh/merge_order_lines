# -*- coding: utf-8 -*-

{
    'name': "Merge Sale Order Items",

    'summary': """
        This module will help you to merge duplicate sale order lines with same product.
    """,

    'description': """
        This module will help you to merge duplicate sale order line with same product.
    """,

    'author': "Agung Sepruloh",
    'website': "https://github.com/agungsepruloh",
    'license': 'LGPL-3',
    'maintainers': ['agungsepruloh'],
    'category': 'Sales',
    'version': '17.0.1.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        'views/res_config_settings_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],

    'images': ['static/description/banner.gif'],
    'application': True,
}
