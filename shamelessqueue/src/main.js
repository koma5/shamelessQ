import Vue from 'vue'
import App from './App.vue'

import PouchDB from 'pouchdb'
import pouchVue from 'pouch-vue';
import pf from 'pouchdb-find'
import plf from 'pouchdb-live-find'
import pd from 'pouchdb-debug'
import pa from 'pouchdb-authentication'

import Croppa from 'vue-croppa';
import 'vue-croppa/dist/vue-croppa.css';

PouchDB.plugin(pf);
PouchDB.plugin(plf);
PouchDB.plugin(pd);
PouchDB.plugin(pa);

Vue.use(pouchVue, {
    pouch: PouchDB,
    defaultDB: 'postcards',
    optionDB: {},
    debug: '*'
});

Vue.use(Croppa);

Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')
