#!/usr/bin/env python

# Let's import tornado and tornadis
import os
import sys
import tornado
import tornado.web
import tornado.ioloop

class EditorHandler(object):
   def __init__(self):
       self.sessions = {}

   @tornado.gen.coroutine
   def create_session(self, data, ws):
   	   try:
   	   	  self.sessions[data[id]]['listeners'].append(ws)
   	   except KeyError:
   	   	  self.sessions[data[id]]['listeners'] = [ws]
   	   	  self.sessions[data[id]]['path'] = data[path]
   	   for listener in listeners:
   	       listener.notify_login(ws.login_name)

   def get_file(self, req):
       	


