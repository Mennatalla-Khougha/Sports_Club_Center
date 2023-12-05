const tournamentEl = document.querySelector(".grid-container");
const selectEl = document.getElementById("sport");
const api = `http://${window.location.hostname}:5000/api/v1/tournaments/`;
let tournamentsHTML = {};

tournamentsHTML["All"] = "";

fetch(api)
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    for (const tournament of data) {
      let text = `<div class="grid_item">`;
      text += `<a href="/tournaments/${tournament.id}"><h2>${tournament.name}</h2></a>`;
      text += `<p>A ${tournament.sport} tournament, for age range: ${tournament.age_range}<br>`;
      text += `Date: ${tournament.date}</p>`;
      text += `<img src="../static/tournaments_images/${tournament.id}.png" onerror="this.onerror=null; this.src='../static/tournaments_images/${tournament.sport}.png'" alt="${tournament.sport} Tournament" />`;
      text += `</div>`;
      tournamentsHTML["All"] += text;
      if (tournamentsHTML[tournament.sport_id] !== undefined) {
        tournamentsHTML[tournament.sport_id] += text;
      } else {
        tournamentsHTML[tournament.sport_id] = text;
      }
    }
    tournamentEl.innerHTML = tournamentsHTML["All"];

    selectEl.addEventListener("change", () => {
      tournamentEl.innerHTML = tournamentsHTML[selectEl.value];
    });
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });
