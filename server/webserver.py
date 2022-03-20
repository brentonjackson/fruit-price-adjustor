from bottle import route, run, template, static_file
import os


def get_price():
    f = open('currentFruitPrice.txt')
    return f.read()

# create server


@route('/')
def index():
    return template('index', priceStr=get_price())


@route('/images')
def index(source='currentFrame.jpg'):
    response = '<h1>Live Video Feed</h1>'
    response += '<image src=' + source + '>'
    return response


# run server
run(host='0.0.0.0', port=5000)
