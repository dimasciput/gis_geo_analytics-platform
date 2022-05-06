import React from 'react';
import { NavLink } from 'react-router-dom';
import i18n from "i18next";
import { getBaseUrl } from "../app";

export default class NavBar extends React.PureComponent {
  render() {
    return (
      <header className='page__header'>
        <ul className='page__header-menu'>
          <li>
            <NavLink
              exact
              to={getBaseUrl()}
              title={i18n.t('Homepage')}
              activeClassName='page__header-link--active'
              className='page__header-link'
            >
              <span>Home</span>
            </NavLink>
          </li>
          <li>
            <NavLink
              exact
              to={getBaseUrl()}
              title={i18n.t('Homepage')}
              activeClassName='page__header-link--active'
              className='page__header-link'
            >
              <span>Home</span>
            </NavLink>
          </li>
        </ul>
      </header>
    );
  }
}
