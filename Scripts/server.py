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

<<<<<<< HEAD
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

worker.setTicker('GOOG')
worker.setDate('2020-08-21')
worker.setFlag('Calls')
worker.setType('Credit')
@app.route('/api/spread/basic_spreads', methods=['GET'])
def getBasicSpread():
	try:
		# worker.setTicker(request.form['Stock'])
		# worker.setDate(request.form['selectDate'])
		# worker.setFlag(request.form['selectFlag'])
		# worker.setType(request.form['selectType'])
		worker.getBasicSpread()
		return worker.best_ratio
	except:
		return jsonify({'status': 501})
=======
@app.route('/api/spread/basic_spreads', methods=['POST'])
def getBasicSpread():
    try:
        data = request.json
        worker.setTicker(data['Stock'])
        worker.setDate(data['selectDate'])
        worker.setFlag(data['selectFlag'])
        worker.setType(data['selectType'])
        worker.getBasicSpread()
        return jsonify(worker.best_ratio)
    except Exception as e:
        return jsonify({'status': 501, 'exception': e})
>>>>>>> a97310a8f2a075cdd5dcfa4f207feba7e6a8bd33



app.run(debug=True, port=7500)
