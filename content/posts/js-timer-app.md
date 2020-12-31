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

The app does not work yet.  I will add js code to it. 


<script type="text/javascript">

    id15.addEventListener("click", () => {
        display.innerHTML = "15:00"
    });

    id10.addEventListener("click", () => {
        display.innerHTML = "10:00"
    });

    id25.addEventListener("click", () => {
        display.innerHTML = "25:00"
    });

    id5.addEventListener("click", () => {
        display.innerHTML = "5:00"
    });

    reset.addEventListener("click", () => {
        display.innerHTML = "00:00"
    });

    // let time = 100
    // start.addEventListener("click", () => {
    //     let timerId = setInterval(() => {
    //         // decrease the display by 1 second
    //         display.innerHTML = String(time--);
    //     }, 1000);
    // });

</script>