from flask import Flask,render_template,request
from flask_pymongo import PyMongo
import json
from bson import json_util
import random


app=Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost:27017/flaskdb'
mongo=PyMongo(app)

@app.route('/')   
def showquote():
    data=mongo.db.quotes.find()
    data=json.loads(json_util.dumps(data)) 

    # print(type(data))
    # print(data[1])
    # print(len(data))
    random_number = random.randint(0,len(data)-1)

    return render_template('index.html',data=data[random_number])
@app.route('/add',methods = ['POST', 'GET'])   
def addquote():
    if request.method == 'POST':
      print('Post method')
      #print(request.form['quote'])
      #print(request.form['quote'])
      quote = request.form['quote']
      auther = request.form['auther']
    #   print(quote,auther)
      new_quote={'quote':quote,'auther':auther}
      mongo.db.quotes.insert_one(new_quote)
    #   print(new_quote)
      return "data added"
    else:
        return render_template('add.html')

if __name__=="__main__":
    app.run(port=2500)