from flask import Flask,render_template,redirect,request,url_for,flash
import pandas as pd
from datetime import datetime
import requests
from .modules.mailing import mail_sender as mail

urlList = ["https://www.google.com","https://github.com/bleh_blu_bleh"]
mailing_list = ["example@gmail.com"]

app = Flask(__name__)

@app.route("/", methods=["GET"])
def url_checker():
    statusArray = []
    for url in urlList:
        urlDict = {
            "url" : url,
            "last_checked" : datetime.now().strftime("%H:%M:%S"),
        }
        response = requests.get(url)
        if(response.status_code == 200):
            urlDict["code_color"] = 1
        else:
            urlDict["code_color"] = 0
        statusArray.append(urlDict)
    mailing_attachment = pd.DataFrame(statusArray).to_string()
    for mailID in mailing_list:
        mail(mailID,mailing_attachment)
    return render_template("home.html",statusArray=statusArray)

@app.route('/addUrl',methods = ['GET','POST'])
def addUrl():
    if request.method == 'POST' :
        url = request.form['url']
        if(url not in urlList):
            urlList.append(url)
    urlList.sort()
    return redirect(url_for('url_checker'))


if __name__ == "__main__":
    app.run(debug=True)

