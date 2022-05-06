import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { Route, Router, Switch } from 'react-router-dom';

import App from './app';
import config, { subUrl } from './config';

// Store
import { history, store } from './store';

ReactDOM.render(
  <Provider store={store}>
    <Router history={history}>
      {
        subUrl ?
          <Switch>
            <Route path={subUrl} component={App}/>
            <Route path={'*'} component={App}/>
          </Switch>
          : <Route path={subUrl} component={App}/>
      }

    </Router>
  </Provider>,
  document.getElementById('root')
);

/* eslint-disable no-console */
console.log.apply(console, config.consoleMessage);
console.log('Environment', config.environment);
/* eslint-enable no-console */
