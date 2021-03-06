title: A Javascript Count Down Timer App
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

<div class="p-3 mb-4" 
     style="border: 3px solid #666; border-radius: 10px;">

    <h1 class="display-1 mt-0" id="display">15:00</h1>

    <div>
        <button type="button" class="btn btn-outline-primary" id="id15">15 min</button>
        <button type="button" class="btn btn-outline-primary" id="id10">10 min</button>
        <button type="button" class="btn btn-outline-primary" id="id25">25 min</button>
        <button type="button" class="btn btn-outline-primary" id="id5">5 min</button>
    </div>

    <div class="mt-3">
        <button type="button" class="btn btn-primary" id="start">Start</button>
    </div>

</div>

The app is not finished yet.  I will add js code to it...

**Update (1/1/2021):** The app is working Okay now. I add two beep sounds at the 
end of the timer.  Also the NoSleep js is added to prevent screen sleeping. 
The only major problem is that if you refresh the webpage, the timer will go 
back to initial state 15 minutes.  

**Update (1/5/2021):** Change the sound to three beeps and change the font color 
to red when it reaches zero. So far I am happy with the app. 


<script src="/theme/js/NoSleep.min.js"></script>

<script>

    // for Nosleep js
    let noSleep = new NoSleep();
    let wakeLockEnabled = false;

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
        resetTime( 5 * 60);
    });

    function strToSec(strT) {
        // 15:00 str to 15 * 60 + 0 sec
        let strA = strT.split(":");
        let strMin = strA[0];
        let strSec = strA[1]; 
        let sec = Number(strMin) * 60 + Number(strSec);
        return sec
    }

    function colorRed(elem) {
        elem.style.color = "red"; 
    }

    function secToStr(sec) {
        // 900 sec to 15:00
        // sec / 60

        display.style.color = '';

        if(sec < 0)
        {
            sec = -sec;
            colorRed(display); //display is id
        }

        let quotient = Math.floor(sec/60);
        let remainder = sec % 60;

        let quotientStr = quotient.toString();
        let remainderStr = remainder.toString(); 

        if (quotient < 10 )
        {
            quotientStr = '0' + quotient.toString(); 
        }

        if (remainder < 10 )
        {
            remainderStr = '0' + remainder.toString(); 
        }
        let strT = quotientStr + ':' + remainderStr;
        return strT
    }


    let running = false;
    let timerId = 0;
    let buttons = document.querySelectorAll('button');
    
    // play beep sound, revised from
    // https://stackoverflow.com/questions/879152/how-do-i-make-javascript-beep
    function beep() {
        let snd = new Audio("data:audio/wav;base64,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qJrx4KOQjahZxWbcZgztj2c49nKmkId44S71j0c8eV9yDK6uPRzx5X18eDvjvQ6yKo9ZSS6l//8elePK/Lf//IInrOF/FvDoADYAGBMGb7FtErm5MXMlmPAJQVgWta7Zx2go+8xJ0UiCb8LHHdftWyLJE0QIAIsI+UbXu67dZMjmgDGCGl1H+vpF4NSDckSIkk7Vd+sxEhBQMRU8j/12UIRhzSaUdQ+rQU5kGeFxm+hb1oh6pWWmv3uvmReDl0UnvtapVaIzo1jZbf/pD6ElLqSX+rUmOQNpJFa/r+sa4e/pBlAABoAAAAA3CUgShLdGIxsY7AUABPRrgCABdDuQ5GC7DqPQCgbbJUAoRSUj+NIEig0YfyWUho1VBBBA//uQZB4ABZx5zfMakeAAAAmwAAAAF5F3P0w9GtAAACfAAAAAwLhMDmAYWMgVEG1U0FIGCBgXBXAtfMH10000EEEEEECUBYln03TTTdNBDZopopYvrTTdNa325mImNg3TTPV9q3pmY0xoO6bv3r00y+IDGid/9aaaZTGMuj9mpu9Mpio1dXrr5HERTZSmqU36A3CumzN/9Robv/Xx4v9ijkSRSNLQhAWumap82WRSBUqXStV/YcS+XVLnSS+WLDroqArFkMEsAS+eWmrUzrO0oEmE40RlMZ5+ODIkAyKAGUwZ3mVKmcamcJnMW26MRPgUw6j+LkhyHGVGYjSUUKNpuJUQoOIAyDvEyG8S5yfK6dhZc0Tx1KI/gviKL6qvvFs1+bWtaz58uUNnryq6kt5RzOCkPWlVqVX2a/EEBUdU1KrXLf40GoiiFXK///qpoiDXrOgqDR38JB0bw7SoL+ZB9o1RCkQjQ2CBYZKd/+VJxZRRZlqSkKiws0WFxUyCwsKiMy7hUVFhIaCrNQsKkTIsLivwKKigsj8XYlwt/WKi2N4d//uQRCSAAjURNIHpMZBGYiaQPSYyAAABLAAAAAAAACWAAAAApUF/Mg+0aohSIRobBAsMlO//Kk4soosy1JSFRYWaLC4qZBYWFRGZdwqKiwkNBVmoWFSJkWFxX4FFRQWR+LsS4W/rFRb/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////VEFHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAU291bmRib3kuZGUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjAwNGh0dHA6Ly93d3cuc291bmRib3kuZGUAAAAAAAAAACU=");  
        snd.play();
        setTimeout( () => { snd.play();}, 1000 ); //change to 1 sec
        setTimeout( () => { snd.play();}, 2000 ); //change to 2 sec
    }


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

                if (time == 0){
                    beep();
                }
                display.innerHTML = secToStr(time);
            }, 1000);

            start.innerHTML = "Stop"
            running = true;
            buttons.forEach( (elem, index, array) => {elem.disabled = true;} ); 
            start.disabled = false; 
        }
    });

    start.addEventListener('click', function() {
        if (!wakeLockEnabled) {
            noSleep.enable(); // keep the screen on!
            wakeLockEnabled = true;
            // toggleEl.value = "Wake Lock is enabled";
            // display.style.backgroundColor = "lightblue";
        } else {
            noSleep.disable(); // let the screen turn off.
            wakeLockEnabled = false;
            // toggleEl.value = "Wake Lock is disabled";
            // display.style.backgroundColor = "";
        }
    }, false);

</script>