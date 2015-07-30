from flask import Flask
import time

app = Flask(__name__)

alphabet = 'abcdefghijklmnopqrstuwxyz'
number = '1234567890'


def numbering_system():
    base_system = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result = {}
    for csc_n in base_system:
        result[csc_n] = base_system.find(csc_n)
    return result
ns = numbering_system()


def csc(sym):
    result = ''
    for s in sym:
        result += str(ns[s])
    return result


def r_csc(num):
    for key in numbering_system().keys():
        if ns[key] == int(num):
            return key
    return 'out_of_range'


def increment(csc_number):
    csc_len = len(csc_number)
    i = 0
    while 1:
        if i > csc_len:
            csc_number += '0'
        if i == csc_len:
            csc_number += '0'
            break

        num = csc_number[i]
        if num in ns.keys():
            csc_result = r_csc(int(csc(num))+1)
            if csc_result != 'out_of_range':
                csc_number = csc_number[:i] + csc_result + csc_number[i+1:]
                break
            else:
                csc_number = csc_number[:i] + '0' + csc_number[i+1:]
                i += 1
        else:
            csc_number = csc_number[:i] + '0' + csc_number[i+1:]
            i += 1
    return csc_number


def word_generator(csc_number):
    return 0


def getDifTime(s):
    current_milli_time2 = lambda: int(round(time.time() * 1000))
    endTime = current_milli_time2()
    return float(endTime - s) / 1000


@app.route('/<count>')
def freedomain(count):
    return 'TEST'


if __name__ == '__main__':
    app.run(host="172.31.27.41", port=8080)
    #app.run()