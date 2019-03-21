/* ====== Home ====== */

function renderHome() {
  // 対象ランクはランダムに選定
  const targetRank = Math.floor(Math.random() * 5) + 1;
  console.log('targetRank', targetRank);

  const message = document.getElementsByClassName('main_title')[0];
  message.textContent = (() => {
    if (targetRank === 1) {
      return "出てけー！！！！！（でもまた来てね。）"
    } else if (targetRank === 2) {
      return "月曜の朝6時の気分です。また来てほしいぞ。"
    } else if (targetRank === 3) {
      return "居るのは別にいいけど、構ってやれないぞ。"
    } else if (targetRank === 4) {
      return "飯でも行こか。今日は魚の気分。"
    } else if (targetRank === 5) {
      return "遊びに来てくれたの！？何する！？何する！？駅伝！？"
    }
  })();


  const targetJson = window.gotData.filter(data => data.score === targetRank)[0];

  const creature = !!targetJson ? CreatureDOM(targetJson) : document.createElement('div');

  document.getElementById('container').appendChild(creature);
}

/* ====== Main ====== */

function main() {
  if (!!window.gotData) {
    renderHome()
  } else {
    setTimeout(() => {
      main();
    }, 100);
  }
}

window.addEventListener("load", () => {
  main();
});
