'use strict';

class rigsmonitoring.Views.CgminerView extends Backbone.View
  el: '#cgminer'
  template: JST['app/scripts/templates/cgminer.ejs']
  initialize: ->
    @listenTo @model, 'change', @render
    @model.fetch()
    Visibility.every 60000 * 5, () -> rigsmonitoring.cgminer.model.fetch()
    $('#last-cgminer-update').html new Date().toLocaleString()

  render: ->
      $(@el).html @template @model.toJSON()
