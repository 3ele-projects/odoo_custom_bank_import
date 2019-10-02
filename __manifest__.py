# -*- coding: utf-8 -*-
{
    'name': "custom_bank_import",

    'summary': """
        Add a custom search for bank.statement.line validation""",

    'description': """
        Inherit bank.import.statement model to match bank.statement with the invoice.origin field.
        Caution: This Model is needs the account_bank_statement_import
    """,

    'author': "3ele | Sebastian Weiss",
    'website': "https://3ele.de",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_bank_statement_import'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
