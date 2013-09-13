window.rigsmonitoring =
  Models: {}
  Collections: {}
  Views: {}
  Routers: {}
  init: ->
    'use strict'
    new @Views.TickerView model: new @Models.TickerModel

$ ->
  'use strict'
  rigsmonitoring.init()
