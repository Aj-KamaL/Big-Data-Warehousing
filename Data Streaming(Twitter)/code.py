#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import numpy as np
from tweepy import Stream
import tweepy
from kafka import KafkaProducer, KafkaConsumer
import time
import pickle
import random 
import sys, select, os

# In[2]:


access_token = '***************************************************'
access_token_secret = '***************************************************'
consumer_key = '***************************************************'
consumer_secret = '***************************************************'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# In[4]:


Buffer = []
SurpriseNo = []
producer = KafkaProducer(bootstrap_servers="localhost:9092")
topic_name  = 'COVID_Fi'


# In[5]:


def calculateAMS(seq, sampled, counters):
    newseq= []
    dictt= {}
    covered= {}
    for idd in seq:
        if(idd in sampled):
            newseq.append(idd)
            if(idd in dictt):
                dictt[idd]+= 1
            else:
                dictt[idd]= 1
                covered[idd]= 0
    summ= 0
    for i in range(len(newseq)):
            summ+= 2*(dictt[newseq[i]] - covered[newseq[i]]) - 1
            covered[newseq[i]]+= 1
    print ("AMS for the Counter "+str(counters)+"  : "+ str(summ))
    SurpriseNo.append(sum(dictt.values()))


# In[6]:


def reservoir_sampling(Stream):
    global Buffer
    reservoir=[]
    uniqstream= np.unique(np.array(Stream))
    if(len(uniqstream)> 10000):
        for i in range(10000):
            reservoir.append(uniqstream[i])
        while(i < len(uniqstream)):
            j= random.randrange(i+1)
            if(j< 10000):
                reservoir[j]= uniqstream[i]
            i+= 1
    else:
        for idd in uniqstream:
            reservoir.append(idd)
#   Buffer.clear()
#   for hjk in reservoir:
#       Buffer.append(hjk)
#   print("Length of the Sampled(Unique) Stream: " +str(len(Buffer)))
    return reservoir


# In[10]:


def get_twitter_data():
    global Buffer
    global delay_sleep
    try:
        res=api.search("COVID OR Coronavirus OR coronavirus OR CORONAVIRUS OR COVID-19 OR COVID19 OR covid OR lockdown OR socialdistancing OR indiafightscorona OR quarantine OR WHO OR pandemic OR IndiaFightsCorona OR PMNRF OR pm-cares OR PM-CARES OR coronaupdatesinindia OR ICMR OR lockdownextension OR CoronaVirusUpdates OR ConstitutionOverCoronavirus OR stayathome OR coronaupdatesinindia OR Plandemic2020 OR ID2020 OR WuhanVirus OR Staywoke OR StayAtHome OR StayHomeSaveLives OR FightAgainstCOVID19 OR SAVELIVEHOUSE")
        stream=[]
        for i in res:
            record = ''
            record+=str(i.user.id_str)
            producer.send(topic_name,str.encode(record))
            Buffer.append(str(i.user.id_str))
        print("Length of the Stream: " +str(len(Buffer))+" "+str((time.time()-curr_timee)/60))#shoudl add more 15 each time!
        return True
    except tweepy.TweepError as e:
        print ("Some error!!")
        delay_sleep+=int(e.message[0]['code'].split(':')[1].strip())
        return False


# In[8]:
curr_timee=0
delay_sleep=0
def periodic_work(interval,count):
    global Buffer
    global curr_timee
    counter= 0
    while counter<count:
        print("Running for interval of: "+str(40) +".  Counter No.:  "+str(counter))
        Buffer.clear()
        curr_timee=time.time()
        delay_sleep=0
        while (time.time()-curr_timee)/60<interval+delay_sleep/60:
            get_twitter_data()
        sampled= reservoir_sampling(Buffer)     
        print("Length of the reservoir: " +str(len(sampled)))
        calculateAMS(Buffer, sampled, counter)
        counter+=1
    print("Surprise Numbers")
    print(SurpriseNo)


# In[ ]:


periodic_work(40,15)

with open('/home/ajkamal/Desktop/zzz/surprise40.pickle', 'wb') as f:
    pickle.dump(SurpriseNo, f)


# In[ ]:




