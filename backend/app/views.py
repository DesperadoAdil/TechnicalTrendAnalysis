# -*- coding: UTF-8 -*-
from flask import *
from app import app, cache
from .utils import TITLELIST

import random

@app.before_first_request
def first_request():
    print ("first_request")
    heat = {}
    for title in TITLELIST:
        heat[title] = {}
        for key,value in cache[title].items():
            sum = 0
            for num in value.values():
                sum += num
            heat[title][key] = sum
        heat[title] = sorted(heat[title].items(), key = lambda v : v[1], reverse = True)
    session['heat'] = heat


@app.route('/data', methods = ["GET"])
def get_data():
    ret = []
    for item in cache.keys():
        ret.append(item)
    return jsonify(ret)


@app.route('/data', methods = ["POST"])
def post_data():
    try:
        data = json.loads(request.get_data())
    except:
        abort(400)

    if "heat" in session:
        ret = session.get("heat")[data["title"]]
    else:
        first_request()
        ret = session.get("heat")[data["title"]]

    return jsonify(ret)


@app.route('/graphdata', methods = ["POST"])
def graph_data():
    try:
        data = json.loads(request.get_data())
    except:
        abort(400)

    ret = {}
    labels = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"]
    datasets = []

    if "heat" in session:
        heat = session.get("heat")[data["title"]]
    else:
        first_request()
        heat = session.get("heat")[data["title"]]

    for i in range(10):
        dataset = {}
        dataset['label'] = heat[i][0]
        r = random.randint(0, 256)
        g = random.randint(0, 256)
        b = random.randint(0, 256)
        dataset['borderColor'] = 'rgba(%s, %s, %s, %s)' % (r, g, b, 1.0)
        dataset['backgroundColor'] = 'rgba(%s, %s, %s, %s)' % (r, g, b, 1.0)
        dataset['borderWidth'] = 1
        dataset['pointStrokeColor'] = "#fff"
        dataset['pointStyle'] = "circle"
        dataset['cubicInterpolationMode'] = "monotone"
        dataset['spanGaps'] = "true"
        dataset['fill'] = "false"
        dataset['data'] = []
        for item in labels:
            if item in cache[data["title"]][heat[i][0]]:
                dataset['data'].append(cache[data["title"]][heat[i][0]][item])
            else:
                dataset['data'].append(0)
        datasets.append(dataset)
        '''ret[i] = {}
        ret[i]["name"] = heat[i][0]
        ret[i]["data"] = dataset['data']'''

    ret['labels'] = labels
    ret['datasets'] = datasets

    return jsonify(ret)


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
