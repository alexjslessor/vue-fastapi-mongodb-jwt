import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/notprotected/Home.vue';
import DashboardPage from '@/views/DashboardPage';
import LoginForm from '@/components/forms/auth/LoginForm';
import Shop from '@/views/Shop';
import Product from '@/views/Product';
import CheckoutPage from '@/views/CheckoutPage';

import Account from '@/views/Account';
import Blog from '@/views/Blog';
import Post from '@/components/blog/Post';

// Auth page and child components
import AuthPage from '@/views/AuthPage';
import SignUpForm from '@/components/forms/auth/SignUpForm';
import ChangePassword from '@/components/forms/auth/ChangePassword';
import ForgotPassword from '@/components/forms/auth/ForgotPassword';
import ForgotPasswordFinal from '@/components/forms/auth/ForgotPasswordFinal';

// import CheckoutSuccess from '@/components/CheckoutSuccess.vue'
// import SignUpPage from '@/views/notactive/SignUpPage';
// import AddShippingPage from '@/views/AddShippingPage';
// import AuthResetPasswordPage from '@/views/AuthResetPasswordPage'

// import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/auth',
    name: 'AuthPage',
    component: AuthPage,
    children: [
      {
        path: 'login',
        name: 'Login',
        component: LoginForm,
      },
      {
        path: 'signup',
        name: 'SignUp',
        component: SignUpForm
      },
      {
        path: 'reset',
        name: 'ChangePassword',
        component: ChangePassword,
        // meta: {protectedRoute: true},
      },
      {
        path: 'forgot-password',
        name: 'ForgotPassword',
        component: ForgotPassword,
      },
      {
        path: 'forgot-password-final',
        name: 'ForgotPasswordFinal',
        props: route => ({ query: route.query.q }),
        component: ForgotPasswordFinal,
        meta: {protectedRoute: true},
      },
    ]
  },
  {
    path: '/account',
    name: 'Account',
    component: Account,
    meta: {protectedRoute: true},
  },
  {
    path: '/shop',
    name: 'Shop',
    component: Shop,
    meta: {protectedRoute: true},
  },
  {
    path: '/blog',
    name: 'Blog',
    component: Blog,
    meta: {protectedRoute: true},
  },
  {
    path: '/blog/:postId',
    name: 'Post',
    component: Post,
    props: true,
    meta: {protectedRoute: true},
  },
  // {
  //   path: '/success',
  //   name: 'Success',
  //   component: CheckoutSuccess
  // },
  {
    path: '/:productId/shop',
    name: 'Product',
    component: Product,
    props: true,
    meta: {protectedRoute: true},
  },
  {
    path: '/checkout',
    name: 'CheckoutPage',
    component: CheckoutPage,
    meta: {protectedRoute: true},
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardPage,
    meta: {protectedRoute: true},
  },
]

const router = new VueRouter({
  mode: "history",
  base: "",
  routes})


// This callback runs before every route change, including on page load.
// router.beforeEach((to, from, next) => {
//   // This goes through the matched routes from last to first, finding the closest route with a title.
//   // e.g., if we have `/some/deep/nested/route` and `/some`, `/deep`, and `/nested` have titles,
//   // `/nested`'s will be chosen.
//   const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);

//   // Find the nearest route element with meta tags.
//   const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

//   // If a route with a title was found, set the document (page) title to that value.
//   if(nearestWithTitle) document.title = nearestWithTitle.meta.title;

//   // Remove any stale meta tags from the document using the key attribute we set below.
//   Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el));

//   // Skip rendering meta tags if there are none.
//   if(!nearestWithMeta) return next();

//   // Turn the meta tag definitions into actual elements in the head.
//   nearestWithMeta.meta.metaTags.map(tagDef => {
//     const tag = document.createElement('meta');

//     Object.keys(tagDef).forEach(key => {
//       tag.setAttribute(key, tagDef[key]);
//     });

//     // We use this to track which meta tags we create so we don't interfere with other ones.
//     tag.setAttribute('data-vue-router-controlled', '');

//     return tag;
//   })
//   // Add the meta tags to the document head.
//   .forEach(tag => document.head.appendChild(tag));

//   next();
// });

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.protectedRoute) && !store.state.isAuthenticated) {
//     next({ name: 'Login', query: { to: to.path } });

//   } else {
//     next()
//   }
// })

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.protectedRoute)) {

//     if (!store.getters.getUsername) {
//       next({path: '/login'})
//     } else {
//       next();
//     }

//     // if (store.getters.getIsFirstLogin) {
//     //   next({ path: '/reset' });
//     // } else {
//     //   next();
//     // }

//   } else {
//     next();
//   }
// });

// router.afterEach((to, from, next) => {
//   const newUser = store.getters.getIsFirstLogin;
//   if (newUser) {
//     router.push('/reset')
//   }
// });


// https://github.com/ywiyogo/FastAPI-Vuetify/blob/master/vuetify-material/src/router.js
// router.beforeEach((to, from, next) => {
//   // const loggedIn = localStorage.getItem("access_token");
//   const loggedIn = localStorage.getItem("token");
//   if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
//     next("/");
//   } else {
//     next();
//   }
// });

export default router