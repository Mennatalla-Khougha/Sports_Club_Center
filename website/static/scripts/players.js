const playerEl = document.querySelector(".grid-container");
const selectEl = document.getElementById("sport");
const api = `http://${window.location.hostname}:5000/api/v1/players/`;
let playersHTML = {};

playersHTML["All"] = "";

fetch(api)
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    data.sort((a, b) => {
      if (a.first_name < b.first_name) return -1;
      if (a.first_name > b.first_name) return 1;

      if (a.last_name < b.last_name) return -1;
      if (a.last_name > b.last_name) return 1;

      return 0;
    });
    for (const player of data) {
      let text = `<div class="item_player">`;
      text += `<a href="/players/${player.id}"><h2>${player.first_name} ${player.last_name}</h2></a>`;
      text += `<p>${player.age} years old ${player.sport} player, participated in ${player.played_tournaments} tournaments.</p>`;
      text += `<img src="../static/personal_images/${player.id}.png" onerror="this.onerror=null; this.src='../static/personal_images/no_pic.png'" alt="${player.sport} player" />`;
      text += `</div>`;
      playersHTML["All"] += text;
      if (playersHTML[player.sport_id] !== undefined) {
        playersHTML[player.sport_id] += text;
      } else {
        playersHTML[player.sport_id] = text;
      }
    }
    playerEl.innerHTML = playersHTML["All"];

    selectEl.addEventListener("change", () => {
      playerEl.innerHTML = playersHTML[selectEl.value];
    });
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });
