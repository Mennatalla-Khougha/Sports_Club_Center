const monthEl = document.querySelector(".date h1");
const dateEl = document.querySelector(".date p");
const daysEl = document.querySelector(".days");
const selectEl = document.getElementById("sport");
const prevButton = document.getElementById("prev");
const nextButton = document.getElementById("next");
const urlParams = new URLSearchParams(window.location.search);
const api = `http://${window.location.hostname}:5000/api/v1/tournaments/`;
let paramsApi = `http://${window.location.hostname}:5000/api/v1/players/`;

let myDate = new Date();
let monthInx = myDate.getMonth();
const thisMonth = monthInx;
const thisYear = myDate.getFullYear();
let selected = "All";

let tournamentsList = {};
tournamentsList["All"] = [];

const classes = {
  Karate: "karate",
  Squash: "squash",
  "Track & Field": "track",
};

dateEl.innerText = `today: ${myDate.toDateString()}`;

function countTournaments(day, tournaments) {
  let formattedDay = `${myDate.getFullYear()}-`;
  if (monthInx + 1 < 10){
    formattedDay += "0";
  }
  formattedDay += `${monthInx + 1}-`
  if (day < 10){
    formattedDay += "0";
  }
  formattedDay += `${day}`
  return tournaments.filter((tournament) =>
    tournament.date.startsWith(formattedDay)
  );
}

function updateCalender(dates) {
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

  monthEl.innerText = `${month[monthInx]} ${myDate.getFullYear()}`;

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
      days += `<div class= "day today"><p>${i}</p>`;
    } else {
      days += `<div class= "day"><p>${i}</p>`;
    }
    days += `<div class= "circle-container">`;
    let tournaments = countTournaments(i, dates);
    for (const tournament of tournaments) {
      days += `<div class= "circle ${classes[tournament.sport]}"></div>`;
    }
    days += "</div></div>";
  }
  daysEl.innerHTML = days;
}

if (urlParams.has("id")) {
  console.log(urlParams.get("id"));
  paramsApi += `${urlParams.get("id")}/tournaments`;
  fetch(paramsApi)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      selected = urlParams.get("type");
      tournamentsList[selected] = data;
      updateCalender(data);
      console.log(data);
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });
}

fetch(api)
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    for (const tournament of data) {
      tournamentsList["All"].push(tournament);
      if (tournamentsList[tournament.sport] !== undefined) {
        tournamentsList[tournament.sport].push(tournament);
      } else {
        tournamentsList[tournament.sport] = [tournament];
      }
    }
    if (!urlParams.has("id")) {
      if (urlParams.has("type")) {
        selectEl.selectedIndex = urlParams.get("type");
        const changeEvent = new Event('change');
        selectEl.dispatchEvent(changeEvent);
      } else {
        updateCalender(tournamentsList["All"]);
      }
    }
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });

selectEl.addEventListener("change", () => {
  selected = selectEl.value;
  updateCalender(tournamentsList[selected]);
});

prevButton.addEventListener("click", () => {
  monthInx--;
  if (monthInx === -1) {
    monthInx = 11;
    myDate.setFullYear(myDate.getFullYear() - 1);
  }
  updateCalender(tournamentsList[selected]);
});

nextButton.addEventListener("click", () => {
  monthInx++;
  if (monthInx === 12) {
    monthInx = 0;
    myDate.setFullYear(myDate.getFullYear() + 1);
  }
  updateCalender(tournamentsList[selected]);
});
