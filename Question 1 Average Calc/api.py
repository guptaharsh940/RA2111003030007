from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv()

url = os.getenv('URL')
token = os.getenv('AUTH_TOKEN')
# Defining header with bearer token
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}


@app.route('/numbers/e')
def even():
    
    durl = url+"even"
    l = []
    try:
        response = requests.get(durl, headers=headers, timeout=0.5)
        if response.status_code == 200:
            receivednums = response.json()['numbers']
            initial = l.copy()
            # Window size 10 so adding the numbers accordingly
            for i in receivednums:
                l.append(i)
                if (len(l) > 10):
                    l.pop(0)

            avg = sum(l)/len(l)
            response = {"numbers":receivednums,"windowPrevState":initial,"windowCurrState":l,"avg":avg}
            return jsonify(response)

        else:
            return jsonify({"Request failed with status code:": response.status_code})
    except requests.exceptions.Timeout:  
        return "Request timed out"
    

@app.route('/numbers/p')
def prime():
    
    durl = url+"primes"
    l = []
    try:
        response = requests.get(durl, headers=headers, timeout=0.5)
        if response.status_code == 200:
            receivednums = response.json()['numbers']
            initial = l.copy()
            # Window size 10 so adding the numbers accordingly
            for i in receivednums:
                l.append(i)
                if (len(l) > 10):
                    l.pop(0)

            avg = sum(l)/len(l)
            response = {"numbers":receivednums,"windowPrevState":initial,"windowCurrState":l,"avg":avg}
            return jsonify(response)

        else:
            return jsonify({"Request failed with status code:": response.status_code})
    except requests.exceptions.Timeout:  
        return "Request timed out"
    
@app.route('/numbers/f')
def fibo():
    
    durl = url+"fibo"
    l = []
    try:
        response = requests.get(durl, headers=headers, timeout=0.5)
        if response.status_code == 200:
            receivednums = response.json()['numbers']
            initial = l.copy()
            # Window size 10 so adding the numbers accordingly
            for i in receivednums:
                l.append(i)
                if (len(l) > 10):
                    l.pop(0)

            avg = sum(l)/len(l)
            response = {"numbers":receivednums,"windowPrevState":initial,"windowCurrState":l,"avg":avg}
            return jsonify(response)

        else:
            return jsonify({"Request failed with status code:": response.status_code})
    except requests.exceptions.Timeout:  
        return "Request timed out"
    

@app.route('/numbers/r')
def rand():
    
    durl = url+"rand"
    l = []
    try:
        response = requests.get(durl, headers=headers, timeout=0.5)
        if response.status_code == 200:
            receivednums = response.json()['numbers']
            initial = l.copy()
            # Window size 10 so adding the numbers accordingly
            for i in receivednums:
                l.append(i)
                if (len(l) > 10):
                    l.pop(0)

            avg = sum(l)/len(l)
            response = {"numbers":receivednums,"windowPrevState":initial,"windowCurrState":l,"avg":avg}
            return jsonify(response)

        else:
            return jsonify({"Request failed with status code:": response.status_code})
    except requests.exceptions.Timeout:  
        return "Request timed out"


if __name__ == '__main__':
    app.run(port=9876)
