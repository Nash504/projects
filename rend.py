from flask import render_template,Flask;
app=Flask(__name__)

@app.route('/')
def home():
    name='python'
    return render_template('home.html',name=name)
if __name__=='__main__':
    app.run(debug=True)