let mockJson = JSON.parse(createMockJson());
let selectedIndexes = [];


/* ====== Train ====== */

function renderTrain() {
  const oldContainer = document.getElementById('container');
  if (!!oldContainer) {
    document.getElementsByClassName('main')[0].removeChild(oldContainer);
  }
  const container = document.createElement('div');
  container.id = 'container';
  document.getElementsByClassName('main')[0].appendChild(container);

  const trainDOMs = mockJson.map((data, index) => TrainDOM(data, index));
  trainDOMs.forEach(dom => document.getElementById('container').appendChild(dom));

  // 全部選択完了した時の処理
  if (selectedIndexes.length === 5) {

    // データ送信
    const dataForSend =
      [
        mockJson[selectedIndexes[0]],
        mockJson[selectedIndexes[1]],
        mockJson[selectedIndexes[2]],
        mockJson[selectedIndexes[3]],
        mockJson[selectedIndexes[4]]
      ]
        .map((data, i) => ({...data, rank: 5 - i}));

    console.log("send-data-content", dataForSend);
    $.ajax({
      url: 'http://crazy-pets.grouchydev.io/api',
      type: 'post',
      contentType: "application/json",
      data: JSON.stringify(dataForSend)
    })
      .done(() => {
        console.log('送信完了！');
        const topIndex = selectedIndexes[0];
        const topDataJson = JSON.stringify(mockJson[topIndex]);
        localStorage.setItem('topData', topDataJson);
        location.href = 'thanks.html';
      })
      .fail(() => {
        console.log('送信エラー！')
      });
  }
}

function TrainDOM(data, index) {
  const isSelected = selectedIndexes.some(selectedIndex => selectedIndex === index);


  const container = document.createElement('div');
  container.style.position = 'relative';

  const creatureDOM = CreatureDOM(data);
  creatureDOM.onclick = isSelected ? () => {
  } : onSelect(index);
  creatureDOM.style.cursor = 'pointer';

  const effectArea = document.createElement('div');
  effectArea.style.width = '100%';
  effectArea.style.height = '60px';
  effectArea.style.textAlign = 'center';
  effectArea.style.marginTop = '-36px';

  const rankContainer = document.createElement('div');
  rankContainer.className = 'lank_text';
  rankContainer.style.width = '100%';
  rankContainer.style.height = '60px';
  rankContainer.style.textAlign = 'center';
  rankContainer.style.marginTop = '-36px';

  const rankText = document.createElement('span');
  rankText.textContent =
    isSelected
      ? selectedIndexes
        .map((selectedIndex, rankMinus1) => [selectedIndex, rankMinus1 + 1])
        .filter(tuple => tuple[0] === index)
        .map(([selectedIndex, rank]) => rank)[0]
      : '';

  // 表示/非表示
  rankContainer.style.display = isSelected ? 'block' : 'none';

  container.appendChild(creatureDOM);
  container.appendChild(rankContainer);
  rankContainer.appendChild(rankText);
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
function main() {
  if (!!window.gotData) {
    renderTrain()
  } else {
    setTimeout(() => {
      main();
    }, 100);
  }
}

window.addEventListener("load", () => {
  main();
});
