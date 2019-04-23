# -*- coding: UTF-8 -*-
from flask import *
from app import app, cache

@app.route('/data', methods = ["GET"])
def get_data():
    ret = []
    for item in cache.keys():
        ret.append(item)
    return jsonify(ret)

@app.route('/data', methods = ["POST"])
def post_data():
    data = json.loads(request.get_data())

    heat = {}
    for key,value in cache[data["title"]].items():
        list = []
        list.extend(value.values())
        sum = 0
        for num in list:
            sum += num
        heat[key] = (sum, list)

    heat = sorted(heat.items(), key = lambda v : v[1][0], reverse = True)
    return jsonify(heat)

'''heat = {}
for key,value in data.items():
    list = []
    list.extend(value.values())
    sum = 0
    for num in list:
        sum += num
    heat[key] = (sum, list)

heat = sorted(heat.items(), key = lambda v : v[1][0], reverse = True)
print (heat)
for i in range(20):
    print (i, heat[i][0])
    hype_cycle_scatter(heat[i][1][1], heat[i][0], i)
show_hype_cycle()'''

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")
