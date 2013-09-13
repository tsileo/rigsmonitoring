window.rigsmonitoring =
  Models: {}
  Collections: {}
  Views: {}
  Routers: {}
  init: ->
    'use strict'
    console.log 'Hello from Backbone!'
    new @Views.TickerView

$ ->
  'use strict'
  rigsmonitoring.init();
