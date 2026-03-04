fetch('/_data/stress.json')
  .then(response => response.json())
  .then(data => {

    const stress =
      0.5 * data.emails +
      3 * data.tasks_due_3_days +
      2 * data.meetings_this_week;

    const normalized = Math.min(stress, 100);

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