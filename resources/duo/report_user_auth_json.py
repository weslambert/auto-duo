#!/usr/bin/env python
from __future__ import print_function
from __future__ import absolute_import
import argparse
import sys
import duo_client
import json
from six.moves import input
from ConfigParser import SafeConfigParser
import datetime
import calendar

# Args
parser = argparse.ArgumentParser(description='This script will query the Duo Admin API for authentication logs.')
parser.add_argument('-m','--minutes_ago', help='Input file name',required=True)
args = parser.parse_args()

# Get current time and define value for number of minutes ago (default is 1 minute)
minutes_ago = int(args.minutes_ago)
d = datetime.datetime.utcnow() - datetime.timedelta(minutes=minutes_ago)
num_minutes_ago=calendar.timegm(d.utctimetuple())

# Parse config file details
parser = SafeConfigParser()
parser.read('/etc/duo/duo.conf')

admin_api = duo_client.Admin(
ikey = parser.get('config', 'ikey'),
skey = parser.get('config', 'skey'),
host = parser.get('config', 'host')
)

# Retrieve log info from API:
logs = admin_api.get_authentication_log(mintime=num_minutes_ago)

# Write logs to file
with open("/var/log/duo/duo_auth.json", "wb") as outfile:
  for log in logs:
      json.dump(log, outfile, indent=4)
      outfile.write("\n")
