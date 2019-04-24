/*
   New Perspectives on HTML5 and CSS3, 7th Edition
   Tutorial 9
   Case Problem 1

   Planisphere Script
   Author: Arron Burris
   Date: 4/22/2019
"February 3, 2018 3:15:28 a.m."
*/

"use strict";

var thisTime = new Date(2018, 3, 3, 3, 15, 28,);
var timeStr = thisTime.toLocaleString();	
document.getElementById("timeStamp").innerHTML = timeStr;

var thisHour = getHours("thisTime");

var thisMonth = getMonth("thisTime");

var mapNum = (2 * thisMonth + thisHour)%24;

var imgStr = ("<img src='sd_sky0.png' />");

var Element = document.getElementById("planisphere");

Element.insertAdjacentHTML("afterbegin", imgStr);
