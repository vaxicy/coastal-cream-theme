// Coastal Cream Theme — sea blue, warm sand and mint
import { readFile } from 'node:fs/promises';

const COASTAL_PALETTE = {
  sky: '#A6D3EF',
  sea: '#4E86A8',
  sand: '#FEE6BB',
  mint: '#CEE2D0',
  cream: '#FDF9F7',
};

export class TideChart {
  constructor(place = 'Quiet cove') {
    this.place = place;
    this.palette = COASTAL_PALETTE;
  }

  /** Mix two coastal colors into a washed-out shade. */
  mix(from, to, ratio = 0.5) {
    const parse = (hex) =>
      [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channel = (value, i) =>
      Math.round(value * (1 - ratio) + b[i] * ratio);
    const toHex = (value) => value.toString(16).padStart(2, '0');
    return '#' + a.map(channel).map(toHex).join('');
  }

  async readTide(file) {
    const content = await readFile(file, 'utf8');
    const readings = content.split('\n').filter(Boolean);
    return {
      place: this.place,
      bands: Object.keys(this.palette).length,
      readings: readings.length,
      content,
    };
  }
}

const chart = new TideChart();
const foam = chart.mix(COASTAL_PALETTE.sea, COASTAL_PALETTE.cream);

console.log(`foam shade: ${foam}`);
