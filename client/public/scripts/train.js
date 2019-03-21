let mockJson = JSON.parse(createMockJson());
let selectedIndexes = [];


/* ====== Train ====== */

function renderTrain() {
  const oldContainer = document.getElementById('container');
  if (!!oldContainer) {
    document.body.removeChild(oldContainer);
  }
  const container = document.createElement('div');
  container.id = 'container';
  document.body.appendChild(container);

  const trainDOMs = mockJson.map((data, index) => TrainDOM(data, index));
  trainDOMs.forEach(dom => document.getElementById('container').appendChild(dom));

  if (selectedIndexes.length === 5) {
    setTimeout(() => {
      location.href = 'thanks.html';
    }, 1000)
  }
}

function TrainDOM(data, index) {
  const isSelected = selectedIndexes.some(selectedIndex => selectedIndex === index);


  const container = document.createElement('div');
  container.style.position = 'relative';
  container.style.float = 'left';

  const creatureDOM = CreatureDOM(data);
  creatureDOM.onclick = isSelected ? () => {
  } : onSelect(index);
  creatureDOM.style.cursor = 'pointer';

  const effectArea = document.createElement('div');
  effectArea.style.width = '100%';
  effectArea.style.height = '60px';
  effectArea.style.textAlign = 'center';
  effectArea.style.marginTop = '-36px';

  const rankText = document.createElement('span');
  rankText.textContent =
    isSelected
      ? selectedIndexes
      .map((selectedIndex, rankMinus1) => [selectedIndex, rankMinus1 + 1])
      .filter(tuple => tuple[0] === index)
      .map(([selectedIndex, rank]) => rank)[0] + '位'
      : '';
  rankText.style.display = isSelected ? 'block' : 'none';
  rankText.style.fontSize = '25px';
  rankText.style.fontWeight = '900';

  container.appendChild(creatureDOM);
  container.appendChild(effectArea);
  effectArea.appendChild(rankText);
  return container;
}

function onSelect(index) {
  return () => {
    selectedIndexes.push(index);
    // 再描画
    renderTrain();
  }
}


/* ====== Main ====== */

window.addEventListener("load", () => {
  // outputMockJson();
  renderTrain();
});