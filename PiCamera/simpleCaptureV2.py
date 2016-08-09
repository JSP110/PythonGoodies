# This program takes picture using picamera, and delete files older than 14 days.
import picamera
from datetime import datetime
import os, time

camera = picamera.PiCamera()
camera.resolution = (512,384)


# adapted from http://blog.rackspacecloudreview.com/86-freebie-python-chron-to-delete-files-older-than-x/
def cleanDir(dir, age):
  print "Scanning:", dir
  for f in os.listdir(dir):
    now = time.time()
    filepath = os.path.join(dir, f)
    modified = os.stat(filepath).st_mtime
    if modified < now - age: 
      if os.path.isfile(filepath):
        os.remove(filepath)
        print 'Deleted: %s (%s)' % (f, modified)

# 1 Day	= 86400 seconds
# cleanDir("/system/path/to/folder", (7 * 86400))

while True:
  currentHour = int(datetime.now().strftime('%H'))
  print ("Current Hour = " + str(currentHour))
  if (currentHour > 8 and currentHour <23):
    print ("Taking photo = yes")
    camera.capture('/home/pi/images/images/%s.jpg' %datetime.now().strftime('%Y%m%d_%H%M%S'))
  else:
    print ("Taking photo = no")
  cleanDir("/home/pi/images", (14 * 86400)) #clean files older than 14 days
  time.sleep(120)