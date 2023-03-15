# -*- coding: utf-8 -*-
{
    'name': 'Facturas',
    'version': '1.0',
    'author': 'Miguel Fernández Fernández',
    'summary': 'Módulo para gestionar facturas',
    'description': 'Este módulo permite gestionar facturas en Odoo',
    'category': 'Contabilidad',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/factura_form.xml',
        'views/factura_calendar.xml',
        'views/factura_kanban.xml',
        'views/factura_list.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
