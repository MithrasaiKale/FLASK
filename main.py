from flask import Flask, jsonify, request

app=Flask(__name__)

mytask=[
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    }, 
    {
        'id': 2,
        'title': u'Buy randoms stuff from the market',
        'description': u'IceCream, newComputer', 
        'done': False
    }
]
@app.route("/")
def welcome():
    return "Do your work and buy things."

@app.route("/addData", methods=["POST"] )
def add_data():
    if not request.json:
        return jsonify({
            "status":"error","message":"please provide the data"
        },400)
    t={
      'id': mytask[-1]['id'] + 1,
       "title":request.json["title"],
       "description":request.json.get("description", ""),
       "done":False     
    }
    mytask.append(t)
    return jsonify({
        "status":"success","message":"Task added successfully"

    })
@app.route("/getdata")
def gettingData():
    return jsonify({
        "data":mytask
    })

if(__name__ == "__main__"):
     app.run(debug = True)
