import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';

// 路由信息
const routes: RouteRecordRaw[] = [
  {
    path: "/",
    redirect: "/dashboard",
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('@/views/dashboard/index.vue'),
    meta: {
      index: 100,
      isAuthorized: false,
      title: "控制面板",
    }
  },

  {
    path: '/order/:id',
    name: 'order_edit',
    component: () => import('@/views/orderList/index.vue'),
    meta: {
      index: 100,
      isAuthorized: false,
      title: "订单列表",
    }
  },

  {
    path: '/order',
    name: 'order_add',
    component: () => import('@/views/orderList/index.vue'),
    meta: {
      index: 100,
      isAuthorized: false,
      title: "订单列表",
    }
  },

  {
    path: '/changeSetp',
    name: 'changeSetp',
    component: () => import('@/views/changeStep/index.vue'),
    meta: {
      index: 100,
      isAuthorized: false,
      title: "编辑步骤",
    }
  },

];

// 导出路由
const router = createRouter({
  history: createWebHashHistory(),
  routes
});

// 路由守卫, 修改页面标题
router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title as string;
  }

  next();

});

export default router;
