function getBackground() {
  const seed = Math.round(0xffffff * Math.random());
  const r = seed >> 16;
  const g = (seed >> 8) & 255;
  const b = seed & 255;

  return { r, g, b };
}

function getForeground({ r, g, b }) {
  return r * 0.299 + g * 0.587 + b * 0.114 > 186
    ? { b: 255, w: 0 }
    : { b: 0, w: 255 };
}

function generateTrainingSet() {
  const json = { colors: [] };

  for (let i = 0; i < 10000; i++) {
    const background = getBackground();
    const foreground = getForeground(background);
    const data = { background, foreground };

    json.colors.push(data);
  }

  console.log(JSON.stringify(json));
}

function generatePredictionSet() {
  const json = { colors: [] };

  for (let i = 0; i < 10; i++) {
    const background = getBackground();
    const data = { background };

    json.colors.push(data);
  }

  console.log(JSON.stringify(json));
}

generatePredictionSet();
