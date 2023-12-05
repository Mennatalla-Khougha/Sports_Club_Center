const eventEl = document.querySelector(".info_event_wraper");
const api = `http://${window.location.hostname}:5000/api/v1/tournaments/`;

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
    let text = `<article class="info_event">`;
    text += `<img src="../static/tournaments_images/${event.id}.png" onerror="this.onerror=null; this.src='../static/tournaments_images/${event.sport}.png'" alt="${event.name}" />`;
    text += `<div class="text">`;
    text += `<h2 class="name">${event.name}</h2>`;
    if (event.description) text += `<p>${event.description}</p>`;
    text += `</div>`;
    text += `</article>`;

    eventEl.innerHTML = text;
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });
