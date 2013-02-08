"""  
    Copyright, Ang Lee, 2013, All rights reserved.
    ang.lee@gmail.com
"""
import os.path

import tornado.web
import tornado.wsgi
import wsgiref.handlers

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        pycode = "', '. join([str(x * x) for x in range(10)])" 
        self.render('index.html', code=pycode, result=eval(pycode))
    def post(self):
        pycode = self.get_argument('code')
        self.render('index.html', code=pycode, result=eval(pycode))

if __name__ == '__main__':
    app = tornado.wsgi.WSGIApplication(
        handlers=[(r'/', IndexHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
                )
    wsgiref.handlers.CGIHandler().run(app)
