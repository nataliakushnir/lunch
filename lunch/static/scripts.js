$(document).ready(function () {

    $.get("/ajax/available-days", function (data) {
        enableDays = data;
    });

    function enableAllTheseDays(date) {
        var sdate = $.datepicker.formatDate('yy-mm-dd', date);
        if ($.inArray(sdate, enableDays) != -1) {
            return [true];
        }
        return [false];
    }

    $("#id_date").datepicker({
        minDate: 1,
        dateFormat: "yy-mm-dd",
        beforeShowDay: enableAllTheseDays,
        onSelect: function(dateText) {
        $(this).change();
      }
    })
    .change(function() {
      window.location.href = "?date=" + this.value;

    }).keydown(false);
});

$(function() {
    var spinner = $( "#spinner" ).spinner();
    $("#spinner").width(10);
    $( "#disable" ).click(function() {
      if ( spinner.spinner( "option", "disabled" ) ) {
        spinner.spinner( "enable" );
      } else {
        spinner.spinner( "disable" );
      }
    });
    $( "#destroy" ).click(function() {
      if ( spinner.spinner( "instance" ) ) {
        spinner.spinner( "destroy" );
      } else {
        spinner.spinner();
      }
    });
    $( "#getvalue" ).click(function() {
      alert( spinner.spinner( "value" ) );
    });
    $( "#setvalue" ).click(function() {
      spinner.spinner( "value", 5 );
    });

    $( "button" ).button();
  });