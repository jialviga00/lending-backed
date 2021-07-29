from flask_restful import Resource, Api
from flask import Flask, request
from flask_cors import CORS
from json import loads

app = Flask(__name__)
# CORS(app)
cors = CORS(
	app, 
	resources={r"/validate_amount/": {"origins": "http://localhost:3000"}}
)
api = Api(app)

class LendingApi(Resource):
	
	def head(self):
		return { "success": True }


	def post(self):

		data = loads(request.data.decode('UTF-8'))
		tax_id = data.get("taxId", False) # TODO
		business_name = data.get("businessName", False) # TODO
		requested_amount = int(data.get("requestedAmount", False))

		if requested_amount is False:
			return { "success": False, "error": "Requested amount UNDEFINED" }
		if requested_amount < 50000:
			return { "success": True, "status": "Declined" }
		elif requested_amount > 50000:
			return { "success": True, "status": "Approved" }
		else:
			return { "success": True, "status": "Undecided" }

api.add_resource(LendingApi, '/validate_amount/')

if __name__ == '__main__':
	app.run()