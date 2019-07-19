import Vue from 'vue'
import App from './App.vue'

import PouchDB from 'pouchdb'
import pouchVue from 'pouch-vue';
import pf from 'pouchdb-find'
import plf from 'pouchdb-live-find'
import pd from 'pouchdb-debug'

PouchDB.plugin(pf);
PouchDB.plugin(plf);
PouchDB.plugin(pd);

Vue.use(pouchVue, {
    pouch: PouchDB,
    defaultDB: 'postcards',
    optionDB: {},
    debug: '*'
});

Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')
