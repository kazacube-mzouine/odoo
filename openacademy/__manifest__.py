# -*- coding: utf-8 -*-
{
    'name': "Openacademy",

    'summary': """
        Course
        """,

    'author': "Kazacube",
    'website': "http://www.Kazacube.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/cours_data.xml',
        'views/course_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,
}