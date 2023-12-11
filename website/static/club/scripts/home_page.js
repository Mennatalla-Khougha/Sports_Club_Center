const eventEl = document.querySelector(".info.event");
const api = `http://${window.location.hostname}:5011/club_api/v1/tournaments/`;

fetch(api)
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    let currentDate = new Date();
    let event;
    let i = 0;
    while (new Date(data[i].date) >= currentDate) {
      i++;
    }
    if (i === 0) {
      event = data[0];
    } else {
      event = data[i - 1];
    }
    console.log(event);
    let text = `<h2 class="name">${event.name}</h2>`;
    let row = `<div class="row">`;
    row += `<img src="/static/club/images/tournaments/${event.id}.png" onerror="this.onerror=null; this.src='/static/club/images/tournaments/${event.sport}.png'" alt="${event.name}" />`;
    row += `<div class="text">`;
    if (event.description) row += `<p>${event.description}</p>`;
    row += `</div>`;
    row += `</div>`;
    text += row;

    eventEl.innerHTML = text;
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });
