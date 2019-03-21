/* ====== Thanks ====== */

function renderThanks() {
  const topJson = localStorage.getItem('topData');

  const creature = !!topJson ? CreatureDOM(JSON.parse(topJson)) : document.createElement('div');

  document.getElementById('container').appendChild(creature);
}

/* ====== Main ====== */

window.addEventListener("load", () => {
  renderThanks();
});