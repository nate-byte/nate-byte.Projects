# When Squares Attack

Work of CS 329E Spring 2021 - Team 3

## Development

![](https://i.loli.net/2021/04/11/GlHIuFzBMtcoJrT.jpg)

### State management

There are 2 kinds of variables: **global variables** and **local variables**.

#### Global variables

- Global variables are variables that are shared among all game states.
- Define them in `globalStates.js`. Follow the [naming convention](#Naming%20convention).

#### Local variables

- Local variables are variables that are specific to one game state, or not suitable to be defined as global variables (i.e. variables that uses `game` object, which is only accessible inside a game state).
- Follow the [naming convention](#Naming%20convention).
- How to define and access a local variable:
  1. Inside the `prototype` object of a game state, define them as key-value pairs just like `preload` function.
  2. For variables without an initial value, give them a `null` value. This is more like a convention than requirement, so that we can keep a list of local variables at the top.

```js
demo.state1 = function() {};
demo.state1.prototype = {
  greeting: 'Hello world.',
  cursors: null,
  preload: function() {
    // access them in `this` object
    // the following code prints 'Hello world' in the console when the game state runs.
    console.log(this.greeting)

    // assign value to variables with no initial value
    this.cursors = game.input.keyboard.createCursorKeys();
    // ...
  },
  create: function() {
    // ...
  },
  update: function() {
    // ...
  }
}
```

### Files

```bash
.
├── globalStates.js   # all global variables and constants
├── utils.js          # all utility functions
└── state1.js         # State 1: Game
```

### Naming convention

- Variables: [camelCase](https://en.wikipedia.org/wiki/Camel_case), ex `thisIsMyVariable`.
- Constants: all-upper [SNAKE_CASE](https://en.wikipedia.org/wiki/Snake_case), ex `THIS_IS_MY_CONSTANT`.

## Arts

Put them in the subdirectory of `assets` accordingly.

Naming convention of files: [camelCase](https://en.wikipedia.org/wiki/Camel_case). Don't include symbols and spaces.

```bash
.
├── assets
│  ├── audios
│  ├── backgrounds
│  ├── buttons
│  ├── sprites
│  ├── spritesheets
│  └── tilemaps
```

### Music

1. Intro - @nate-byte

### Images

Sprites, spritesheets, tilemaps, buttons ...
