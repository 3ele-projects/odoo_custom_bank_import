# -*- coding: utf-8 -*-
from odoo import http

# class CustomBankImport(http.Controller):
#     @http.route('/custom_bank_import/custom_bank_import/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_bank_import/custom_bank_import/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_bank_import.listing', {
#             'root': '/custom_bank_import/custom_bank_import',
#             'objects': http.request.env['custom_bank_import.custom_bank_import'].search([]),
#         })

#     @http.route('/custom_bank_import/custom_bank_import/objects/<model("custom_bank_import.custom_bank_import"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_bank_import.object', {
#             'object': obj
#         })