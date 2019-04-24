# -*- coding: UTF-8 -*-
from flask import *
from app import app, cache
from .utils import TITLELIST
from .hype_cycle import load_hype_cycle, get_pos

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


"""
@api {get} /api/data 获取领域
@apiVersion 0.1.1
@apiName GetData
@apiGroup General
@apiDescription 获取所有可查看的领域

@apiSuccess {List} list 可查看的领域的列表
@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    [
        "大数据",
        "人工智能",
        "自动驾驶",
        "区块链",
        "计算机视觉",
        "数据挖掘",
        "数据建模",
        "深度学习",
        "图数据库",
        "物联网"
    ]
"""
@app.route('/api/data', methods = ["GET"])
@app.route('/data', methods = ["GET"])
def get_data():
    ret = []
    for item in cache.keys():
        if item != "pos":
            ret.append(item)
    return jsonify(ret)


"""
@api {post} /api/data 获取热度
@apiVersion 0.1.1
@apiName PostData
@apiGroup General
@apiDescription 获取指定领域的关键词和热度信息

@apiParam {String} title 领域名

@apiSuccess {List} list 查询的领域的热度列表
@apiSuccess {List} list.item 热度列表中的每一项，即一个小列表
@apiSuccess {String} list.item[0] 关键词名
@apiSuccess {Integer} list.item[1] 关键词热度值
@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    [
        [
            "cloud computing",
            267
        ],
        ...
        [
            "world wide web",
            6
        ]
    ]

@apiError BadRequest 无效请求
@apiErrorExample {json} Error-Response:
    HTTP/1.1 400 BAD REQUEST
    {
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>400 Bad Request</title>
        <h1>Bad Request</h1>
        <p>The browser (or proxy) sent a request that this server could not understand.</p>
    }
"""
@app.route('/api/data', methods = ["POST"])
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


"""
@api {post} /api/graphdata 获取年份-热度数据
@apiVersion 0.1.1
@apiName PostGraphData
@apiGroup General
@apiDescription 获取指定领域的年份-热度信息

@apiParam {String} title 领域名

@apiSuccess {List} labels 年份列表
@apiSuccess {List} datasets 图表信息列表
@apiSuccess {Dict} datasets.item 图表信息
@apiSuccess {Color} datasets.item.backgroundColor 线条填充颜色
@apiSuccess {Color} datasets.item.borderColor 线条颜色
@apiSuccess {Integer} datasets.item.borderWidth 线宽（以像素为单位）
@apiSuccess {String} datasets.item.cubicInterpolationMode 插值模式
@apiSuccess {String} datasets.item.fill 如何填补线下的区域
@apiSuccess {String} datasets.item.label 数据集的标签
@apiSuccess {Color} datasets.item.pointStrokeColor 背景点击颜色
@apiSuccess {String} datasets.item.pointStyle 点样式
@apiSuccess {Bool} datasets.item.spanGaps 是否填充空数据点
@apiSuccess {List} datasets.item.data 数据列表
@apiSuccess {Integer} datasets.item.data.item 热度数据
@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "labels": [
            "2000",
            ...
            "2017"
        ],
        "datasets": [
            {
                "backgroundColor": "rgba(190, 25, 51, 1.0)",
                "borderColor": "rgba(190, 25, 51, 1.0)",
                "borderWidth": 1,
                "cubicInterpolationMode": "monotone",
                "data": [
                    0,
                    ...
                    4
                ],
                "fill": "false",
                "label": "cloud computing",
                "pointStrokeColor": "#fff",
                "pointStyle": "circle",
                "spanGaps": "true"
            },
            ...
        ]
    }

@apiError BadRequest 无效请求
@apiErrorExample {json} Error-Response:
    HTTP/1.1 400 BAD REQUEST
    {
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>400 Bad Request</title>
        <h1>Bad Request</h1>
        <p>The browser (or proxy) sent a request that this server could not understand.</p>
    }
"""
@app.route('/api/graphdata', methods = ["POST"])
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

    ret['labels'] = labels
    ret['datasets'] = datasets

    return jsonify(ret)


