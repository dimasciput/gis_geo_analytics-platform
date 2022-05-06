import React from 'react';
import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import { Route, Switch } from "react-router-dom";

// Utils and Config
import { getCookie, setCookie } from "./utils/main";
import { subUrl } from './config';

// Views
import Home from './views/Home';
import Dashboard from './views/Dashboard';
import PageNotFound from './views/PageNotFound';

const resources = {};

/**
 * Return base url
 * the url may use sub url and also language
 */
export function getBaseUrl() {
  return subUrl ? subUrl : ''
}

/**
 * Change language
 * @param lang
 */
export function changeLanguage(lang) {
  setCookie('lang', lang);
  window.location.reload()
}


class App extends React.Component {
  constructor(props) {
    super(props);

    // get cookie of lang
    const lang = getCookie('lang')
    if (!Object.keys(resources).includes(lang) && lang !== 'en') {
      changeLanguage('en')
    }

    // set the translation
    i18n
      .use(initReactI18next) // passes i18n down to react-i18next
      .init({
        resources,
        lng: lang,
        keySeparator: false, // we do not use keys in form messages.welcome
        interpolation: {
          escapeValue: false // react already safes from xss
        }
      });
  }

  render() {
    return (
      <Switch>
        <Route exact path={getBaseUrl() + '/'} component={Home}/>
        <Route exact path={getBaseUrl() + '/dashboard/:instance/:id'} component={Dashboard}/>
        <Route path={getBaseUrl() + '*'} component={PageNotFound}/>
      </Switch>
    )
  }
}

export default App;
