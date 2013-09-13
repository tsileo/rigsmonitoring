'use strict';

class rigsmonitoring.Views.SlushView extends Backbone.View
  el: '#slush'
  template: JST['app/scripts/templates/slush.ejs']
  initialize: ->
    @listenTo @model, 'change', @render
    @model.fetch()
    Visibility.every 60000 * 5, () -> rigsmonitoring.slush.model.fetch()
    $('#last-api-update').html new Date().toLocaleString()

  render: ->
      $(@el).html @template @model.toJSON()
