from odoo import http
from odoo.http import request

class MiModuloFacturaController(http.Controller):
    @http.route('/mi_modulo/facturas/', auth='user', website=True)
    def index(self, **kw):
        Factura = request.env['mi_modulo.factura']
        facturas_a_pagar = Factura.search([('estado', '=', 'a_pagar')])
        facturas_a_cobrar = Factura.search([('estado', '=', 'a_cobrar')])
        facturas_borrador = Factura.search([('estado', '=', 'borrador')])
        return http.request.render('mi_modulo.factura_index', {
            'facturas_a_pagar': facturas_a_pagar,
            'facturas_a_cobrar': facturas_a_cobrar,
            'facturas_borrador': facturas_borrador,
        })

    @http.route('/mi_modulo/facturas/nueva', auth='user', website=True)
    def nueva_factura(self, **kw):
        return http.request.render('mi_modulo.factura_nueva', {})
    
    @http.route('/mi_modulo/facturas/crear', auth='user', methods=['POST'], website=True)
    def crear_factura(self, **kw):
        Factura = request.env['mi_modulo.factura']
        factura = Factura.create({
            'nombre': kw.get('nombre'),
            'fecha_emision': kw.get('fecha_emision'),
            'fecha_limite_pago': kw.get('fecha_limite_pago'),
            'estado': kw.get('estado'),
        })
        return http.request.redirect('/mi_modulo/facturas/')
