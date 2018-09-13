from sys import argv

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
    <h3>Veldu uppáhalds liðið þitt</h3>
    <a href="/sida2?lid=Astralis"><img src='Images/Astralis.png'></a>
    <a href="/sida2?lid=North"><img src='Images/North.png'></a>
    <a href="/sida2?lid=Liquid"><img src='Images/Liquid.png'></a>
    """

@route("/sida2")
def page():
    I = request.query.lid
    if I=="Astralis":
        return "<h3>Þetta er uppáhaldsliðið mitt</h3><img src='Images/Astralis.png'>"
    elif I=="North":
        return "<h3>Þetta er uppáhaldsliðið mitt</h3><img src='Images/North.png'>"
    elif I=="Liquid":
        return "<h3>Þetta er uppáhaldsliðið mitt</h3><img src='Images/Liquid.png'>"

@error(404)
def villa(error):
    return "<h2>Error: 404 Not Found</h2>"

@route("/Images/<skra>")
def static_skra(skra):
    return static_file(skra, root="Images")

bottle.run(host="0.0.0.0", port=argv[1])
