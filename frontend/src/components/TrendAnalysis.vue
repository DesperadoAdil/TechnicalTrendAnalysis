<template>
  <div class="layout">
    <Menu mode="horizontal" theme="dark" active-key="1">
      <div class="layout-nav">
        <Menu-item v-for="title in titleList" :key="title" name="" @click.native="getdata(title)">
          <Icon type="ios-checkmark"></Icon>
          {{ title }}
        </Menu-item>
      </div>
    </Menu>
    <br>
    <h1>{{ title }}</h1>
    <Row>
      <i-col span="6">
        <h2>热点关键词，共{{ msg }}条</h2>
      </i-col>
      <i-col span="18">
      </i-col>
    </Row>
    <div class="layout-content">
      <Row>
        <i-col span="6">
          <h6 v-for="data in dataList">
            {{ data.name }}
            <li>热度：</li>
            {{ data.time }}
          </h6>
        </i-col>
        <i-col span="18">
          <canvas id="myChart"></canvas><br>
          <canvas id="myChart2"></canvas>
        </i-col>
      </Row>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js';
export default {
  name: 'TrendAnalysis',
  data () {
    return {
      msg : 0,
      title : '',
      titleList : [],
      dataList : [
        {
          name : '',
          time : ''
        }
      ],
    }
  },
  mounted () {
    this.gettitle()
  },
  methods: {
    gettitle () {
      this.titleList = []
      this.$http.get('/api/data').then(res => {
        for (var i = 0; i < res.data.length; i++) {
          this.titleList.push(res.data[i])
        }
        this.getdata(res.data[0])
      }).catch(err => {
        console.log(err)
        return null
      })
    },
    getdata (title) {
      this.dataList = []
      let data = {
        "title" : title
      }
      this.getgraph(data)
      this.gettrend(data)
      this.$http.post('/api/data', data).then(res => {
        this.msg = res.data.length
        for (var i = 0; i < this.msg; i++) {
          this.dataList.push({
            'name' : res.data[i][0],
            'time' : res.data[i][1],
          })
        }
        this.title = title
      }).catch(err => {
        console.log(err)
      })
    },
    getgraph (data) {
      var c = document.getElementById("myChart")
      var ctx = c.getContext("2d")
      ctx.clearRect(0, 0, c.width, c.height)
      ctx.beginPath()

      this.$http.post('/api/graphdata', data).then(res => {
        var myChart = new Chart(ctx, {
          type: "line",
          data: res.data,
          options: {
            events : ['click'],
            title : {
              display: true,
              text: '热度图'
            }
          }
        });
      })
    },
    gettrend (data) {
      var c = document.getElementById("myChart2")
      var ctx = c.getContext("2d")
      ctx.clearRect(0, 0, c.width, c.height)
      ctx.beginPath()

      this.$http.post('/api/trenddata', data).then(res => {
        var myChart = new Chart(ctx, {
          type: "line",
          data: res.data,
          options: {
            events : ['click'],
            elements: {
              line: {
                tension: 0 // disables bezier curves
              }
            },
            scales: {
              xAxes: [{
                ticks: {
                  beginAtZero: true,
                  max: 1,
                  min: 0
                }
              }],
              yAxes: [{
                ticks: {
                  beginAtZero: true,
                  max: 1,
                  min: 0
                }
              }]
            }
          }
        });
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .layout{
        border: 1px solid #d7dde4;
        background: #f5f7f9;
    }
    .layout-nav{
        margin: 0 auto;
    }
    .layout-content{
        min-height: 200px;
        margin: 15px;
        overflow: hidden;
        background: #f5f7f9;
        border-radius: 4px;
    }
    .layout-content-main{
        padding: 10px;
    }
    .layout-copy{
        text-align: center;
        padding: 10px 0 20px;
        color: #9ea7b4;
    }
h1, h2 {
  font-weight: normal;
}
h6.hidden {
  visibility:hidden;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
