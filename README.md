# Rigs Monitoring

Self-hosted monitoring dashboard for your mining rigs ([Bitcoin](http://bitcoin.org/) mining) written with [Python](http://python.org/) and [CoffeeScript](http://coffeescript.org/) with [Yeoman](http://yeoman.io/) and [Backbone](http://backbonejs.org/).

Full documentation on [rigsmonitoring.com](https://rigsmonitoring.com).


## Features

- Mining info from [Slush's pool](https://mining.bitcoin.cz/)
- [Exchange Rates API from Blockchain](https://blockchain.info/api/exchange_rates_api)
- Devices infos from [cgminer API](https://github.com/ckolivas/cgminer), using [pycgminer](https://github.com/tsileo/pycgminer)


## Installation

```console
$ git clone https://github.com/tsileo/rigsmonitoring.git
$ cd rigsmonitoring
$ npm install
$ bower install
$ grunt build
$ pip install -r reqs.txt
$ cp -r settings.cfg.sample settings.cfg
$ vim settings.cfg
$ python server.py
```

For development, ``grunt server`` will automatically spawn a develoment server.

```console
$ grunt server
```


## Donation

BTC 1BB599XpWHXL9wNdFAbZ5EgVATtegYH11d


## License

Copyright (c) 2013 Thomas Sileo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.