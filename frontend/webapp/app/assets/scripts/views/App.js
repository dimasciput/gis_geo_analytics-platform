import React, { Component } from 'react';
import T from 'prop-types';
import c from 'classnames';

import NavBar from '../components/NavBar';

import { environment } from '../config';

class App extends Component {
  render() {

    const { className, children } = this.props;

    return (
      <div className={c('page', className)}>
        <NavBar/>
        <main>
          {children}
        </main>
      </div>
    );
  }
}

if (environment !== 'production') {
  App.propTypes = {
    className: T.string,
    children: T.node
  };
}

export default App;
