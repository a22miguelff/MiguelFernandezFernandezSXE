from odoo import http
from odoo.http import request

class MiModuloFacturaController(http.Controller):
    @http.route('/facturas/facturas/', auth='user', website=True)
    def index(self, **kw):
        Factura = request.env['facturas.factura']
        facturas_a_pagar = Factura.search([('estado', '=', 'a_pagar')])
        facturas_a_cobrar = Factura.search([('estado', '=', 'a_cobrar')])
        facturas_borrador = Factura.search([('estado', '=', 'borrador')])
        return http.request.render('facturas.factura_index', {
            'facturas_a_pagar': facturas_a_pagar,
            'facturas_a_cobrar': facturas_a_cobrar,
            'facturas_borrador': facturas_borrador,
        })

    @http.route('/facturas/facturas/nueva', auth='user', website=True)
    def nueva_factura(self, **kw):
        return http.request.render('facturas.factura_nueva', {})
    
    @http.route('/facturas/facturas/crear', auth='user', methods=['POST'], website=True)
    def crear_factura(self, **kw):
        Factura = request.env['facturas.factura']
        factura = Factura.create({
            'nombre': kw.get('nombre'),
            'fecha_emision': kw.get('fecha_emision'),
            'fecha_limite_pago': kw.get('fecha_limite_pago'),
            'estado': kw.get('state'),
        })
        return http.request.redirect('/facturas/facturas/')
