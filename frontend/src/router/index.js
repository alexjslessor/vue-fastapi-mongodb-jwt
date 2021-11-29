import Vue from 'vue';
import VueRouter from 'vue-router';
import routes from './routes';

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  base: "",
  routes})

  router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.protectedRoute)) {
        const loggedIn = !!localStorage.getItem("username");
        // console.log('loggedin: ', loggedIn);
        if (!loggedIn) {
          next({ name: 'Login' } );
        } else {
          next();
        }
    } else {
      next();
    }
  });

  export default router