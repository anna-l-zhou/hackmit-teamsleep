$(document).ready(function () {
    var running = false;
    var hoursElement = $("#hr");
    var minutesElement = $('#min')
    var secondsElement = $('#sec')

    var hours = minutes = seconds = timer = 0;

    function prependZero(time) {
        time = '' + (time | 0);
        while (time.length < 2) time = '0' + time;
        return time;
    }

    function setStopwatch(hours, minutes, seconds) {
        hoursElement.text(prependZero(hours));
        minutesElement.text(prependZero(minutes));
        secondsElement.text(prependZero(seconds));
    }

    function runTimer() {
        var startTime = Date.now();
        var prevHours = hours;
        var prevMinutes = minutes;
        var prevSeconds = seconds;

        timer = setInterval(function () {
            var timeElapsed = Date.now() - startTime;

            hours = (timeElapsed / 3600000) + prevHours;
            minutes = ((timeElapsed / 60000) + prevMinutes) % 60;
            seconds = ((timeElapsed / 1000) + prevSeconds) % 60;

            console.log(hours)
            

            setStopwatch(hours, minutes, seconds);
        }, 1000);
    }

    function run() {
        running = true;
        runTimer()
        $("#trackstart").hide()
    }

    function pause() {
        running = false;
        clearTimeout(timer);
    }

    function reset() {
        running = false;
        pause();
        hours = minutes = seconds = 0;
        setStopwatch(hours, minutes, seconds);
    }

    $("#trackstart").on('click', function () {
        running = true;
        run()
    })

    $("#trackpause").on('click', function () {
        pause();
    })

    $("#trackreset").on('click', function () {
        running = false;
        pause();
        clearTimeout(timer);
    })

})