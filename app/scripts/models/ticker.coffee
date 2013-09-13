'use strict';

class rigsmonitoring.Models.TickerModel extends Backbone.Model
  url: 'https://blockchain.info/ticker?cors=true'
  parse: (resp) -> ticker: resp