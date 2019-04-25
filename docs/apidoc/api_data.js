define({ "api": [
  {
    "type": "get",
    "url": "/api/data",
    "title": "获取领域",
    "version": "0.1.1",
    "name": "GetData",
    "group": "General",
    "description": "<p>获取所有可查看的领域</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "List",
            "optional": false,
            "field": "list",
            "description": "<p>可查看的领域的列表</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n[\n    \"大数据\",\n    \"人工智能\",\n    \"自动驾驶\",\n    \"区块链\",\n    \"计算机视觉\",\n    \"数据挖掘\",\n    \"数据建模\",\n    \"深度学习\",\n    \"图数据库\",\n    \"物联网\"\n]",
          "type": "json"
        }
      ]
    },
    "filename": "backend/app/views.py",
    "groupTitle": "General",
    "sampleRequest": [
      {
        "url": "http://localhost:80/api/data"
      }
    ]
  },
  {
    "type": "post",
    "url": "/api/data",
    "title": "获取热度",
    "version": "0.1.1",
    "name": "PostData",
    "group": "General",
    "description": "<p>获取指定领域的关键词和热度信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "title",
            "description": "<p>领域名</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "List",
            "optional": false,
            "field": "list",
            "description": "<p>查询的领域的热度列表</p>"
          },
          {
            "group": "Success 200",
            "type": "List",
            "optional": false,
            "field": "list.item",
            "description": "<p>热度列表中的每一项，即一个小列表</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "list.item[0]",
            "description": "<p>关键词名</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "list.item[1]",
            "description": "<p>关键词热度值</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n[\n    [\n        \"cloud computing\",\n        267\n    ],\n    ...\n    [\n        \"world wide web\",\n        6\n    ]\n]",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>无效请求</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 400 BAD REQUEST\n{\n    <!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\">\n    <title>400 Bad Request</title>\n    <h1>Bad Request</h1>\n    <p>The browser (or proxy) sent a request that this server could not understand.</p>\n}",
          "type": "json"
        }
      ]
    },
    "filename": "backend/app/views.py",
    "groupTitle": "General",
    "sampleRequest": [
      {
        "url": "http://localhost:80/api/data"
      }
    ]
  },
  {
    "type": "post",
    "url": "/api/graphdata",
    "title": "获取年份-热度数据",
    "version": "0.1.1",
    "name": "PostGraphData",
    "group": "General",
    "description": "<p>获取指定领域的年份-热度信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "title",
            "description": "<p>领域名</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "List",
            "optional": false,
            "field": "labels",
            "description": "<p>年份列表</p>"
          },
          {
            "group": "Success 200",
            "type": "List",
            "optional": false,
            "field": "datasets",
            "description": "<p>图表信息列表</p>"
          },
          {
            "group": "Success 200",
            "type": "Dict",
            "optional": false,
            "field": "datasets.item",
            "description": "<p>图表信息</p>"
          },
          {
            "group": "Success 200",
            "type": "Color",
            "optional": false,
            "field": "datasets.item.backgroundColor",
            "description": "<p>线条填充颜色</p>"
          },
          {
            "group": "Success 200",
            "type": "Color",
            "optional": false,
            "field": "datasets.item.borderColor",
            "description": "<p>线条颜色</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "datasets.item.borderWidth",
            "description": "<p>线宽（以像素为单位）</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "datasets.item.cubicInterpolationMode",
            "description": "<p>插值模式</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "datasets.item.fill",
            "description": "<p>如何填补线下的区域</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "datasets.item.label",
            "description": "<p>数据集的标签</p>"
          },
          {
            "group": "Success 200",
            "type": "Color",
            "optional": false,
            "field": "datasets.item.pointStrokeColor",
            "description": "<p>背景点击颜色</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "datasets.item.pointStyle",
            "description": "<p>点样式</p>"
          },
          {
            "group": "Success 200",
            "type": "Bool",
            "optional": false,
            "field": "datasets.item.spanGaps",
            "description": "<p>是否填充空数据点</p>"
          },
          {
            "group": "Success 200",
            "type": "List",
            "optional": false,
            "field": "datasets.item.data",
            "description": "<p>数据列表</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "datasets.item.data.item",
            "description": "<p>热度数据</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"labels\": [\n        \"2000\",\n        ...\n        \"2017\"\n    ],\n    \"datasets\": [\n        {\n            \"backgroundColor\": \"rgba(190, 25, 51, 1.0)\",\n            \"borderColor\": \"rgba(190, 25, 51, 1.0)\",\n            \"borderWidth\": 1,\n            \"cubicInterpolationMode\": \"monotone\",\n            \"data\": [\n                0,\n                ...\n                4\n            ],\n            \"fill\": \"false\",\n            \"label\": \"cloud computing\",\n            \"pointStrokeColor\": \"#fff\",\n            \"pointStyle\": \"circle\",\n            \"spanGaps\": \"true\"\n        },\n        ...\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>无效请求</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 400 BAD REQUEST\n{\n    <!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\">\n    <title>400 Bad Request</title>\n    <h1>Bad Request</h1>\n    <p>The browser (or proxy) sent a request that this server could not understand.</p>\n}",
          "type": "json"
        }
      ]
    },
    "filename": "backend/app/views.py",
    "groupTitle": "General",
    "sampleRequest": [
      {
        "url": "http://localhost:80/api/graphdata"
      }
    ]
  },
  {
    "type": "post",
    "url": "/api/trenddata",
    "title": "获取技术成熟度数据",
    "version": "0.1.1",
    "name": "PostTrendData",
    "group": "General",
    "description": "<p>获取指定领域的技术成熟度信息</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "title",
            "description": "<p>领域名</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "List",
            "optional": false,
            "field": "labels",
            "description": "<p>X轴坐标</p>"
          },
          {
            "group": "Success 200",
            "type": "List",
            "optional": false,
            "field": "datasets",
            "description": "<p>图表信息列表</p>"
          },
          {
            "group": "Success 200",
            "type": "Dict",
            "optional": false,
            "field": "datasets.item",
            "description": "<p>图表信息</p>"
          },
          {
            "group": "Success 200",
            "type": "Color",
            "optional": false,
            "field": "datasets.item.backgroundColor",
            "description": "<p>线条填充颜色</p>"
          },
          {
            "group": "Success 200",
            "type": "Color",
            "optional": false,
            "field": "datasets.item.borderColor",
            "description": "<p>线条颜色</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "datasets.item.borderWidth",
            "description": "<p>线宽（以像素为单位）</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "datasets.item.cubicInterpolationMode",
            "description": "<p>插值模式</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "datasets.item.fill",
            "description": "<p>如何填补线下的区域</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "datasets.item.label",
            "description": "<p>数据集的标签</p>"
          },
          {
            "group": "Success 200",
            "type": "Color",
            "optional": false,
            "field": "datasets.item.pointRadius",
            "description": "<p>点半径</p>"
          },
          {
            "group": "Success 200",
            "type": "Color",
            "optional": false,
            "field": "datasets.item.pointStrokeColor",
            "description": "<p>背景点击颜色</p>"
          },
          {
            "group": "Success 200",
            "type": "Bool",
            "optional": false,
            "field": "datasets.item.spanGaps",
            "description": "<p>是否填充空数据点</p>"
          },
          {
            "group": "Success 200",
            "type": "List",
            "optional": false,
            "field": "datasets.item.data",
            "description": "<p>数据列表</p>"
          },
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "datasets.item.data.item",
            "description": "<p>热度数据</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"labels\": [\n        0,\n        0.0016339869281045752,\n        ...\n        0.9983660130718954,\n        1\n    ],\n    \"datasets\": [\n        {\n            \"backgroundColor\": \"rgba(186, 114, 2, 1.0)\",\n            \"borderColor\": \"rgba(186, 114, 2, 1.0)\",\n            \"borderWidth\": 1,\n            \"cubicInterpolationMode\": \"default\",\n            \"data\": [\n                {\n                    \"x\": 0,\n                    \"y\": 0\n                },\n                ...\n                {\n                    \"x\": 1,\n                    \"y\": 0.6449044585987261\n                }\n            ],\n            \"fill\": \"false\",\n            \"label\": \"技术成熟度曲线\",\n            \"pointRadius\": 0,\n            \"pointStrokeColor\": \"#fff\",\n            \"spanGaps\": \"true\"\n        },\n        ...\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "optional": false,
            "field": "BadRequest",
            "description": "<p>无效请求</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 400 BAD REQUEST\n{\n    <!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\">\n    <title>400 Bad Request</title>\n    <h1>Bad Request</h1>\n    <p>The browser (or proxy) sent a request that this server could not understand.</p>\n}",
          "type": "json"
        }
      ]
    },
    "filename": "backend/app/views.py",
    "groupTitle": "General",
    "sampleRequest": [
      {
        "url": "http://localhost:80/api/trenddata"
      }
    ]
  }
] });
