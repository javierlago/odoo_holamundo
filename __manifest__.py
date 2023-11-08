{
    'name': "odoo_holamundo",

    'summary': """
        Proxecto inicial""",

    'description': """
        Este es mi primer modulo
        
    """,

    'author': "Javier Lago Amoedo",
    'website': "https://www.edu.xunta.gal/centros/iesteis/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

        'views/holamundo.xml',
        'views/menu.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
# -*- coding: utf-8 -*-
