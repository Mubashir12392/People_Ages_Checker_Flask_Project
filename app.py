from flask import Flask, render_template, redirect, request
from functions import youngest, oldest
app = Flask(__name__)

@app.route('/age_checker', methods=["GET", "POST"])
def age_checker():
    
    #when request method is get, it will show a form page
    if request.method == "GET":
        return render_template('age_checker.html')
    
    #when request method is post, data will calaculte by following methods
    elif request.method == "POST":
        first = request.form['1st_person']
        second = request.form['2nd_person']
        third = request.form['3rd_person']
        young = None
        old = None
        if ((first < second and first < third) and (first != second and first != third)):
            young = first
        elif ((second < first and second < third) and (second != first and second != third)):
            young = second
        else:
            young = third
        
        if ((first > second and first > third) and (first != second and first != third)):
            old = first
        elif ((second > first and second > third) and (second != first and second != third)):
            old = second
        else:
            old = third
        #at the end the result will show on html file
        return render_template("result.html", young= young, old= old)

        
