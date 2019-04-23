import Vue from 'vue'
import Router from 'vue-router'
import TrendAnalysis from '@/components/TrendAnalysis'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'TrendAnalysis',
      component: TrendAnalysis
    }
  ]
})
