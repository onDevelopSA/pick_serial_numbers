# -*- coding: utf-8 -*-
from odoo import http

# class StockSerialNumbers(http.Controller):
#     @http.route('/stock_serial_numbers/stock_serial_numbers/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_serial_numbers/stock_serial_numbers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_serial_numbers.listing', {
#             'root': '/stock_serial_numbers/stock_serial_numbers',
#             'objects': http.request.env['stock_serial_numbers.stock_serial_numbers'].search([]),
#         })

#     @http.route('/stock_serial_numbers/stock_serial_numbers/objects/<model("stock_serial_numbers.stock_serial_numbers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_serial_numbers.object', {
#             'object': obj
#         })