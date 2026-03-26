fetch('/_data/stress.json')
  .then(response => response.json())
  .then(data => {

    const currentStress =
      0.3 * unread_emails +
      1.5 * emails +
      3 * tasks +
      2 * meetings;

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