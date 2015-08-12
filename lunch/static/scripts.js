$(document).ready(function () {
    var enableDays = ['2015-08-13', '2015-08-14'];

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
        onSelect: function (dateText) {
            //alert(dateText)
        }
    });



});