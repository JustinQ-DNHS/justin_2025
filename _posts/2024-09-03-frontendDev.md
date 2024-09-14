---
title: FrontEnd (Week 2)
description: Completing my frontend work Assignment
layout: post
type: hack
comments: true
---
<style>
    .text {
        font-size: 38px;
        text-align: center;
        color: green !important;
    }
    .source {
        font-size: 28px;
        text-align:center;
    }
    button {
        text-align: center;
        width: 120px;
        height: 60px;
        background-color: #1d85c2 !important;
    }
</style>

<div style="text-align:center; border: 1px solid #415ce0;">
    <p class="text">THIS BUTTON DOES NOTHING?!!?!?!</p>
    <button style="margin-bottom:25px" onclick='window.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")'>Click Me?</button>
</div>
<br>
<div>
    <p class="source"><a href="https://www.w3schools.com/tags/tag_comment.asp">Source 1</a></p>
    <p class="source"><a href="https://nighthawkcoders.github.io/portfolio_2025/frontend/basics/playground">Source 2</a></p>
    <p class="text">These are my sources</p>
</div>

<script>
    let person = {
        name: "Justin",
        gender: "Male",
        programmingExperience: "1 Year",
        age: 17,
        currentClasses: ["APStatistics", "APCalculusBC", "Civics", "Digital Media Production", "APComputer Science Principles",],
        interests: ["Programming", "Piano", "Guitar", "Board Games", "Video Games",],
    }

    console.log(person)

    person.interests.push("arrayManipulation")
    console.log("\n")
    console.log(person)
    console.log(typeof(person) + "\n" + typeof(person.age) + "\n" + typeof(person.name))
</script>
