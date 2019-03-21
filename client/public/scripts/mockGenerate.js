/* ======== JSON ========*/

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

// CSV生成時に実行
function outputMockJson() {
  console.log(createMockJson());
}


/* ======== CSV ========*/

function outputCSV() {
  const columns = () => new Array(8).fill(0).map((_, i) => {
    if (i === 0) {
      return Math.random() / 2
    } else if (i === 1) {
      return Math.random() / 2
    } else if (i === 2) {
      return Math.random() / 2 + 0.65
    } else if (i === 3) {
      return Math.random() / 2
    } else if (i === 4) {
      return Math.random() / 2 + 0.25
    } else if (i === 5) {
      return Math.random() / 2 + 0.25
    } else if (i === 6) {
      return Math.random() / 2 + 0.25
    } else if (i === 7) {
      return Math.random() / 3 + 0.7
    }
  }).join(",");
  const rows = new Array(300).fill(0).map(columns).join("\n");
  console.log(rows);
}