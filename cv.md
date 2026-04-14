---
layout: post
title: CV
permalink: /cv/
---

## Curriculum Vitae

Download PDF: [Resume.pdf](/assets/Resume.pdf)

---

## Education
B.A. Physics - University of Pennsylvania

M.S. Physics - University of Pennsylvania

(Far in the future) Candidate for Ph.D. Electrical Engineering - University of California Los Angeles

## Research Interests
- Microcombs!
- Photonics

## Biography (á la [Matt Might](https://matt.might.net/bio/#isformal=0&isfocus=0&isfunders=0&isbertrand=0&iscstechlit=0&iscsbackground=0&iseducation=0&issocial=0))

<h3>Parameters to change the bio</h3>

<p>
Check or uncheck these to modify the bio:
</p>

<input type="checkbox" id="isformal"  checked onchange="updateAll()" /> Use formal titles?
<br />

<input type="checkbox" id="isfunding"  checked onchange="updateAll()" /> Include funding? 
<br />

<input type="checkbox" id="iseducation"  checked onchange="updateAll()" /> Include education? 
<br />

<input type="checkbox" id="ishobbies"  checked onchange="updateAll()" /> Include 
hobbies?
<br />

<input type="checkbox" id="issocial"  checked onchange="updateAll()" /> Include 
social media info?
<br />


<h3>Generated bio</h3>

<p>
<span name="IntroName">INTRONAME</span> will be pursuing his Ph.D. in electrical engineering (to be updated on June 29th, 2026) from the University of California Los Angeles (UCLA). 

<span name="Funding">
At UCLA, <span name="NextName">NEXTNAME</span> receives funding from the Defense Advanced Research Projects Agency (DARPA) and the National Science Foundation (NSF) as a part of a quantum fellowship.
</span>

<span name="Education"> 
<span name="NextName">NEXTNAME</span> will (to be updated on May 18th, 2026) receive a B.A. and M.S. (2026) from the University of Pennsylvania (Penn) in physics.
</span>
</p>

<span name="Hobbies"> 
<span name="NextName">NEXTNAME</span> takes part in being an event supervisor and running tournaments for Science Olympiad. He has written tests for every single event you can think of except for the bio events. On the side, he enjoys playing and watching cricket, previously for the Club team at Penn and is looking to join a team in LA.
</span>

<p>
<span name="Social">
<span name="NextName">NEXTNAME</span>
posts as <a href="https://www.instagram.com/janguwangu/">@janguwangu</a>
and occasionally writes about life and other cool things at 
<a href="https://eclipticmaster.github.io/">eclipticmaster.github.io</a>.


<script>

// Interface elements
var IsFormal = document.getElementById("isformal") ;
var IsFunding = document.getElementById("isfunding") ;
var IsEducation = document.getElementById("iseducation") ;
var IsHobbies = document.getElementById("ishobbies")
var IsSocial = document.getElementById("issocial") ; 


// Interface manipulation 
function setAll(name,value) {

  var fields = document.getElementsByName(name);

  for (var i = 0; i < fields.length; ++i) {
    fields[i].innerText = value;
  }

}

function setAllVisibility(name,value) {

  var fields = document.getElementsByName(name);

  for (var i = 0; i < fields.length; ++i) {
    fields[i].style.display = value ? "inline" : "none" ;
  }

}

function refresh() {
  parseHash();
  updateAll();
}

function setSpoken() {
  window.location.hash = "isformal=0&isfunding=0&ishobbies=0&iseducation=0&issocial=0" ;
  refresh() ;
}


// parseHash: parses the #hash part of the URL and sets
// interface elements to match
function parseHash() {

  var hash = {} ;

  var params = window.location.hash.substring(1); 
    var vars = params.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
          hash[pair[0]] = pair[1] ;
    }

  IsFormal.checked = hash['isformal'] == "1" ? true : false ;
  IsFunding.checked = hash['isfunding'] == "1" ? true : false ;
  IsEducation.checked = hash['iseducation'] == "1" ? true : false ;
  IsHobbies.checked = hash['iseducation'] == "1" ? true : false ;
  IsSocial.checked = hash['issocial'] == "1" ? true : false ;

  updateAll() ;
}


// updateAll: updates the bio to match the interface elements:
function updateAll() {

  var hashParts = {} ;

  if (IsFormal.checked) {
    hashParts['isformal'] = "1" ;
    setAll("IntroName",'Mr. Manas Choure');
    setAll("NextName",'Mr. Choure');
  } else {
    hashParts['isformal'] = "0"; 
    setAll("IntroName",'Manas Choure') ;
    setAll("NextName",'Manas') ;
  }

  if (IsFunding.checked) {
    hashParts['isfunding'] = "1" ;
    setAllVisibility("Funding", true); 

  } else {
    hashParts['isfunding'] = "0"; 
    setAllVisibility("Funding", false); 
  }

  if (IsEducation.checked) {
    hashParts['iseducation'] = "1" ;
    setAllVisibility("Education", true); 

  } else {
    hashParts['iseducation'] = "0"; 
    setAllVisibility("Education", false); 
  }

  if (IsHobbies.checked) {
    hashParts['ishobbies'] = "1" ;
    setAllVisibility("Hobbies", true); 

  } else {
    hashParts['ishobbies'] = "0"; 
    setAllVisibility("Hobbies", false); 
  }

  if (IsSocial.checked) {
    hashParts['issocial'] = "1" ;
    setAllVisibility("Social", true); 

  } else {
    hashParts['issocial'] = "0"; 
    setAllVisibility("Social", false); 
  }




  // set the hash
  var newHash = "";
  var separator = "";
  for (var field in hashParts) {

    newHash = newHash + separator + field + "=" + hashParts[field]  ;
    separator = "&";
  }

  window.location.hash = newHash ;
}


// On page load:
parseHash() ;
updateAll() ;

</script>
