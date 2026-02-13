# -*- coding: utf-8 -*-
# from odoo import http


# class GestionDormir(http.Controller):
#     @http.route('/gestion_dormir/gestion_dormir', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_dormir/gestion_dormir/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_dormir.listing', {
#             'root': '/gestion_dormir/gestion_dormir',
#             'objects': http.request.env['gestion_dormir.gestion_dormir'].search([]),
#         })

#     @http.route('/gestion_dormir/gestion_dormir/objects/<model("gestion_dormir.gestion_dormir"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_dormir.object', {
#             'object': obj
#         })

