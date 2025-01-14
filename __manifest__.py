# -*- coding: utf-8 -*-
{
    'name': "challenge_CRM_Affiliate",

    'summary': """
        Odoo CRM-Affiliate Module
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Gelareh Seddigh",

    'category': 'Uncategorized',
    'version': '1.0',

    'depends': ['crm' ],

    'data': [
        'data/affiliates_data.xml',
        'security/ir.model.access.csv',
        'views/crm_affiliate_view.xml',
        'views/crm_lead_view.xml',
        'views/menu.xml',
    ],
    
    
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
