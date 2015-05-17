#!/usr/bin/python
from datetime import datetime, timedelta
import argparse

parser = argparse.ArgumentParser(description='Find a time in the future.')
parser.add_argument("hours", metavar="N", type=int, nargs="+",
                       help="How many hours from now?")
args = parser.parse_args()

def future_time(hours):
  d = datetime.now() + timedelta(hours=hours)
  d = '{:%H:%M}'.format(d)
  d = datetime.strptime(str(d), "%H:%M")
  return d.strftime("%I:%M %p")

print future_time(args.hours[0])
