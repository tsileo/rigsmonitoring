'use strict';

class rigsmonitoring.Views.TickerView extends Backbone.View
  el: '#ticker'
  template: JST['app/scripts/templates/ticker.ejs']
  initialize: ->
    @listenTo @model, 'change', @render
    @model.fetch()
    Visibility.every 60000 * 5, () -> rigsmonitoring.ticker.model.fetch()
    $('#last-ticker-update').html new Date().toLocaleString()

  render: ->
      $(@el).html @template @model.toJSON()
