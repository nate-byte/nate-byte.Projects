var CENTER_X = 1500 / 2;
var CENTER_Y = 1000 / 2;
var DOUBLE_SPEED = 800;

// Do not change the reference of the following objects of constants directly.
// Make a copy of them. i.e. `Object.assign({}, DEFAULT_VELOCITY)`

// Alternative cursors: WASD
var CURSORS_ALT = {
  up: Phaser.KeyCode.W,
  left: Phaser.KeyCode.A,
  down: Phaser.KeyCode.S,
  right: Phaser.KeyCode.D,
  one: Phaser.KeyCode.ONE,
  two: Phaser.KeyCode.TWO,
  three: Phaser.KeyCode.THREE,
  four: Phaser.KeyCode.FOUR,
}

var DEFAULT_VELOCITY = {
  player: 300,
  bullet: 1000,
}

var DEFAULT_FIRE = {
  next: 0,
  interval: 300,
}

var FONT_STYLE = {
  font: "22px Orbitron",
  fill: 'white',
  align: 'left',
  wordWrap:true,
  wordWrapWidth: 750
};

var PHASE = {
  PLAYING: 0,
  PAUSED: 1,
  ENDED: 2,
}

var music = {
  intro: null,
  isPlaying: true,
  wasPlaying: false,
}
