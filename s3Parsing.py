"""s3Parsing
Usage:
  s3Parsing.py date <YYYYMMDD>...
  s3Parsing.py
"""
import boto3
from datetime import datetime
import glob
from docopt import docopt

def getFileLocation(bucketName, pattern):

    resource = boto3.resource('s3')
    srcBucket = resource.Bucket(bucketName)

    allObjects = []
    for object in srcBucket.objects.all():
        if glob.fnmatch.fnmatch(object.key,pattern):
            print(object.key)
            allObjects.append(object.key)


    print(allObjects)

if __name__ == '__main__':
    arguments = docopt(__doc__, version= 'S3_Parser version 1.0')
    print(arguments)
    date = arguments['<YYYYMMDD>']
    if date:
        for item in date:
            year = item[:4]
            month = item[4:6]
            day = item[6:]
            pattern = '*' + 'year=' + year + '/month=' + month + '/day=' + day + '/*.csv'
            print('{0} {1} {2}'.format("year is "+ year, "month is "+month, "day is "+day))
    else:
        currentTime = datetime.now()
        year = currentTime.strftime("%Y")
        month = currentTime.strftime("%m")
        day = currentTime.strftime("%d")
        pattern = '*' + 'year=' + year + '/month=' + month + '/day=' + day + '/*.csv'
    print(pattern)
    getFileLocation(bucketName=<bucketName>, pattern=pattern)