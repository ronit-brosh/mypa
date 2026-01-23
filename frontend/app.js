const API = "http://127.0.0.1:8000";

document.addEventListener("DOMContentLoaded", init);

async function init() {
  const res = await fetch(`${API}/wakeup-times`);
  const wakeups = await res.json();

  const todayKey = getTodayKey(); // sun / mon / ...
  const planned = wakeups[todayKey];

  if (planned) {
    document.getElementById("actualWakeup").value = planned;
  }
}

function renderDayTitle() {
  const now = new Date();

  const daysHe = [
    "יום ראשון",
    "יום שני",
    "יום שלישי",
    "יום רביעי",
    "יום חמישי",
    "יום שישי",
    "יום שבת"
  ];

  const dayName = daysHe[now.getDay()];
  const dateStr = now.toLocaleDateString("he-IL");

  document.getElementById("dayTitle").textContent =
    `${dayName} · ${dateStr}`;
}

renderDayTitle();


async function buildDay() {
  const actual = document.getElementById("actualWakeup").value;

  const res = await fetch(`${API}/plan/day`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      date: new Date().toISOString().slice(0, 10),
      actual_wakeup: actual
    })
  });

  const data = await res.json();

  const ul = document.getElementById("schedule");
  ul.innerHTML = "";

  data.schedule
    .sort((a, b) => a.start.localeCompare(b.start))
    .forEach(item => {

    const li = document.createElement("li");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";

    const label = document.createElement("span");
    label.textContent = ` ${item.start}–${item.end}  ${item.name}`;

    li.appendChild(checkbox);
    li.appendChild(label);
    ul.appendChild(li);
  });
}

function getTodayKey() {
  const days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"];
  return days[new Date().getDay()];
}
