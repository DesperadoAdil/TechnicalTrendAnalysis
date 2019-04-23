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
          <canvas id="myChart2"></canvas>
          <h6 v-for="data in dataList">
            <li>序列：</li>
            {{ data.list }}
          </h6>
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
          time : '',
          list : ''
        }
      ],
    }
  },
  mounted () {
    this.gettitle()

    var ctx2 = document.getElementById("myChart2");

    var myChart2 = new Chart(ctx2, {
            type: "line",
            data: {
                labels: ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"],
                datasets: [
                    {
                        label: "热度图",
                        backgroundColor: "rgba(225,10,10,0.3)",
                        borderColor: "rgba(225,103,110,1)",
                        borderWidth: 1,
                        pointStrokeColor: "#fff",
                        pointStyle: "crossRot",
                        data: [65, 59, 0, 81, 56, 10, 40, 22, 32, 54, 10, 30, 34, 54, 67, 76, 52, 27],
                        cubicInterpolationMode: "monotone",
                        spanGaps: "false",
                        fill: "false"
                    }
                ]
            },
            options: {
            }
        });
  },
  methods: {
    gettitle () {
      this.titleList = []
      this.$http.get('/api/data').then(res => {
        for (var i = 0; i < res.data.length; i++) {
          this.titleList.push(res.data[i])
        }
        this.$Message.success("获取导航栏信息成功!")
        this.getdata(res.data[0])
      }).catch(err => {
        console.log(err)
        this.$Message.error("获取导航栏信息失败!")
        return null
      })
    },
    getdata (title) {
      this.dataList = []
      let data = {
        "title" : title
      }
      this.$http.post('/api/data', data).then(res => {
        this.msg = res.data.length
        for (var i = 0; i < this.msg; i++) {
          this.dataList.push({
            'name' : res.data[i][0],
            'time' : res.data[i][1][0],
            'list' : res.data[i][1][1]
          })
        }
        this.title = title
        this.$Message.success("获取"+title+"成功!")
      }).catch(err => {
        console.log(err)
        this.$Message.error("获取"+title+"失败!")
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
