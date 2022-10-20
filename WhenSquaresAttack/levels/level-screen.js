whenSquaresAttack.levelScreen = function(){};
whenSquaresAttack.levelScreen.prototype = {
    // define local variables
    preload: function(){
        // load assets
        game.load.image('levelscreen', 'assets/tilemaps/levelscreen.png');
        game.load.image('Level 1', 'assets/buttons/Level 1.png');
        game.load.image('Level 2', 'assets/buttons/Level 2.png');
        game.load.image('Level 3', 'assets/buttons/Level 3.png');
        game.load.image('Level 4', 'assets/buttons/Level 4.png');
        game.load.image('Level 5', 'assets/buttons/Level 5.png');
        
    }, 
    create: function(){
        game.scale.scaleMode = Phaser.ScaleManager.SHOW_ALL;
        var levelscreen = game.add.sprite(0,0,'levelscreen');

        createButton(game,'Level 1', 250, 250, 200, 200, function(){
            music.intro.play();
            music.isPlaying = true;
            game.state.start('state1');
        });

        createButton(game,'Level 2', 250, 750, 200, 200, function(){
            music.intro.play();
            music.isPlaying = true;
            game.state.start('state2');
        });

        createButton(game,'Level 3', 750, 500, 200, 200, function(){
            music.intro.play();
            music.isPlaying = true;
            game.state.start('state3');
        });

        createButton(game,'Level 4', 1250, 250, 200, 200, function(){
            music.intro.play();
            music.isPlaying = true;
            game.state.start('state4');
        });

        createButton(game,'Level 5', 1250, 750, 200, 200, function(){
            music.intro.play();
            music.isPlaying = true;
            game.state.start('state5');
        });
        // init game
        // init sound
        // init map
        // init bullets
        // init player: spawn at center
        // init camera: enables game camera to follow player
        // init zombies: spawn 10 randomly
        // init crates: spawn 3 randomly
        // init text display
        // init physics
        // init buttons
    }, 
    update: function(){
        // phase: PLAYING
            // player & map: collision
            // player: fire ability
            // player: rotate towards pointer
            // zombies: track player
            // player: collect power up
            // player: killed
            // zombies: killed
            // player: control movements
            // zombies: all dead (go to ENDED)
            // player: dead (go to ENDED)
            // player: using power ups (10 sec; player grows and shrinks; shoot and move faster)
        // phase: PAUSED
    },
    // define functions
};
