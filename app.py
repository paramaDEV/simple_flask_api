from flask import *
from Models.Studio import *
from connection import Base, session

app = Flask(__name__)

@app.errorhandler(404) 
def error404Handler(e) :
    return make_response(jsonify({'message':'not found','status':404}),404)


@app.route("/")
def root() :
    return render_template('home.html')

@app.route("/docs",methods=['GET'])
def docs() : 
    return render_template('docs.html')

@app.route("/studios")
def studios() : 
    return StudioModel.displayStudio()

# # Open connection to database (unused)
# try :
#     connection = conn.connect_to_db()
#     print('Connection success')
# except :
#     print('Connection failed')

# def test() :

