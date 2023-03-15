from odoo import models, fields, api


class Factura(models.Model):
    _name = 'facturas.factura'
    _description = 'Modelo para facturas'

    # Campos básicos de la factura
    name = fields.Char(string='Nombre de factura', required=True)
    fecha_emision = fields.Date(string='Fecha de emisión', required=True)
    fecha_limite_pago = fields.Date(string='Fecha límite de pago', required=True)
    state = fields.Selection(
        [('draft', 'Borrador'), ('to_pay', 'A pagar'), ('to_receive', 'A cobrar')],
        string='Estado',
        default='draft',
        required=True)
    # Campos relacionales
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    linea_ids = fields.One2many('mi_modulo.factura.linea', 'factura_id', string='Líneas de Factura')

    # Campos calculados
    total_factura = fields.Float(string='Total de la Factura', compute='_compute_total_factura')

    @api.depends('linea_ids')
    def _compute_total_factura(self):
        for factura in self:
            factura.total_factura = sum(linea.subtotal for linea in factura.linea_ids)


class FacturaLinea(models.Model):
    _name = 'mi_modulo.factura.linea'
    _description = 'Línea de Factura'

    # Campos de la línea de factura
    factura_id = fields.Many2one('mi_modulo.factura', string='Factura', ondelete='cascade')
    producto_id = fields.Many2one('product.product', string='Producto', required=True)
    cantidad = fields.Float(string='Cantidad', required=True)
    precio_unitario = fields.Float(string='Precio Unitario', required=True)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal')

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for linea in self:
            linea.subtotal = linea.cantidad * linea.precio_unitario
