const monthEl = document.querySelector(".date h1");
const dateEl = document.querySelector(".date p");
const daysEl = document.querySelector(".days");
const prevButton = document.getElementById("prev");
const nextButton = document.getElementById("next");

let myDate = new Date();
let monthInx = myDate.getMonth();
const thisMonth = monthInx;
const thisYear = myDate.getFullYear();

dateEl.innerText = `today: ${myDate.toDateString()}`;

function updateCalender() {
  const lastDay = new Date(myDate.getFullYear(), monthInx + 1, 0).getDate();
  const firstDay = new Date(myDate.getFullYear(), monthInx, 1).getDay() - 1;
  const month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  console.log(firstDay);
  console.log(month[monthEl]);

  monthEl.innerText = month[monthInx];

  let days = "";

  for (let i = firstDay; i > 0; i--) {
    days += `<div class= "empty"></div>`;
  }

  for (let i = 1; i <= lastDay; i++) {
    if (
      i === myDate.getDate() &&
      monthInx === thisMonth &&
      myDate.getFullYear() === thisYear
    ) {
      days += `<div class= "today">${i}</div>`;
    } else {
      days += `<div>${i}</div>`;
    }
  }
  daysEl.innerHTML = days;
}

updateCalender();

prevButton.addEventListener("click", () => {
  monthInx--;
  if (monthInx === -1) {
    monthInx = 11;
    myDate.setFullYear(myDate.getFullYear() - 1);
  }
  updateCalender();
  console.log(monthInx);
});

nextButton.addEventListener("click", () => {
  monthInx++;
  if (monthInx === 12) {
    monthInx = 0;
    myDate.setFullYear(myDate.getFullYear() + 1);
  }
  updateCalender();
  console.log(monthInx);
});
