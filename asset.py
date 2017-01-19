from flask import Flask, render_template, request, url_for, jsonify 
from myngram import ngram_hemal1

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello', methods=['POST'])
def hello():
    name=request.form['yourname']
    cap_name = name.upper()
    email=request.form['youremail']
    textentered=request.form['description']
    tokens=ngram_hemal1(textentered)
    return render_template('form_action.html', name=cap_name, email=email, description=tokens)


@app.route('/technology')
def get_records():
    list = [ {
          
          "tag": "java"				     ,  "weight": 2,
          "tag": "python"			     ,  "weight": 12,
          "tag": "object oriented" ,  "weight": 22,
          "tag": "c#"				       ,  "weight": 32,
          
        	 },
          ]
    return jsonify(results = list)

# Run the app :)
if __name__ == '__main__':
  app.run(debug=True)