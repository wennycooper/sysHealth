#!/usr/bin/env python
import web

urls = (
    '/sysHealth', 'sysHealth'
)

app = web.application(urls, globals())

class sysHealth:        
    def GET(self):
        output = 'good'
        return output

if __name__ == "__main__":
    app.run()
