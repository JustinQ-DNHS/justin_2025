---
title: Cookie Clicker
description: That cookie clicker
layout: post
type: hacks
comments: true
---
<style>
    .menu {
        height: 400px;
        width: 80%;
        background-color: #3f4247;
        margin-left: auto;
        margin-right: auto;
        border-radius: 10px;
        border: solid 5px #292827;
        padding: 10px;

        display: flex;
        justify-content: space-between; 
        align-items: flex-start; 
    }
    .cookiesClickedMenu {
        font-size: 28px;
    }
    .cookiesMenu > div {
        background-color: grey;
        padding: 0px 16px;
        margin: 15px 0;
        border-radius: 4px;
        border: solid 2px white;
        width: fit-content;
        height: 50px;
    }
    .store {
        width: 120px;
        display: inline-block;
        overflow: auto;
        text-align: right;
        background-color: white;
        height: 100%;
        padding: 10px;
        border-radius: 2px;
        border: solid 2px grey;
    }
    .item > p {
        margin: 0;
    }
    .item:hover {
        background-color: grey;
    }
    .item:active {
        background-color: black;
    }
    .cookie:active {
        width: 80%;
        height: 80%;
    }
</style>

<div style="text-align:center;">
    <img src="{{site.baseurl}}/images/cookieClicker.png" alt="Cookie Should be Here" onclick="clickCookie(1, true);" class="cookie">
</div>
<!-- Important Information -->
<div id="menu" class="menu">
    <div class="cookiesMenu" style="display:inline-block; width:fit-content">
        <div><p id="totalCookiesClickedMenu" class="cookiesClickedMenu">Total Cookies: 0</p></div>
        <div><p id="cookiesClickedMenu" class="cookiesClickedMenu">Cookies: 0</p></div>
        <div><p id="cookiesPerSecond" class="cookiesPerSecond">CPS: 0</p></div>
    </div>
    <!-- Store -->
    <div class="store">
        <div class="item" id="cursor" onclick="if (cookiesClicked >= 100) {cursorsOwned++; cookiesClicked-=100; cPerSecond++;}">
            <p style="color:black">Cursor</p>
            <p style="color:black; font-size:14px">100 Cookies</p>
        </div>
        <div class="item" id="grandma" onclick="if (cookiesClicked >= 500) {grandmasOwned++; cookiesClicked-=500; cPerSecond+=5}">
            <p style="color:black">Grandma</p>
            <p style="color:black; font-size:14px">500 Cookies</p>
        </div>
    </div>
</div>

<script>
    // All sound file sources
    const cookieClickSound = [
        new Audio('{{site.baseurl}}/audio/cookieClick1.mp3'), 
        new Audio('{{site.baseurl}}/audio/cookieClick2.mp3'), 
        new Audio('{{site.baseurl}}/audio/cookieClick3.mp3'), 
        new Audio('{{site.baseurl}}/audio/cookieClick4.mp3')
    ]

    // important reference variables
    let cPerSecond = 0;
    let cursorsOwned = 0;
    let grandmasOwned = 0;
    let cookiesClicked = 0;
    let totalCookiesClicked = 0;
    let cookiesClickedMenu = document.getElementById("cookiesClickedMenu");
    let totalCookiesClickedMenu = document.getElementById("totalCookiesClickedMenu");
    let cookiesPerSecondMenu = document.getElementById("cookiesPerSecond");
    
    function clickCookie(cookiesPerSecond, playSound = false) {
        // Increases cookies clicked count
        cookiesClicked += cookiesPerSecond;
        totalCookiesClicked += cookiesPerSecond;
        cookiesPerSecondMenu.innerHTML = "CPS: " + cPerSecond;
        // Updates counter
        cookiesClickedMenu.innerHTML = "Cookies: " + cookiesClicked;
        totalCookiesClickedMenu.innerHTML = "Total Cookies: " + totalCookiesClicked;
        if (playSound) {
            cookieClickSound[Math.floor((Math.random() * 3))].play();
        }
    }
    // Function to generate cookies depending on number cursors owned
    function cursorCookies(x) {
        clickCookie(x);
        // console.log(x);
        // This is broken, does not add grandmas. Needs to be fixed
        setTimeout(() => cursorCookies(cursorsOwned), 1000); // Pass a function reference with setTimeout
    }

    // Initial call of loop to generate cookies
    cursorCookies(cursorsOwned);
</script>
