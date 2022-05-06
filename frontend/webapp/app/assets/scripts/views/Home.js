import React, { Component } from 'react';
import { connect } from 'react-redux';

import { appDescription, appTitle } from '../config';

import App from './App';

class Home extends Component {

  render() {
    return (
      <App className='page__home'>
        <article>
          <header>
            <div>
              <div>
                <h1>{appTitle}</h1>
              </div>
            </div>
          </header>
          <div>
            <div>
              {appDescription}
            </div>
          </div>
        </article>
      </App>
    );
  }
}

export default connect(
)(Home);
