# -*- coding: utf-8 -*-
{
    'name': "Nivel de sueño",

    'summary': "Tómate un café",

    'description': """
Este módulo te recomienda que café deberías tomarte dependiendo del sueño que tengas
    """,

    'author': "Jorge",

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/gestion_cafe_views.xml',
    ],

    'installable': True,
    'application': True,
}

