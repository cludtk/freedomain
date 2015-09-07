import json
from flask import Flask, render_template, redirect, url_for, Response
import time
from pip._vendor import requests
from constants import *
from csc import CSC
from tkmodel import Domain_model

app = Flask(__name__)

fcsc = CSC(alphabet)
currentCSC = '0'

def getDifTime(s):
    current_milli_time2 = lambda: int(round(time.time() * 1000))
    endTime = current_milli_time2()
    return float(endTime - s) / 1000

@app.route('/')
def index():
    return redirect('/0')

@app.route('/<count>')
def freedomain(count):

    array = []
    i = 0
    localCSC = count
    while 1:
        if i == 10000:
            break
        localCSC = fcsc.increment(localCSC)
        array.append(localCSC)
        i +=1

    return render_template('index2.html', arr=array, next=array[len(array)-1])

@app.route('/ck/<domain>')
def checkdomain(domain):

    domain = {'domain': domain, 'tld': ''}
    req = requests.post('https://my.freenom.com/includes/domains/fn-available.php', domain)
    res = Response(req)
    json_dict = json.loads(res.data)

    tkmodel = Domain_model(json_dict)

    return render_template('domains2.html', free=tkmodel.free_domains, paid=tkmodel.paid_domains)



if __name__ == '__main__':
    app_debug = True
    if not app_debug:
        app.run(host="172.31.27.41", port=80)
    else:
        app.run()