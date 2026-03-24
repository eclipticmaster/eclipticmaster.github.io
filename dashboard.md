---
layout: default
title: Stress Levels
permalink: /stress/
---

## Stress Levels

### Current Stress Level

<div id="stress-container">
  <div id="stress-bar"></div>
</div>

<p id="stress-label"></p>

---

### Stress Over Time

<canvas id="stressChart"></canvas>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
document.addEventListener("DOMContentLoaded", function () {

  const current = {{ site.data.current_stress | jsonify }};

  console.log("Current data:", current); // DEBUG

  const emails = Number(current.emails) || 0;
  const tasks = Number(current.tasks_due_3_days) || 0;
  const meetings = Number(current.meetings_this_week) || 0;

  const currentStress =
      0.5 * emails +
      3 * tasks +
      2 * meetings;

  console.log("Computed stress:", currentStress);

  const normalized = Math.min(currentStress, 100);

  const bar = document.getElementById("stress-bar");
  const label = document.getElementById("stress-label");

  bar.style.width = normalized + "%";

  if (normalized < 30) {
    bar.style.backgroundColor = "green";
    label.textContent = "Low stress";
  } else if (normalized < 60) {
    bar.style.backgroundColor = "goldenrod";
    label.textContent = "Moderate stress";
  } else {
    bar.style.backgroundColor = "darkred";
    label.textContent = "High stress";
  }

});
</script>