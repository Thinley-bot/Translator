from flask import Flask,request,Response
from flask.templating import render_template
from googletrans import Translator

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        sentence=request.form.get('sentence')
        language=request.form.get('inputvalue')
        
        output=Translator().translate(sentence,dest=language)
    else:
        return render_template('index.html')
    
    return render_template('index.html',output=output,sentence=sentence)

if __name__=='__main__':
    app.run(debug=True)