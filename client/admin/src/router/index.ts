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
    component: () => import('@/views/dashboard/dashboard-index.vue'),
    meta: {
      index: 100,
      isAuthorized: false,
      title: "控制面板",
    }
  },

  {
    path: '/order/list-edit/:id',
    name: 'order-list-change',
    component: () => import('@/views/order/order-list-edit-index.vue'),
    meta: {
      index: 100,
      isAuthorized: false,
      title: "订单列表",
    }
  },
  {
    path: '/order/list-edit',
    name: 'order-list-edit',
    component: () => import('@/views/order/order-list-edit-index.vue'),
    meta: {
      index: 100,
      isAuthorized: false,
      title: "订单列表",
    }
  },
  {
    path: '/order/step-edit/:id',
    name: 'order-step-change',
    component: () => import('@/views/order/order-step-edit-index.vue'),
    meta: {
      index: 100,
      isAuthorized: false,
      title: "编辑流程",
    }
  },
  {
    path: '/order/step-edit',
    name: 'order-step-edit',
    component: () => import('@/views/order/order-step-edit-index.vue'),
    meta: {
      index: 100,
      isAuthorized: false,
      title: "编辑流程",
    }
  },

  {
    path: '/order/staff-edit',
    name: 'order-staff-edit',
    component: () => import('@/views/staff/staff-edit-index.vue'),
    meta: {
      index: 100,
      isAuthorized: false,
      title: "员工信息编辑",
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
