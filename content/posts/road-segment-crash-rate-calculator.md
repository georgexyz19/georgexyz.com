title: Road Segment Crash Rate Calculator
slug: road-segment-crash-rate-calculator
date: 2021-01-11 10:30
modified: 2021-01-11 10:30
tags: traffic engineering
note: crash rate calculator
no: 66

I am reading Part Two, Chapter 4.3 of 
[javascript.info](javascript.info) tutorial.  It has an exercise to write a js deposit calculator. 
I often use [a spreadsheet file](/files/CrashRateCal.xlsx) to calculate road segment crash rate.
The equations are not difficult, but it is easy to make mistakes.  

The equation below is from [this FHWA link](https://safety.fhwa.dot.gov/local_rural/training/fhwasa1210/s3.cfm). 

<div style="max-width:800px; border-top:1px solid #000; border-bottom:1px solid #000;">
  <img class="img-fluid pb-3" src="/images/crash-rate/eq.png" alt="mvm"> 
</div>

<p class="mt-4">Here is a js version I wrote.  The code is similar to the deposit calculator. </p>

**Road Segment Crash Rate Calculator**

<form name="calculator">
<table>
    <tr>
    <td>AADT (Annual Average Daily Traffic) </td>
    <td>
        <input name="aadt" type="number" value="10000" required>
    </td>
    </tr>

    <tr>
    <td>Segment Length (miles)</td>
    <td>
        <input name="length" type="number" step="0.01" value="1.51" required>
    </td>
    </tr>
    
    <tr>
    <td>Crash Number In 3 Years</td>
    <td>
        <input name="crashes" type="number" step="0.1" value="17" required>
    </td>
    </tr>

    <tr>
    <td>Results:</td>
    </tr>

    <tr>
    <td>Crash Number in 1 Year</td>
    <td>
        <input name="crashpery" type="text" readonly>
    </td>
    </tr>

    <tr>
    <td>VMT (Vehicle Miles Traveled)</td>
    <td>
        <input name="vmt" type="text" readonly>
    </td>
    </tr>

    <tr>
    <td>Segment Crash Rate</td>
    <td>
        <input name="rate" type="text" readonly>
    </td>
    </tr>
</table>
</form>


  <script>

    let form = document.forms.calculator;

    form.aadt.oninput = calculate;
    form.length.oninput = calculate;
    form.crashes.oninput = calculate;
    let days = 365; 

    function numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }

    function calculate() { 
        let aadt = +form.aadt.value;
        let length = +form.length.value;
        let crashes = +form.crashes.value; 

        let crashpery = (crashes / 3).toFixed(2);

        form.crashpery.value = crashpery; 

        let vmt = aadt * length * days; 
        vmt = Math.round(vmt); 
        form.vmt.value = numberWithCommas(vmt); 
        
        let rate = crashpery * 100000000 / vmt ;
        form.rate.value = rate.toFixed(1);


    //   if (!interest) return;

    //   let years = form.months.value / 12;
    //   if (!years) return;

    //   let result = Math.round(initial * (1 + interest * years));

    //   let height = result / form.money.value * 100 + 'px';
    //   document.getElementById('height-after').style.height = height;
    //   document.getElementById('money-before').innerHTML = form.money.value;
    //   document.getElementById('money-after').innerHTML = result;
    }

    calculate();
  </script>