"""
@api {post} /api/trenddata 获取技术成熟度数据
@apiVersion 0.1.1
@apiName PostTrendData
@apiGroup General
@apiDescription 获取指定领域的技术成熟度信息

@apiParam {String} title 领域名

@apiSuccess {List} labels X轴坐标
@apiSuccess {List} datasets 图表信息列表
@apiSuccess {Dict} datasets.item 图表信息
@apiSuccess {Color} datasets.item.backgroundColor 线条填充颜色
@apiSuccess {Color} datasets.item.borderColor 线条颜色
@apiSuccess {Integer} datasets.item.borderWidth 线宽（以像素为单位）
@apiSuccess {String} datasets.item.cubicInterpolationMode 插值模式
@apiSuccess {String} datasets.item.fill 如何填补线下的区域
@apiSuccess {String} datasets.item.label 数据集的标签
@apiSuccess {Color} datasets.item.pointRadius 点半径
@apiSuccess {Color} datasets.item.pointStrokeColor 背景点击颜色
@apiSuccess {Bool} datasets.item.spanGaps 是否填充空数据点
@apiSuccess {List} datasets.item.data 数据列表
@apiSuccess {Integer} datasets.item.data.item 热度数据
@apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "labels": [
            0,
            0.0016339869281045752,
            ...
            0.9983660130718954,
            1
        ],
        "datasets": [
            {
                "backgroundColor": "rgba(186, 114, 2, 1.0)",
                "borderColor": "rgba(186, 114, 2, 1.0)",
                "borderWidth": 1,
                "cubicInterpolationMode": "default",
                "data": [
                    {
                        "x": 0,
                        "y": 0
                    },
                    ...
                    {
                        "x": 1,
                        "y": 0.6449044585987261
                    }
                ],
                "fill": "false",
                "label": "技术成熟度曲线",
                "pointRadius": 0,
                "pointStrokeColor": "#fff",
                "spanGaps": "true"
            },
            ...
        ]
    }

@apiError BadRequest 无效请求
@apiErrorExample {json} Error-Response:
    HTTP/1.1 400 BAD REQUEST
    {
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>400 Bad Request</title>
        <h1>Bad Request</h1>
        <p>The browser (or proxy) sent a request that this server could not understand.</p>
    }
"""
@app.route('/api/trenddata', methods = ["POST"])
@app.route('/trenddata', methods = ["POST"])
def trend():
    try:
        data = json.loads(request.get_data())
    except:
        abort(400)

    ret = {}
    labels = []
    datasets = []

    if "heat" in session:
        heat = session.get("heat")[data["title"]]
    else:
        first_request()
        heat = session.get("heat")[data["title"]]

    dataset = {}
    dataset['label'] = "技术成熟度曲线"
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    dataset['borderColor'] = 'rgba(%s, %s, %s, %s)' % (r, g, b, 1.0)
    dataset['backgroundColor'] = 'rgba(%s, %s, %s, %s)' % (r, g, b, 1.0)
    dataset['borderWidth'] = 1
    dataset['pointStrokeColor'] = "#fff"
    dataset['pointRadius'] = 0
    dataset['cubicInterpolationMode'] = "default"
    dataset['spanGaps'] = "true"
    dataset['fill'] = "false"
    dataset['data'] = []
    (X, Y) = load_hype_cycle()
    for i in range(len(X)):
        d = {}
        d['x'] = X[i]
        d['y'] = Y[i]
        labels.append(X[i])
        dataset['data'].append(d)
    datasets.append(dataset)

    for i in range(20):
        dataset = {}
        dataset['label'] = heat[i][0]
        r = random.randint(0, 256)
        g = random.randint(0, 256)
        b = random.randint(0, 256)
        dataset['borderColor'] = 'rgba(%s, %s, %s, %s)' % (r, g, b, 1.0)
        dataset['backgroundColor'] = 'rgba(%s, %s, %s, %s)' % (r, g, b, 1.0)
        dataset['borderWidth'] = 1
        dataset['pointStrokeColor'] = "#fff"
        dataset['pointRadius'] = 8
        dataset['pointStyle'] = "circle"
        dataset['cubicInterpolationMode'] = "monotone"
        dataset['spanGaps'] = "true"
        dataset['fill'] = "false"
        dataset['data'] = []
        d = cache['pos'][data["title"]][i]
        labels.append(d['x'])
        dataset['data'].append(d)
        datasets.append(dataset)

    ret['labels'] = sorted(labels)
    ret['datasets'] = datasets

    return jsonify(ret)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")
