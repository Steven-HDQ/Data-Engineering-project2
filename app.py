from flask import Flask, request, render_template
from redis import Redis, RedisError, StrictRedis
import pandas as pd
import random
import time
from gensim.models import Doc2Vec
from prometheus_client import start_http_server
from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Summary
from prometheus_client import Histogram

model = Doc2Vec.load("doc2vec.model")
data  = pd.read_csv('Tweet_Processed.csv')

REQUESTS = Counter('Lab2_requests_total', 'How many times the app has been accessed')
EXCEPTIONS = Counter('Lab2_exceptions_total', 'How many times the app issued an exception')

INPROGRESS = Gauge('Lab2_inprogress_gauge', 'How many requests to app are currently in progress')
LAST = Gauge('Lab2_last_accessed_gauge', 'When was the app last accessed')

LATENCY = Summary('Lab2_latency_seconds', 'Time needed for a request')
LATENCY_HIS = Histogram('Lab2_latency_histogram_seconds', 'Time needed for a request',buckets=[0.0001, 0.0002, 0.0005, 0.001, 0.01, 0.1, 1.0, 1.5, 2.0, 3.0])

app = Flask(__name__)

def search_silimar(text):
	tweet=list(data['ori_tweet'])
	test_text=text.split(' ')
	inferred_vector=model.infer_vector(doc_words=test_text,alpha=0.025,steps=500)
	results=model.docvecs.most_similar([inferred_vector],topn=20)
	res=[]
	for index,sim in results:
		sim=round(sim*100,2)
		words = tweet[index]
		sentence=''
		for word in words:
			sentence += word
		res.append((sim,sentence))
	INPROGRESS.dec()
	return res

@app.route('/', methods=['GET', 'POST'])
def index():
	REQUESTS.inc()
	#with EXCEPTIONS.count_exceptions():
	#	if random.random() < 0.2:
	#		raise Exception

	LAST.set(time.time())
	INPROGRESS.inc()
	start = time.time()
	rand = random.random()
	if rand < 0.5 :
		time.sleep(0.1 * rand)
	text=''
	result=''
	head=''
	if request.method == 'POST':
		text = request.form['text']
		if text=='':
			pass
		else:
			result = search_silimar(text)
			head='Similar Tweets:'
		return render_template('index.html',text=text,result=result,head=head)
	INPROGRESS.dec()
	LATENCY.observe(time.time() - start)
	LATENCY_HIS.observe(time.time() - start)
	return render_template('index.html',text=text,result=result,head=head)

if __name__ == '__main__':
	start_http_server(8010)
	redis_client = StrictRedis(host='redis', port=6379)
	app.run(host='0.0.0.0')
	
	
	
	
