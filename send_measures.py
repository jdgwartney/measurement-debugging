#!/usr/bin/env python

from tspapi import API
from tspapi import Measurement
from random import randint
from datetime import datetime
from time import sleep


def create_batch():
  delay = 30
  api = API()
  measurements = []
  timestamp = int(datetime.now().strftime('%s'))
  # skew timestamp by 5 seconds
  timestamp = timestamp - delay
  measurements.append(Measurement(metric='API_TEST_METRIC', value=randint(0, 99), source='red', timestamp=timestamp))
  measurements.append(Measurement(metric='API_TEST_METRIC', value=randint(0, 99), source='green', timestamp=timestamp))
  measurements.append(Measurement(metric='API_TEST_METRIC', value=randint(0, 99), source='blue', timestamp=timestamp))
#  sleep(float(delay))
  api.measurement_create_batch(measurements)

def create():
  api = API()
  metric_id = 'API_TEST_METRIC'
  value = ranint(0, 99)
  source = 'foo'
  timestamp = datetime.now().strftime('%s')
  api.measurement_create(metric_id, value, source, timestamp)

if __name__ == "__main__":
  create_batch()
