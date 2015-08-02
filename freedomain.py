from flask import Flask, render_template
import time
from constants import *
from csc import CSC

app = Flask(__name__)

fcsc = CSC(alphabet)
currentCSC = '0'

def getDifTime(s):
    current_milli_time2 = lambda: int(round(time.time() * 1000))
    endTime = current_milli_time2()
    return float(endTime - s) / 1000

@app.route('/<count>')
def freedomain(count):
    test = fcsc.increment(str(count))

    currentCSC = fcsc.increment(currentCSC)
    return render_template('index.html', name=currentCSC)


if __name__ == '__main__':
    if not __debug__:
        app.run(host="172.31.27.41", port=8080)
    else:
        app.run()