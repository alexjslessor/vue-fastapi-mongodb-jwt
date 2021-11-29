// import Vue from 'vue';
// import VueRouter from 'vue-router';
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
    beforeEnter: (to, from, next) => {
      if (from.name == 'Login') {
        const newUser = JSON.parse(localStorage.getItem("isFirstLogin") );
        // console.log('dashboard before enter: ', newUser);
        if ( newUser ) {
          next( { path: '/reset' } );
        } else {
          next();
        }
      } else {
        next();
      }
    },
  },
];

export default routes;