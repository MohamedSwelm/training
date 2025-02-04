# -*- coding: utf-8 -*-
{
    'name': "training_app",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "mohammed swelm",
    # 'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale_management','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/purchase_request_view.xml',
        'wizards/rejected_reason_view.xml',
        'views/product_template_view.xml',
        'views/sale_order_line_view.xml',
        # 'views/stock_move_view.xml',
        'views/stock_picking_view.xml',
        'views/account_move_view.xml',


    ],
}

