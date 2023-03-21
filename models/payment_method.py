from odoo import models, fields, api

class PaymentMethod(models.Model):
    _name = 'payment.method'
    _description = 'Payment Method'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    description = fields.Text(string='Description')
    payment_type = fields.Selection(
        [('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('bank_transfer', 'Bank Transfer')],
        string='Payment Type', required=True)

    @api.model
    def create(self, vals):
        res = super(PaymentMethod, self).create(vals)
        # Your custom code here
        return res

    def write(self, vals):
        res = super(PaymentMethod, self).write(vals)
        # Your custom code here
        return res

