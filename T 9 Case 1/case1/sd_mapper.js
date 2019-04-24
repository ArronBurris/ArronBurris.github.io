"use strict";
/*
   New Perspectives on HTML5 and CSS3, 7th Edition
   Tutorial 9
   Case Problem 1

   Planisphere Script
   Author: Arron Burris
   Date: 4/22/2019

*/



var thisTime = new Date(2019, 4, 24, 9, 2, 28);
var timeStr = thisTime.toLocaleString();	
document.getElementById("timeStamp").innerHTML = timeStr;

var thisHour = thisTime.getHours();

var thisMonth = thisTime.getMonth();

var mapNum = (2 * thisMonth + thisHour)%24;

var imgStr = "<img src='sd_sky" + mapNum + ".png' />";

document.getElementById("planisphere").insertAdjacentHTML("afterbegin",imgStr);


