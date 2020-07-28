# -*- coding: utf-8 -*-
from bottle import default_app, route

@route('/')
def hello_world():
    return 'Tutorial Discipulus: Introdução aplicativo web'



application = default_app()

