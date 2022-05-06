import React from 'react';
import { Link } from 'react-router-dom';

import App from './App';
import { getBaseUrl } from "../app";

class PageNotFound extends React.Component {
  render() {
    return (
      <App>
        <article>
          <header>
            <div>
              <div>
                <h1>Page not found</h1>
              </div>
            </div>
          </header>
        </article>
      </App>
    );
  }
}

export default PageNotFound;
