from odoo import fields, models

class Invoice(models.Model):
    _inherit = 'account.invoice'
    
    is_recurring = fields.Boolean(string='Is Recurring Invoice')
    recurring_interval = fields.Selection([('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], string='Recurring Interval')
    recurring_last_date = fields.Date(string='Last Date of Recurring Invoice')
    payment_method_id = fields.Many2one('payment.method', string='Payment Method')