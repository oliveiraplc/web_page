# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:00:15 2020

@author: User
"""

from flask import Flask,render_template, url_for,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')    

# @app.route('/index.html')
# def index():
#     return render_template('index.html')    
    
# @app.route('/about.html')
# def about():
#     return render_template('about.html')    
    
# @app.route('/works.html')
# def works():
#     return render_template('works.html')    

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')    

# @app.route('/components.html')
# def components():
#     return render_template('components.html')    

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)    

def write_file(data):
    with open('database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\n {email},{subject},{message}')

def write_csv(data):
    with open('database.csv','a',newline='\n') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def subimt_form():
    if request.method == 'POST':
        try:
            data=request.form.to_dict()
            print(data)
            write_csv(data)
            return redirect('/thank.html')
        except:
            return 'something wrong'
    else:
        return 'No can\'t do'






















































