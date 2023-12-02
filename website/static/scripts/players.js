const playerEl = document.querySelector(".grid-container");
const selectEl = document.getElementById("sport");
const api = `http://${window.location.hostname}:5000/api/v1/`;
let playersData;
let sportData;
let sports;

fetch(api + "players")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    playersData = data;
    console.log(data);
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });

fetch(api + "players")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    sportData = data;
    console.log(data);
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });
for (const sport of sportData) {
  sports[sport.id] = sport.name;
}

selectEl.addEventListener("change", () => {
  const value = selectEl.value;
  let players = "";
  for (const player of playersData) {
    if (value === "All" || value === player.id)
      players += `<div class="item_player">`;
    players += `<a href="/players/${player.id}"><h2>${player.first_name} ${player.last_name}</h2></a>\n`;
    players += `<p>${player.age} years old ${
      sports[player.sport_id]
    } player, participated in ${player.played_tournaments} tournaments.</p>`;
    players += `<img src="../static/personal_images/${
      player.id
    }.png" onerror="this.onerror=null; this.src='../static/personal_images/no_pic.png'" alt="${
      sports[player.sport_id]
    } player" />`;
  }
  playerEl.innerHTML = players;
});
