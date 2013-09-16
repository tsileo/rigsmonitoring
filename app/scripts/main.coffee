window.rigsmonitoring =
  Models: {}
  Collections: {}
  Views: {}
  Routers: {}
  init: ->
    'use strict'
    @ticker = new @Views.TickerView model: new @Models.TickerModel
    @slush = new @Views.SlushView model: new @Models.SlushModel
    @slush = new @Views.CgminerView model: new @Models.CgminerModel       

$ ->
  'use strict'
  rigsmonitoring.init()
