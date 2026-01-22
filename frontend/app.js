

async function buildDay() {
  const actual = document.getElementById("actualWakeup").value;

  const res = await fetch("http://127.0.0.1:8000/plan/day", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      date: new Date().toISOString().slice(0,10),
      planned_wakeups: {
        sun: "07:00",
        mon: "07:00",
        tue: "07:00",
        wed: "07:00",
        thu: "07:00",
        fri: "08:30",
        sat: "08:30"
      },
      actual_wakeup: actual || null
    })
  });


  const data = await res.json();
  const ul = document.getElementById("schedule");
  ul.innerHTML = "";

  data.schedule.forEach(item => {
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

