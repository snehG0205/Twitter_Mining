from flask import Flask, render_template, request
from test import mining
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('hello.html')


@app.route('/', methods=['GET', 'POST'])
def submit():
	if request.method == 'POST':
		print (request.form) # debug line, see data printed below
		tag = request.form['tag']
		limit = request.form['limit']
		# msg = tag+" "+limit
		sen_list = mining(tag,limit)
		msg = "Positive Percent = "+sen_list[0]+"% <br>Negative Percent = "+sen_list[1]+"% <br>Neutral Percent = "+sen_list[2]+"%"
	return ""+msg

if __name__ == '__main__':
   app.run(debug = True)

print("This")