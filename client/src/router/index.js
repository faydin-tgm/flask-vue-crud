import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Books from '@/components/Todo';
import Order from '@/components/Order';
import OrderComplete from '@/components/OrderComplete';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Todo',
      component: Todos,
    },
    {
      path: '/order/:id',
      name: 'Order',
      component: Order,
    },
    {
      path: '/complete/:id',
      name: 'OrderComplete',
      component: OrderComplete,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
  mode: 'hash',
});
