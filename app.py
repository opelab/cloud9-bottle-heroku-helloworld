# -*- coding:utf-8 -*-

import os
from bottle import route, run
from bottle import error

@route('/hello/')
@route('/hello/<user>')
def hello(user="taro"):
    return "Hello {user}".format(user=user)


@route('/date/<month:re:[a-z]+>/<day:int>/<path:path>')
def date(month, day, path):
    return "{month}/{day} {path}".format(month=month, day=day, path=path)


@error(404)
def error404(error):
    return "Nothing here sorry {error}".format(error=error)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))