from flask import Flask
from flask_restplus import Resource, Api

app = Flask("potassium-meet-teams")

@app.route('/test')
@api.doc(params={})
class TestApp(Resource):
	def get():
return 'Hello, World!'

if __name__ == "__main__":
	app.run(host=HOSTNAME, debug=True)