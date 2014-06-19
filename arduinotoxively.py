#!/usr/bin/env python

import os
import xively
import subprocess
import time
import datetime
import requests
import serial

# extract feed_id and api_key from environment variables
FEED_ID = "YOURFEEDID"
API_KEY = "YOURPRIVATEKEY"
DEBUG = 1

# initialize api client
api = xively.XivelyAPIClient(API_KEY)

if DEBUG:
  print "Opening serial port connection"
# open serial port
ser = serial.Serial('/dev/ttyACM0',9600)


# function to return a datastream object. This either creates a new datastream,
# or returns an existing one
def get_datastream(feed):
  try:
    datastream = feed.datastreams.get("Temperature")
    if DEBUG:
      print "Found existing datastream"
    return datastream
  except:
    if DEBUG:
      print "Creating new datastream"
    datastream = feed.datastreams.create("Temperature", tags="")
    return datastream

# main program entry point - runs continuously updating our datastream with the
# current 1 minute load average
def run():
  print "Starting Xively script"

  feed = api.feeds.get(FEED_ID)

  datastream = get_datastream(feed)
  datastream.max_value = None
  datastream.min_value = None

  while True:
    if DEBUG:
      print "Reading serial"

    temperature = ser.readline()


    if DEBUG:
      print "Updating Xively feed with value: %s" % temperature

    datastream.current_value = temperature
    datastream.at = datetime.datetime.utcnow()
    try:
      datastream.update()
    except requests.HTTPError as e:
      print "HTTPError({0}): {1}".format(e.errno, e.strerror)

    time.sleep(10)

run()
