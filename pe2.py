import pika, os, logging
logging.basicConfig()
from csv import reader
import csv
# Parse CLODUAMQP_URL (fallback to localhost)
#url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost/%2f')
#url = os.environ.get('CLOUDAMQP_URL', 'amqps://xmxasmuw:6ff5SA9lmND2obcLUS2Se1aacrK1Hh-1@snake.rmq2.cloudamqp.com/xmxasmuw/%2f')
url = os.environ.get('CLOUDAMQP_URL', 'amqps://kacojdss:aUd8wEoKcyHLCK46a1_AifxUBDzjsLHi@beaver.rmq.cloudamqp.com/kacojdss')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.queue_declare(queue='pdfprocess') # Declare a queue
# send a message
##import pandas as pd
##df=pd.read_csv('data1.csv')
##for row in df:
#with open('data1.csv', 'r') as read_obj:
 #   csv_reader = reader(read_obj)
   # header = next(csv_reader)

csv.register_dialect('csv_dialect',
                    delimiter='[',
                    skipinitialspace=True,
                    quoting=csv.QUOTE_ALL)
with open('data1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='csv_dialect')
    header=next(reader)
   
 # Check file as empty
    if header != None:
#import pandas as pd
#df=pd.read_csv('data1.csv')
        for row in reader:
   # row variable is a list that represents a row in csv
#import pandas as pd
#df=pd.read_csv('data1.csv') #,usecols=['Date', 'Sound', 'Flame', 'Humidity', 'Temperature']) 

#for row in 'data1.csv': 
           print(row)
           channel.basic_publish(exchange='', routing_key='pdfprocess', body=str(row))
print ("[x] Message sent to consumer")
connection.close()


