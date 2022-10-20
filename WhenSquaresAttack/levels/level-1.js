whenSquaresAttack.state1 = function(){};
whenSquaresAttack.state1.prototype = {
    count: {
        zombie: 0,
        numStars: 0,
        resetAll: function() {
            this.count.zombie = 0;
            this.count.numStars = 0;
        }
    },
    currentPhase: PHASE.PLAYING,
    fire: Object.assign({}, DEFAULT_FIRE),
    velocity: Object.assign({}, DEFAULT_VELOCITY),
    cursors: null,
    button: {
        play: null,
        pause: null,
        replay: null,
        music: null,
        nextLevel: null,
    },
    sprite: {
        // plural form to indicate a group
        player: null,
        bullets: null,
        zombies: null,
        stars: null,
    },
    sound: {
        zombieDeath: null,
        shoot: null,
    },
    map: null,
    mapLayer: {
        grass: null,
        bush: null,
    },
    display: {
        tip: null,
        totalStars: null,
    },
    preload: function(){
        game.load.tilemap('state1map', 'assets/tilemaps/state1map.json',null,Phaser.Tilemap.TILED_JSON);
        game.load.image('grassTile', 'assets/tilemaps/grassTile.png');
        game.load.image('bushTile', 'assets/tilemaps/bushTile.png');

        game.load.image('star','assets/sprites/star.png');
        game.load.image('player','assets/sprites/player.png');
        game.load.image('bullet','assets/sprites/bullet.png');


        game.load.image('replay', 'assets/buttons/replay.png');
        game.load.image('play', 'assets/buttons/play.png');
        game.load.image('pause', 'assets/buttons/pause.png');
        game.load.image('nextlevel', 'assets/buttons/nextlevel.png');
        game.load.image('MainMenu', 'assets/buttons/mainM.png');

        game.load.image('music', 'assets/buttons/music.png');

        game.load.spritesheet('zombie','assets/spritesheets/zombiesheet.png',64,64);

        //Sound Effects
        
    }, 
    create: function(){
        // init game
        game.physics.startSystem(Phaser.Physics.ARCADE);
        game.world.setBounds(0, 0, 1500, 1000);
        game.scale.scaleMode = Phaser.ScaleManager.SHOW_ALL;
        this.cursors = game.input.keyboard.createCursorKeys();

        // init sound
        this.sound.zombieDeath = game.add.audio('zombDeath', 0.2);
        this.sound.shoot = game.add.audio('shoot', 0.2);
        this.sound.star = game.add.audio('star', 0.2);
    
        // init map
        this.map = game.add.tilemap('state1map');
        this.map.addTilesetImage('grassTile');
        this.map.addTilesetImage('bushTile');

        this.mapLayer.grass = this.map.createLayer('Grass');
        this.mapLayer.bush = this.map.createLayer('Bushes');

        this.map.setCollisionBetween(2,20,true, 'Bushes');

        // init bullets
        this.sprite.bullets = game.add.group()
        this.sprite.bullets.createMultiple(50, 'bullet')
        this.sprite.bullets.setAll('checkWorldBounds', true)
        this.sprite.bullets.setAll('outOfBoundsKill', true)
        this.sprite.bullets.setAll('anchor.x', 0.5)
        this.sprite.bullets.setAll('anchor.y', 0.5)
        this.sprite.bullets.setAll('scale.x', 1)
        this.sprite.bullets.setAll('scale.y', 1)

        // init player: spawn at center
        this.sprite.player = game.add.sprite(CENTER_X, CENTER_Y, 'player');
        this.sprite.player.anchor.setTo(0.5, 0.5);
        this.sprite.player.enableBody = true;

        // init camera: enables game camera to follow player
        game.camera.follow(this.sprite.player);
        this.mapLayer.grass.fixedToCamera = false; 
        this.mapLayer.bush.fixedToCamera = false;
        game.camera.deadzone = new Phaser.Rectangle(CENTER_X - 200, 0, 600, 1000);
        
        // init zombies: spawn 5 randomly
        this.sprite.zombies = game.add.group();
        var coordinateExceptions = [{
            x: CENTER_X,
            x: [CENTER_X-20,CENTER_X+20],
            y: CENTER_Y,
            y: [CENTER_Y-20, CENTER_Y+20]
        }];
        for (var i = 0; i < 8; i++) {
            var newCoordinate = getRandCoordinateExcept(1500, 1000, 64, coordinateExceptions);
            coordinateExceptions.push(newCoordinate);
            var z = this.sprite.zombies.create(
                newCoordinate.x,
                newCoordinate.y,
                'zombie'
            );
            this.count.zombie += 1;
        }
        this.sprite.zombies.setAll('anchor.y', 0.5);
        this.sprite.zombies.setAll('anchor.x', 0.5);

        this.sprite.zombies.callAll('animations.add','animations','run',[1,2,3,4],10,true);
        this.sprite.zombies.callAll('animations.play','animations','run');

        // init stars: spawn 3 strategically
        this.sprite.stars = game.add.group();
        this.sprite.stars.create(1390, 240, 'star');
        this.sprite.stars.create(400, 560, 'star');
        this.sprite.stars.create(900, 330, 'star');

        // init text display
        game.add.text(CENTER_X, 10, 'Level 1', FONT_STYLE);
        this.display.totalStars = game.add.text(250, 10, "Total Stars: " + this.count.numStars, FONT_STYLE);
        this.display.tip = game.add.text(200, 100, '', {
            font: 'Orbitron',
            fontSize: 32,
            fill: '#ffffff',
        })
        this.display.tip.anchor.setTo(0, 0.5)

        // init physics
        game.physics.enable([this.sprite.zombies, this.sprite.player, this.sprite.bullets, this.sprite.stars]);
        this.sprite.player.body.collideWorldBounds = true;
        this.sprite.zombies.setAll('body.collideWorldBounds', true);

        // init buttons

        //button to go to the next level
        //Adding visibility to next level
        this.button.mainMenu = game.add.button(1400,30,"MainMenu", (function() {
            this.count.resetAll.call(this);
            game.state.start('main-menu');
            music.intro.stop();
        }).bind(this));
        this.button.mainMenu.scale.setTo(.1,.1);
        this.button.nextLevel = game.add.button(1400,950,'nextlevel', (function() {
            this.count.resetAll.call(this);
            this.currentPhase = PHASE.PLAYING;
            game.state.start('state2');
            this.button.nextLevel.visible = false;
        }).bind(this));
        addButtonStylesTo(this.button.nextLevel);
        this.button.nextLevel.visible = false;

        this.button.music = game.add.button(20,20,'music', function(){
            if (music.isPlaying == false) {
                music.intro.play();
                music.isPlaying = true;
            } else {
                music.intro.stop();
                music.isPlaying = false;
            }
        
        })
        this.button.replay = game.add.button(150, 100, 'replay', (function() {
            this.currentPhase = PHASE.PLAYING;
            this.count.resetAll.call(this);
            game.state.start('state1');
        }).bind(this));
        addButtonStylesTo(this.button.replay);
        this.button.replay.visible = false;

        this.button.pause = game.add.button(150, 100, 'pause', (function() {
            this.currentPhase = PHASE.PAUSED;
            this.animation.stopAll.call(this);
            this.display.tip.text = 'Paused';
            this.visible = false;
            game.time.events.pause();
        }).bind(this));
        addButtonStylesTo(this.button.pause);
        this.button.pause.visible = false;

        this.button.play = game.add.button(150, 100, 'play', (function() {
            this.currentPhase = PHASE.PLAYING;
            this.animation.startAll.call(this);
            this.display.tip.text = '';
            this.visible = false;
            game.time.events.resume();
        }).bind(this));
        addButtonStylesTo(this.button.play);
        this.button.play.visible = false;
    }, 
    update: function(){
        // phase: PLAYING
        if (this.currentPhase === PHASE.PLAYING) {
            // player & map: collision
            game.physics.arcade.collide(this.sprite.player, this.mapLayer.bush);
            game.physics.arcade.collide(this.sprite.player, this.mapLayer.pond, function(p, z) { 
                p.kill();
            });

            // bullets & map: collision
            game.physics.arcade.collide(this.sprite.bullets,[this.mapLayer.bush], function(p, z) { p.kill(); });
            
            // player: fire ability
            if (this.sprite.player.alive && game.input.activePointer.isDown) {
                this.animation.fire.call(this)
            }

            // player: rotate towards pointer
            this.sprite.player.rotation = game.physics.arcade.angleToPointer(this.sprite.player) + Math.PI / 4;

            // zombies: track player
            this.sprite.zombies.children.forEach(z => {
                z.rotation = game.physics.arcade.angleBetween(z, this.sprite.player) + Math.PI / 2;
                game.physics.arcade.moveToObject(z, this.sprite.player);
            })

            game.physics.arcade.overlap(this.sprite.player, this.sprite.stars, (function(player, star) {
                this.sound.star.play();
                star.kill();
                this.count.numStars += 1;
                this.display.totalStars.setText("Total Stars: "+ this.count.numStars);
            }).bind(this));

            // player: killed
            game.physics.arcade.overlap(this.sprite.player, this.sprite.zombies, function(p, z) { p.kill(); })
            game.physics.arcade.collide(this.sprite.player, this.mapLayer.bush, function(p, z) { p.kill(); })

            // zombies: killed
            game.physics.arcade.overlap(this.sprite.bullets, this.sprite.zombies, (function(b, z) {
                b.kill();
                z.kill();
                this.sound.zombieDeath.play();
                this.count.zombie -= 1;
            }).bind(this));

            // player: control movements
            if (this.cursors.up.isDown || game.input.keyboard.isDown(CURSORS_ALT.up)){
                this.sprite.player.body.velocity.y = -this.velocity.player;
            } else if (this.cursors.down.isDown || game.input.keyboard.isDown(CURSORS_ALT.down)) {
                this.sprite.player.body.velocity.y = this.velocity.player;
            } else {
                this.sprite.player.body.velocity.y = 0;
            }

            if (this.cursors.left.isDown || game.input.keyboard.isDown(CURSORS_ALT.left)){
                this.sprite.player.body.velocity.x = -this.velocity.player;
            } else if (this.cursors.right.isDown || game.input.keyboard.isDown(CURSORS_ALT.right)){
                this.sprite.player.body.velocity.x = this.velocity.player;
            } else {
                this.sprite.player.body.velocity.x = 0;
            }

            if (!this.button.pause.visible) {
                this.button.pause.visible = true;
            }

            // zombies: all dead (go to ENDED)
            if ((this.count.zombie === 0) && !this.button.replay.visible && this.count.numStars == 3) {
                this.currentPhase = PHASE.ENDED;
                this.animation.stopAll.call(this);

                this.button.play.visible = false;
                this.button.pause.visible = false;
                this.button.nextLevel.visible = true;
                this.display.tip.text = 'You have killed all zombies and acquired all the stars!';
            }
            
            // player: dead (go to ENDED)
            if ((!this.sprite.player.alive) && !this.button.replay.visible) {
                this.currentPhase = PHASE.ENDED;
                this.animation.stopAll.call(this);

                this.button.play.visible = false;
                this.button.pause.visible = false;
                this.button.nextLevel.visible = false;
                this.button.replay.visible = true;;
                this.display.tip.text = 'You\'re dead.';
            }
        }

        // phase: PAUSED
        if (this.currentPhase === PHASE.PAUSED) {
            this.button.play.visible = true;
        }
    },
    animation: {
        // tip: call these functions with `this.animation.someFunc.call(this)`
        startAll: function() {
            this.sprite.zombies.callAll('animations.play','animations','run');
        },
        stopAll: function() {
            this.sprite.player.body.velocity.setTo(0, 0);
            this.sprite.zombies.children.forEach(z => {
                z.animations.stop('run');
                z.body.velocity.x = 0;
                z.body.velocity.y = 0;
            })
        },
        fire: function() {
            if (game.time.now > this.fire.next) {
                this.sound.shoot.play();
                this.fire.next = game.time.now + this.fire.interval
                var bullet = this.sprite.bullets.getFirstDead()
                bullet.reset(this.sprite.player.x, this.sprite.player.y)
                game.physics.arcade.moveToPointer(bullet, this.velocity.bullet)
                bullet.rotation = game.physics.arcade.angleToPointer(bullet)
            }
        },
    },
};
