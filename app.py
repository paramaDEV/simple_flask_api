from flask import *
from controllers.StudioController import StudioController
from connection import Base, session, db, conn_str

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = conn_str
# db.init_app(app)

@app.errorhandler(404) 
def error404Handler(e) :
    return make_response(jsonify({'message':'not found','status':404}),404)


@app.route("/")
def root() :
    return render_template('home.html')

@app.route("/docs",methods=['GET'])
def docs() : 
    return render_template('docs.html')

@app.route("/studios",methods=['GET'])
def studios() : 
   result = StudioController.displayStudio(0)
   return result

@app.route("/studio/<id>",methods=['GET'])
def studio(id) : 
   result = StudioController.displayStudio(id)
   return result

@app.route("/studio/add/",methods=['POST'])
def insertStudio() : 
    param = {
        'name' : request.form['name'],
        'capacity' : request.form['capacity'],
        'status' : request.form['status'],
        'cinema_id' : request.form['cinema_id']
    }
    StudioController.insertStudio(param)
    return make_response(jsonify({'message':'data created successfully','status':200}),200)




