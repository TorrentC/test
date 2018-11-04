from wsgiref.simple_server import make_server, demo_app


class Light(object):
    def __init__(self):
        pass

    def __call__(self, environ, start_response):
        for k, v in environ.items():
            print('%s----->%s' % (k, v))
        start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
        return ['abc']

    def run(self, host='127.0.0.1', port=5000):
        server = make_server(host, port, app=self)
        print 'Listening on http://%s:%d/' % (host, port)
        print 'Use Ctrl-C to quit.'
        print
        server.serve_forever()


if __name__ == '__main__':
    app = Light()
    app.run()

