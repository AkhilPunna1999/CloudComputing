# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request
import csv


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

file = open('Classification_results_1000.csv')
type(file)
csvreader = csv.reader(file)
results={}

for row in csvreader:
    results[row[0]]=row[1]

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

@app.route('/', methods=['GET'])
def hello():
	return 'Hi'
@app.route('/', methods=['POST'])
# ‘/’ URL is bound with hello_world() function.
def classification():
	file = request.files['inputFile']
	Name=file.filename.split(".")[0]
	print(Name)
	return Name+":"+results[Name],200
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run(host='127.0.0.1', port=3000)
