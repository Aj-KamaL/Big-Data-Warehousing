Crawling the tweets with hashtag #Covid19, #Coronavirus and similar hashtags and create a sample of 10000 user-ids with reservoir sampling algorithm.

AMS algorithm to compute the surprise number.

The result is a graph of surprise number for posting behavior for different time intervals, i.e., 10 minutes, 20 minutes, 30 minutes, 40 minutes. For each interval say, 10 minutes, run your
experiment 15 times and report the average of the surprise numbers.

Replace the Twitter credentials before running the code in code.py.

bin/zookeeper-server-start.sh ./config/zookeeper.properties 
bin/kafka-server-start.sh ./config/server.properties
python3 2016076_2016260_BDA_Assgn_3.py
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic Coronavirus --from-beginning

