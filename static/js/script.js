/**
 * script for the countdown
 */

 const countdown = () => {
    const countDate = new Date ("December 2, 2022 09:00:00").getTime();
    const now = new Date().getTime();
    const gap = countDate - now;

    // counting time
    const second = 1000;
    const minute = second * 60;
    const hour = minute * 60;
    const day = hour * 24;

    // calculate day
    const showDay = Math.floor(gap / day);
    const showHour = Math.floor ((gap % day) / hour)
    const showMin = Math.floor ((gap % hour) / minute)
    const showSec = Math.floor ((gap % minute) / second)

    document.querySelector(".day").innerText = showDay;
    document.querySelector(".hour").innerText = showHour;
    document.querySelector(".min").innerText = showMin;
    document.querySelector(".secs").innerText = showSec;
};

setInterval(countdown, 1000)
