import React, { Component } from 'react';
import { connect } from 'react-redux';
import App from './App';

class Dashboard extends Component {

  render() {
    let { instance, id } = this.props.match.params;
    return (
      <App className='page__dashboard'>
        <article>
          <header>
            <div>
              <div>
                <h1>{instance}</h1>
              </div>
            </div>
          </header>
          <div>
            <div>
              {id}
            </div>
          </div>
        </article>
      </App>
    );
  }
}

export default connect(
)(Dashboard);
