from flask import Flask, _request_ctx_stack
import threading


app = Flask(__name__)


def foo():
    request_context = app.test_request_context()
    _request_ctx_stack.push(request_context)
    print(_request_ctx_stack._local.__storage__)
    print('\n\n')

#
# for i in range(10):
#     t = threading.Thread(target=foo)
#     t.start()
#     t.join()

import sys, os

path = sys.modules[__name__].__file__
print(os.path.abspath(os.path.dirname(path)))