from odoo import fields, models

class Payment(models.Model):
    name = 'models'
    _inherit = 'account.payment'
    
    payment_method_id = fields.Many2one('payment.method', string='Payment Method')
