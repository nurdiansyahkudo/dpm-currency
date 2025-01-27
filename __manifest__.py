{
    'name': "DPM Manual Currency",
    'version': '17.0.1.0.0',
    'category': 'Accounting',
    'summary': """By using this module ,we can change the currency rate manually
     in sale ,purchase and invoice. """,
    'description': """By using this module, we can manually adjust the currency
     rate for key aspects of our business operations, including sales,
     purchases, and invoicing. This feature gives us the power to have precise
     control over currency conversions and adapt quickly to fluctuating 
     exchange rates.""",
    'author': '',
    'company': '',
    'maintainer': '',
    'website': '',
    'depends': ['base', 'account'],
    'data': [
        'views/account_move_views.xml',
        'views/res_currency_views.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}