{
    'name': 'Facturas Recurrentes',
    'summary': 'Agregue funcionalidades de pago en línea, factura recurrente y seguimiento de facturas.',
    'description': 'Este módulo agrega funcionalidades de pago en línea, factura recurrente y seguimiento de facturas a Odoo.',
    'version': '1.0',
    'category': 'Accounting/Invoicing',
    'author': 'Miguel Fernandez Fernandez',
    'images': ['static/description/icon.png'],
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/module_menu.xml',
        'views/payment_view.xml',
        'views/invoice_view.xml',
        'views/invoice_calendar_view.xml',
        'views/invoice_kanban_view.xml'
    ],
}
