function createMockJson() {
  const row = () => new Array(8).fill(0).map(() => Math.random());

  const objs =
    new Array(5)
      .fill(0)
      .map(row)
      .map((cols, i) => ({
        eye_left_x: cols[0],
        eye_left_y: cols[1],
        eye_right_x: cols[2],
        eye_right_y: cols[3],
        nose_x: cols[4],
        nose_y: cols[5],
        mouth_x: cols[6],
        mouth_y: cols[7],
        score: i + 1,
      }));

  return JSON.stringify(objs);
}

function outputMockJson() {
  console.log(createMockJson());
}


/* ====== States ====== */

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
  const topMargin = 40;

  const div = document.createElement('div');
  div.style.position = 'relative';
  div.style.float = 'left';
  div.onclick = isSelected ? () => {
  } : onSelect(index);
  div.style.cursor = 'pointer';


  const base = document.createElement('img');
  base.src = './img/base.png';

  const eyeLeft = document.createElement('img');
  eyeLeft.src = './img/eye_left.png';
  eyeLeft.style.position = 'absolute';
  eyeLeft.style.zIndex = '2';
  eyeLeft.style.left = String(data.eye_left_x * 120);
  eyeLeft.style.top = String(topMargin + data.eye_left_y * 180);

  const eyeRight = document.createElement('img');
  eyeRight.src = './img/eye_right.png';
  eyeRight.style.position = 'absolute';
  eyeRight.style.zIndex = '2';
  eyeRight.style.left = String(data.eye_right_x * 120);
  eyeRight.style.top = String(topMargin + data.eye_right_y * 180);

  const nose = document.createElement('img');
  nose.src = './img/nose.png';
  nose.style.position = 'absolute';
  nose.style.zIndex = '2';
  nose.style.left = String(data.nose_x * 120);
  nose.style.top = String(topMargin + data.nose_y * 180);

  const mouth = document.createElement('img');
  mouth.src = './img/mouth.png';
  mouth.style.position = 'absolute';
  mouth.style.zIndex = '2';
  mouth.style.left = String(data.mouth_x * 120);
  mouth.style.top = String(topMargin + data.mouth_y * 180);

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

  div.appendChild(base);
  div.appendChild(eyeLeft);
  div.appendChild(eyeRight);
  div.appendChild(nose);
  div.appendChild(mouth);
  div.appendChild(effectArea);
  effectArea.appendChild(rankText);
  return div;
}

function onSelect(index) {
  return () => {
    selectedIndexes.push(index);
    // 再描画
    renderTrain();
  }
}


/* ====== Thanks ====== */

// function renderThanks() {
//   const oldContainer = document.getElementById('container');
//   if (!!oldContainer) {
//     document.body.removeChild(oldContainer);
//   }
//   const container = document.createElement('div');
//   container.id = 'container';
//   document.body.appendChild(container);
//   const thanksDOM = ThanksDOM();
//   document.getElementById('container').appendChild(thanksDOM)
// }
//
// function ThanksDOM() {
//   const div = document.createElement('div');
//   div.style.position = 'relative';
//   div.style.float = 'left';
//   div.style.cursor = 'pointer';
//   div.textContent = 'ありがとうございました';
//
//   const BackContainer = document.createElement('div');
//   const backButton = document.createElement('button');
//   backButton.textContent = 'もう一度訓練する';
//   backButton.onclick = () => {
//     selectedIndexes = [];
//     mockJson = JSON.parse(createMockJson());
//     renderTrain();
//   };
//
//   div.appendChild(BackContainer);
//   BackContainer.appendChild(backButton);
//
//   return div;
// }


/* ====== Utility ====== */


// 丸めた文字列
function roundedStr(num) {
  return String(num).slice(0, 4);
}

function updateParts(eyeLeftX, eyeLeftY, eyeRightX, eyeRightY, noseX, noseY, mouthX, mouthY) {

  console.log(`${roundedStr(eyeLeftX)}, ${roundedStr(eyeLeftY)}, ${roundedStr(eyeRightX)}, ${roundedStr(eyeRightY)}, ${roundedStr(noseX)}, ${roundedStr(noseY)}, ${roundedStr(mouthX)}, ${roundedStr(mouthY)}`);

  updatePart('eye_left', eyeLeftX * 200, eyeLeftY * 200);
  updatePart('eye_right', eyeRightX * 200, eyeRightY * 200);
  updatePart('nose', noseX * 200, noseY * 200);
  updatePart('mouth', mouthX * 200, mouthY * 200);
}

function updatePart(id, left, top) {
  const part = document.getElementById(id);
  part.style.left = left;
  part.style.top = top;
}


/* ====== Main ====== */

window.addEventListener("load", () => {
  // outputMockJson();
  renderTrain();
});