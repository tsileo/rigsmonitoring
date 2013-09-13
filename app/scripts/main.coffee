window.rigsmonitoring =
  Models: {}
  Collections: {}
  Views: {}
  Routers: {}
  init: ->
    'use strict'
    @ticker = new @Views.TickerView model: new @Models.TickerModel
    @slush = new @Views.SlushView model: new @Models.SlushModel

$ ->
  'use strict'
  rigsmonitoring.init()
