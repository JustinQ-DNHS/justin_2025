---
toc: true
comments: true
layout: post
title: Creation of Snake
description: How I created and edited the snake game
type: tangibles
courses: { CompSci: { week: 2 } }
---
<style>
    /* Makes all <span> elements with the class of hc highlighted in light gray */
    span.hc {
        background-color: #454545 !important;
        padding-left: 4px;
        padding-right: 4px;
    }
    /* This part is copy and pasted from W3Schools */
    /* Designs the button for collapsable text */
    .collapsible {
        background-color: #454545;
        color: white;
        cursor: pointer;
        padding: 18px;
        width: 100%;
        border: none;
        text-align: left;
        outline: none;
        font-size: 15px;
    }
    .active, .collapsible:hover {
        background-color: #171717;
    }
    .content {
        padding: 0 18px;
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.2s ease-out;
        background-color: #171717;
    }
</style>
<!--Creation of Base Game -->
<section>
  <h2>Creation of the Base Game</h2>
  <p>I created the base of the game / the snake eatting apple part by following a tutorial by Mr. Mortensen. I will summarize it here.
  First, I created a new <span class="hc">.md</span> file in the <span class="hc">_posts</span> folder. I then went to this link <span class="hc"><a href="https://raw.githubusercontent.com/nighthawkcoders/APCSA/master/_posts/2022-07-08-PBL-FE-snake.md">SNAKE SOURCE</a></span> and copied and pasted all the code on that page into the <span class="hc">.md</span> file. This'll create the base page, you can play snake however I edited the code and will explain how to further on.</p>
</section>
<!-- Button Code -->
<section>
<button class="collapsible">How to Create Empty <span class="hc">.md</span> file</button>
    <div class="content">
        <p>The easiest way to create an empty <span class="hc">.md</span> file is to take an existing one and copy and paste it into the <span class="hc">_posts</span> folder. Then delete everything inside the file.</p>
    </div>
</section>
<!-- How to add Impossible Mode -->
<section>
  <h2>How to Add "Impossible" Mode</h2>
  <p>Adding the "Impossible" Mode speed setting is very simple, if you look through the code. Inside the code you'll see a comment over a block of code labeled "Settings Screen", under which you'll see the function for the speed settings. In order to add the "Impossible" setting you must add a new <span class="hc">input</span> code, just copy the code above exactly but instead of "speed#" you will add "speed4". Then you will lower the value, the lower the value the faster it will go. It will also be formatted in that same order, so if you want something to be before "Slow" place the code there and increase the number of each speed after and set the one you created to "speed1". You do not need to add a end input block as it is an empty tag. Then copy the <span class="hc">label</span> code but replace "speed#" with with "speed4" and name it "Impossible". Don't forget to end the label code!</p>
</section>
<!-- How to Change Colors -->
<section>
  <h2>How to Change Everything's Color</h2>
  <p>Changing every objects color is extremely simple, 
<!-- Next part is copy and pasted from W3 School
Script for the collapsable button -->
<script>
var coll = document.getElementsByClassName("collapsible");
var i;
  for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var content = this.nextElementSibling;
      if (content.style.maxHeight){
        content.style.maxHeight = null;
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
      } 
    });
  }
</script>