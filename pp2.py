        import pika, sys, os
        import datetime
        from datetime import datetime
        import time
        import csv
        import pandas

        import pika, os, logging
        logging.basicConfig()
        from csv import reader

        import pandas as pd
        df=pd.read_csv("/data/data.csv")
        df['Date']=pd.to_datetime(df['Date'])
        print (type(df['Date'][0]))
        print(df)
        df.set_index('Date', inplace=True)
        import numpy as np
        df=df.replace({'Humidity':'0', 'Temperature':'0'},np.NaN)
        df=df.interpolate()
        df3=df.pivot_table(index=pd.Grouper(freq='T')) #.agg({'Sound':'sum','Flame':'sum'}) #,columns=['Humidity','Temperature']) #/// freq=S,T,h,M,Y
#        df3 = df3[['Date','Sound','Flame','Humidity','Temperature']] #[['mean', '0', '1', '2', '3']]
        print(df3)
        dff = df3.reindex(columns=['Sound','Flame','Humidity','Temperature'])
#        dff.columns = pd.Index([0], dtype='int64')

        #df3.sort(['Date','Sound','Flame','Humidity','Temperature'])
        print(dff)
        dff['Sound']=dff['Sound'].apply(np.ceil) #().astype('int')
        dff['Sound']=dff['Sound'].astype('int')
        dff['Flame']=dff['Flame'].apply(np.ceil) #().astype('int')
        dff['Flame']=dff['Flame'].astype('int')
        dff['Humidity']=dff['Humidity'].round(0).astype('int')
        dff['Temperature']=dff['Temperature'].round(0).astype('int')
        print(dff)
        dff.to_csv('/data/data1.csv') #, index=False)
        //dff.flush
        //dff.close
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
        with open('/data/data1.csv', 'r') as csvfile:
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
        
