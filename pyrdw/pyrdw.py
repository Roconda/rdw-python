#!/usr/bin/python
import re
import json
import urllib2

def get(license_plate):
  # Filter license plate
  filter_pattern = re.compile(r'[a-zA-Z\d]+')
  plate = ''.join(filter_pattern.findall(license_plate))

  try: 
    req = urllib2.urlopen("https://api.datamarket.azure.com/opendata.rdw/VRTG.Open.Data/v1/KENT_VRTG_O_DAT('%s')?$format=json" % plate).read()
  except urllib2.HTTPError:
    # Return None if no car has been found
    return None

  return json.loads(req)['d']
