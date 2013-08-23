(function($) {

    "use strict";

	var options = {
		events_url: '/calendar/json/',
		view: 'month',
		tmpl_path: '/static/tmpls/',
		first_day: 1,
		onAfterEventsLoad: function(events) {
			if(!events) {
				return;
			}
		},
		classes: {
			months: {
				general: 'label'
			}
		}
	};

	var	calendar = $('#calendar').calendar(options);

	$('.btn-group button[data-calendar-nav]').each(function() {
		var $this = $(this);
		$this.click(function() {
			calendar.navigate($this.data('calendar-nav'));
		});
	});

	$('.btn-group button[data-calendar-view]').each(function() {
		var $this = $(this);
		$this.click(function() {
			calendar.view($this.data('calendar-view'));
		});
	});

}(jQuery));
