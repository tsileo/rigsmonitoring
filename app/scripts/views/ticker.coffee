'use strict';

class rigsmonitoring.Views.TickerView extends Backbone.View
    el: '#ticker'
    template: JST['app/scripts/templates/ticker.ejs']
    initialize: ->
        @render()

    render: ->
        $(@el).html @template
