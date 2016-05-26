#!/usr/bin/env python

# Let's import tornado and tornadis
import os
import sys
import tornado
import tornadis
import tornado.web
import tornado.ioloop


@tornado.gen.coroutine
def talk_to_redis():
    # let's (re)connect (autoconnect mode), call the ping redis command
    # and wait the reply without blocking the tornado ioloop
    # Note: call() method on Client instance returns a Future object (and
    # should be used as a coroutine).
    result = yield client.pubsub_subscribe("channel1")
    if isinstance(result, tornadis.TornadisException):
        # For specific reasons, tornadis nearly never raises any exception
        # they are returned as result
        print "got exception: %s" % result
    else:
        # result is already a python object (a string in this simple example)
        print "Result: %s" % result
    while True:
       result = yield client.pubsub_pop_message()
       if isinstance(result, tornadis.TornadisException):
           # For specific reasons, tornadis nearly never raises any exception
           # they are returned as result
           print "got exception: %s" % result
       else:
           # result is already a python object (a string in this simple example)
           print "Result: %s" % result


# Build a tornadis.Client object with some options as kwargs
# host: redis host to connect
# port: redis port to connect
# autoconnect=True: put the Client object in auto(re)connect mode

# Start a tornado IOLoop, execute the coroutine and end the program
ioloop = tornado.ioloop.IOLoop.instance()
#ioloop.run_sync(talk_to_redis)
client = tornadis.PubSubClient(host="localhost", port=6379, autoconnect=True)
ioloop.run_sync(talk_to_redis)
try:
  ioloop.start()
except KeyboardInterrupt:
  pass
finally:
  print "Closing server...\n"
  tornado.ioloop.IOLoop.instance().stop()
