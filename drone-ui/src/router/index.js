import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Drones from '@/components/Drone';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Drone',
      component: Drones,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },,
    {
      path: '/helloworld',
      name: 'HelloWorld',
      component: Ping,
    },
  ],
});
