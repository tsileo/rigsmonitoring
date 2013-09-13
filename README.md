# Rigs Monitoring

Self-hosted monitoring dashboard for your mining rigs ([Bitcoin](http://bitcoin.org/) mining) written with [Python](http://python.org/) and [CoffeeScript](http://coffeescript.org/) with [Yeoman](http://yeoman.io/) and [Backbone](http://backbonejs.org/).

## Features

- Mining info from [Slush's pool](https://mining.bitcoin.cz/)
- [Exchange Rates API from Blockchain](https://blockchain.info/api/exchange_rates_api)

## Installation

```console
$ git clone https://github.com/tsileo/rigsmonitoring.git
$ npm install
$ bower install
```
for development:

```console
$ grunt server 
$ grunt --force
```

## Features

- Content updated every 5 minutes only when the tab is active, reload at tab focus (using the Page Visibility API).

## TODO

- move links to its own view
- notification system
