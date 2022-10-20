whenSquaresAttack.example = function(){};
whenSquaresAttack.example.prototype = {
    // define local variables
    preload: function(){
        // load assets
    }, 
    create: function(){
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
