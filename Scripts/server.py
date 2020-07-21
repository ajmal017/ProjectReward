from flask import Flask, request, jsonify
from PRApurv import ProjectRewarder
from flask_cors import CORS

worker = ProjectRewarder(None, None, None, None)

app = Flask(__name__)
cors = CORS(app)

print("CORRECT")

'''
    ./ngrok http 7500
    curl -X POST -d "ticker=GOOG,date=2020-08-21,flag=calls,spread_type=credit" localhost:7500/api/set_ticker
    curl -X POST -d "date=2020-08-21" localhost:7500/api/set_date
    curl -X POST -d "flag=calls" localhost:7500/api/set_flag
    curl -X POST -d "spread_type=credit" localhost:7500/api/set_type
    curl -X POST -d "Stock=GOOG" localhost:7500/api/spread/basic_spreads

'''

# @app.route('/api/set_ticker', methods=['POST'])
# def setTicker():
#     #when passing in variables to a flask method, check request.args, request.form, and request.json
#     response = worker.setTicker(request.form['ticker'])
#     print(worker)
#     return jsonify(response)

# @app.route('/api/set_date', methods=['POST'])
# def setDate():
# 	response = worker.setDate(request.form['date'])
# 	print(worker)
# 	return jsonify(response)
# @app.route('/api/set_flag', methods=['POST'])
# def setFlag():
# 	response = worker.setFlag(request.form['flag'])
# 	print(worker)
# 	return jsonify(response)
# @app.route('/api/set_type', methods=['POST'])
# def setType():
# 	response = worker.setType(request.form['spread_type'])
# 	print(worker)
# 	return jsonify(response)
# @app.route('/api/spread/basic_spreads', methods=['GET'])
# def getSpread():
# 	worker.getBasicSpread()
# 	return jsonify(worker.best_ratio)
@app.route('/api/spread/basic_spreads', methods=['POST'])
def getBasicSpread():
    try:
        data = request.json
        print(data)
        worker.setTicker(data['Stock'])
        worker.setDate(data['selectDate'])
        worker.setFlag(data['selectFlag'])
        worker.setType(data['selectType'])
        print(worker)
        worker.getBasicSpread()
        return jsonify(worker.best_ratio)
    except Exception as e:
        return jsonify({'status': 501, 'exception': e})



app.run(debug=True, port=7500)
