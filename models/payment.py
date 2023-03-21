from odoo import fields, models

class Payment(models.Model):
    name = 'account.payment'
    _inherit = 'account.payment'
    
    payment_method_id = fields.Many2one('payment.method', string='Payment Method')
