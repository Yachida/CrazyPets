function CreatureDOM(data) {
  const topMargin = 40;
  const container = document.createElement('div');
  container.style.position = 'relative';

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

  container.appendChild(base);
  container.appendChild(eyeLeft);
  container.appendChild(eyeRight);
  container.appendChild(nose);
  container.appendChild(mouth);

  return container;
}