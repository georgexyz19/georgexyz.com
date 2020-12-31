title: A Javascript Timer App
slug: js-timer-app
date: 2020-12-31 13:49
modified: 2020-12-31 13:49
tags: javascript
note: A starter project for a js timer app
no: 65

I am reading the *Eloquent Javascript* book and 
[javascript.info](javascript.info) website for the past few weeks. 
My goal is to write a javascript timer app for myself. 
On this last day of 2020, I want to write something down as a start 
point.  

<div class="p-3 mb-4" style="border: 3px solid #666;">

    <h1 class="display-1 mt-0" id="display">15:00</h1>

    <div>
        <button type="button" class="btn btn-outline-primary" id="id15">15 min</button>
        <button type="button" class="btn btn-outline-primary" id="id10">10 min</button>
        <button type="button" class="btn btn-outline-primary" id="id25">25 min</button>
        <button type="button" class="btn btn-outline-primary" id="id5">5 min</button>
    </div>

    <div class="mt-3">
        <button type="button" class="btn btn-primary" id="start">Start</button>
        <button type="button" class="btn btn-primary" id="reset">Reset</button>
    </div>

</div>

The app is not finished yet.  I will add js code to it. 


<script type="text/javascript">

    let strTime = display.innerHTML;
    let time = strToSec(strTime);

    function resetTime(t) {
        time = t;
        display.innerHTML = secToStr(t); 
    }

    id15.addEventListener("click", () => {
        resetTime(900);
    });

    id10.addEventListener("click", () => {
        resetTime(600);
    });

    id25.addEventListener("click", () => {
        resetTime(25 * 60);
    });

    id5.addEventListener("click", () => {
        resetTime(5 * 60);
    });


    reset.addEventListener("click", () => {resetTime(0)} );

    function strToSec(strT) {
        // 15:00 str to 15 * 60 + 0 sec
        let strA = strT.split(":");
        let strMin = strA[0];
        let strSec = strA[1]; 
        let sec = Number(strMin) * 60 + Number(strSec);
        return sec
    }

    function secToStr(sec) {
        // 900 sec to 15:00
        // sec / 60
        let quotient = Math.floor(sec/60);
        let remainder = sec % 60;

        let remainderStr = remainder.toString(); 

        if (remainder < 10 )
        {
            remainderStr = '0' + remainder.toString(); 
        }
        let strT = quotient.toString() + ':' + remainderStr;
        return strT
    }


    let running = false;
    let timerId = 0;
    let buttons = document.querySelectorAll('button');

    start.addEventListener("click", () => {
        if (running) {
            if (timerId) {
                clearInterval(timerId);
            }
            start.innerHTML = "Start";
            running = false;
            
            buttons.forEach( (elem, index, array) => {elem.disabled = false;} ); 
             
        }
        else {
            timerId = setInterval(() => {
                // decrease the display by 1 second
                time = time -1
                display.innerHTML = secToStr(time);
            }, 1000);

            start.innerHTML = "Stop"
            running = true;
            buttons.forEach( (elem, index, array) => {elem.disabled = true;} ); 
            start.disabled = false; 
        }
    });

</script>