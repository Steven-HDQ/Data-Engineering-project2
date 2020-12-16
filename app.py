from flask import Flask, request, render_template
from redis import Redis, RedisError, StrictRedis
import pandas as pd
from gensim.models import Doc2Vec

model = Doc2Vec.load("doc2vec.model")
data  = pd.read_csv('Tweet_Processed.csv')

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
	return res

@app.route('/', methods=['GET', 'POST'])
def index():
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
	return render_template('index.html',text=text,result=result,head=head)

if __name__ == '__main__':
	redis_client = StrictRedis(host='redis', port=6379)
	app.run(host='0.0.0.0')
	
	
	
	
