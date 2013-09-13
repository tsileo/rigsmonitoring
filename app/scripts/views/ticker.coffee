'use strict';

class rigsmonitoring.Views.TickerView extends Backbone.View
  el: '#ticker'
  template: JST['app/scripts/templates/ticker.ejs']
  initialize: ->
    @listenTo @model, 'change', @render
    @model.fetch()

  render: ->
      $(@el).html @template @model.toJSON()
