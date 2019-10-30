# -*- coding: utf-8 -*-
{
    'name': 'SANS',
    'version': '13.0.1.05',
    'category': 'Studio',
    "sequence": 1,
    'website': 'https://restyn-sans-demo.odoo.com/',
    'description': u"""
SANS Event Fulfillment System
===========================

APPS:
-----
 - EVENTS

Written by Joe Shields for SANS 10/1/2019

Last Production update: 
""",
    'author': 'RESTYN',
    'depends': [
        'base',
        'website_event',
        'website_event_sale',
    ],
    'data': [
        'views/event_templates.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'OPL-1',
}