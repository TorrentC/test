from flask import Flask
from werkzeug import serving
from werkzeug.wrappers import Request
from wsgiref.simple_server import make_server
from werkzeug.local import LocalStack
from werkzeug.contrib import securecookie

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world'


class A(object):
    def __enter__(self):
        print('enter')

    def __exit__(self, *args, **kwargs):
        print('exit', args, kwargs)


def back_a():
    return A()


def demo_app(environ, start_response):
    print(environ['PATH_INFO'])
    request = Request(environ)
    print(request)
    request.cookies
    from StringIO import StringIO
    stdout = StringIO()
    print >>stdout, "Hello world!"
    print >>stdout
    h = environ.items(); h.sort()
    for k,v in h:
        print >>stdout, k,'=', repr(v)
    start_response("200 OK", [('Content-Type', 'text/plain')])
    return [stdout.getvalue()]


if __name__ == '__main__':
    make_server('', 5000, demo_app).serve_forever()
    app.run()
    app.__call__
    app.wsgi_app
    # with back_a() as a:
    #     pass