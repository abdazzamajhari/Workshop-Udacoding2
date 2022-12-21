from flask import Flask, request, render_template
from flask import jsonify
from model import model

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('home.html')

@app.route('/review', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        review = request.form
        for k, v in review.items():
            val = v
        print(val)

        result = model(val)
        print(result)

        ## API
        # res = {
            # "status":200, 
            # "msg":"ok", 
            # "input":val,
            # "predict":result[0]
            # }
        # return jsonify(res)

        return render_template('home.html', result = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
