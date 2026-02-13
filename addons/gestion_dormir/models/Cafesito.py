# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Cafesito(models.Model):
    _name = 'gestion.dormir'
    _description = 'Deberías tomar café'

    name = fields.Char(string='Alumno', required=True)
    sleepy = fields.Integer(string='Nivel de Sueño (1-10)', default=1)
    coffee = fields.Char(string='Bebida Recomendada', compute='_compute_bebida', store=True)

    @api.depends('sleepy')
    def _compute_bebida(self):
        for record in self:
            if 1 <= record.sleepy <= 3:
                record.coffee = 'Café con leche'
            elif 4 <= record.sleepy <= 6:
                record.coffee = 'Café solo largo'
            elif 7 <= record.sleepy <= 9:
                record.coffee = 'Café solo larguísimo'
            elif record.sleepy >= 10:
                record.coffee = 'Inyección de adrenalina'
            else:
                record.coffee = 'Agua fresca'