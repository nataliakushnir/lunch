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

    $.get("/ajax/available-days", function (data) {
        enableDays = data;
    });

    $("#id_date").datepicker({
        minDate: 1,
        dateFormat: "yy-mm-dd",
        beforeShowDay: enableAllTheseDays,
        onSelect: function (dateText) {
            $(this).change();
        }
    })
        .change(function () {
            window.location.href = "?date=" + this.value;

        }).keydown(false);

    $('.datepick').each(function () {
        $(this).datepicker();


    });

    $('.datepic').each(function () {
        $(this).datepicker();

    });

});