// an app that that parses the data for variables in 'config' <script> since they need to be used over and over.
var app = (function ($) {

	var config = $('#config'),
		app = JSON.parse(config.text());

	$(document).ready(function () {
		var router = new app.router();
	});

	return app
})(jQuery);