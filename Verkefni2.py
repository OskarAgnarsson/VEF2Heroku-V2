#from sys import argv

from bottle import *

@route("/")

def index():
    return """
    <h1>Verkefni 2</h1>
    <a href="/a">Liður A</a>
    <a href="/b">Liður B</a>
    """
@route("/a")

def a():
    return """
    <h2>Verkefni 2 - A</h2>
    <a href="/sida/1">Síða 1</a>
    <a href="/sida/2">Síða 2</a>
    <a href="/sida/3">Síða 3</a>
    """

@route("/sida/<id>")

def page(id):
    if id=="1":
        return "<h2>Þetta er síða 1</h2> <br> <a href='/a'>Til baka</a>"
    elif id=="2":
        return "<h2>Þetta er síða 2</h2> <br> <a href='/a'>Til baka</a>"
    elif id=="3":
        return "<h2>Þetta er síða 3</h2> <br> <a href='/a'>Til baka</a>"
    else:
        return "<h2>Error: 404 Not Found</h2>"

@route("/b")

def b():
    return """
    <h2>Verkefni 2 - B</h2>
    <a><img></img></a>
    <a><img></img></a>
    <a><img></img></a>
    """

@error(404)
def villa(error):
    return "<h2>Error: 404 Not Found</h2>"


run(host="Localhost", port=8080, reloader=True, debug=True)

#bottle.run(host="0.0.0.0", port=argv[1])
