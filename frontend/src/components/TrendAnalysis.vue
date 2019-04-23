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
        <h2>热度图</h2>
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
