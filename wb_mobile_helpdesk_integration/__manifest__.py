# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Weblearns Mobile Helpdesk Integration',
    'version' : '1.1',
    'summary': 'Mobile Helpdesk Integration',
    'author': 'Weblearns',
    'sequence': 10,
    'description': "Mobile Helpdesk Integration",
    'category': 'helpdesk',
    'website': 'https://onlineweblearns.blogspot.com',
    'depends' : ['helpdesk'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'view/helpdesk_request_view.xml'
    ],
    'installable': True,
    'license': 'LGPL-3',
}
