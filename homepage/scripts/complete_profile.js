$(function(){
  $("#pips-range").noUiSlider({
	start: 2,
	connect: "lower",
	range: {
		'min': 0.0,
    '25%': 1.0,
    '50%': 2.0,
    '75%': 3.0,
		'max': 4.0
	},

	// Set some default formatting options.
	// These options will be applied to any Link
	// that doesn't overwrite these values.
	format: wNumb({
		decimals: 1
	})
});

$("#pips-range").Link('lower').to($("#value"), "text");



$(".pips-range").noUiSlider_pips({
	mode: 'range',
	density: 5

});
});
