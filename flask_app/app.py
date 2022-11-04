from flask import Flask, request, render_template
app = Flask(__name__)
import pickle

@app.route('/ml', methods=['POST'])
def pred():
    x = request.form
    data = []
    for key, val in request.form.items():
        data.append(int(val))  
    try:
        model = pickle.load(open('/usr/data/dtree.sav', 'rb'))
    except:
        # For debugging
        model = pickle.load(open('../storage/dtree.sav', 'rb'))
    pred = model.predict([data])
    return f"Age of Abalone {pred}"

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')