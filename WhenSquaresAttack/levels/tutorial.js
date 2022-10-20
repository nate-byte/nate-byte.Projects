whenSquaresAttack.tutorial = function(){};
whenSquaresAttack.tutorial.prototype = {
    count: {
        zombie: 0,
        powerUp: 0,
        numStars: 0,
        resetAll: function() {
            this.count.zombie = 0;
            this.count.powerUp = 0;
            this.count.numStars = 0;
        }
    },
    currentPhase: PHASE.PLAYING,
    currentTutorialPhase: 1,
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
        crates: null,
        stars: null,
    },
    sound: {
        zombieDeath: null,
        shoot: null,
        powerUpContact: null,
        powerUpOn: null,
    },
    map: null,
    mapLayer: {
        grass: null,
        bush: null,
        pond: null,
    },
    display: {
        tip: null,
        totalPowerUps: null,
        totalStars: null,
        text1: null,
        text2: null,
        text3: null,
        text4: null,
    },
    tween: {
        powerUp: null,
    },
    preload: function(){
        game.load.tilemap('tutorialmap', 'assets/tilemaps/tutorialmap.json',null,Phaser.Tilemap.TILED_JSON);
        game.load.image('grassTile', 'assets/tilemaps/grassTile.png');
        game.load.image('bushTile', 'assets/tilemaps/bushTile.png');
        game.load.image('pondTile', 'assets/tilemaps/pondTile.png');

        game.load.image('crate','assets/sprites/Crate.png');
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
        this.sound.powerUpContact = game.add.audio('powerUp', 0.2);
        this.sound.powerUpOn = game.add.audio('power', 0.2);
        this.sound.star = game.add.audio('star', 0.2);
    
        // init map
        this.map = game.add.tilemap('tutorialmap');
        this.map.addTilesetImage('grassTile');
        this.map.addTilesetImage('bushTile');
        this.map.addTilesetImage('pondTile');

        this.mapLayer.grass = this.map.createLayer('Grass');
        this.mapLayer.bush = this.map.createLayer('Bushes');
        this.mapLayer.pond = this.map.createLayer('Ponds');

        this.map.setCollisionBetween(2,20,true, 'Bushes');
        this.map.setCollisionBetween(2,20,true, 'Ponds');

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
        this.mapLayer.pond.fixedToCamera = false;
        this.mapLayer.bush.fixedToCamera = false;
        game.camera.deadzone = new Phaser.Rectangle(CENTER_X - 200, 0, 600, 1000);
        
        // init zombies: spawn 1
        this.sprite.zombies = game.add.group();
        for (var i = 0; i < 1; i++) {
            var z = this.sprite.zombies.create(
                1400,
                200,
                'zombie'
            );
            this.count.zombie += 1;
        }
        this.sprite.zombies.setAll('anchor.y', 0.5);
        this.sprite.zombies.setAll('anchor.x', 0.5);

        this.sprite.zombies.callAll('animations.add','animations','run',[1,2,3,4],10,true);
        this.sprite.zombies.callAll('animations.play','animations','run');

        // init crates: spawn 1 stratigically
        this.sprite.crates = game.add.group();
        this.sprite.crates.create(200, 800, 'crate');

        // init stars: spawn 1 strategically
        this.sprite.stars = game.add.group();
        this.sprite.stars.create(1390, 840, 'star');

        // init text display
        game.add.text(CENTER_X, 10, 'Tutorial', FONT_STYLE);
        this.display.totalPowerUps = game.add.text(50, 10, "Power Ups: " + this.count.powerUp, FONT_STYLE);
        this.display.totalStars = game.add.text(250, 10, "Total Stars: " + this.count.numStars, FONT_STYLE);
        this.display.tip = game.add.text(200, 100, '', {
            font: 'Orbitron',
            fontSize: 32,
            fill: '#ffffff',
        })
        this.display.tip.anchor.setTo(0, 0.5)

        this.display.text1 = game.add.text(425,225, "Use arrow keys or W,A,S,D to move the player around the map to avoid drowning in a pond or getting murdered by a zombie. Press 2 to go to step 2.",FONT_STYLE);
        this.display.text1.visible = false;
        this.display.text2 = game.add.text(425,225, "Collect crates to gain speed power ups and press the space bar to use them.\nCollect stars to try and beat your high score!\nPress 3 to go to step 3.",FONT_STYLE);
        this.display.text2.visible = false;
        this.display.text3 = game.add.text(425,225, "Aim with your curser and click to shoot the zombies.",FONT_STYLE);
        this.display.text3.visible = false;
        this.display.text4 = game.add.text(425,225, "Kill all the zombies to win! Press NEXT LEVEL to continue.",FONT_STYLE);
        this.display.text4.visible = false;

        // init physics
        game.physics.enable([this.sprite.zombies, this.sprite.player, this.sprite.bullets, this.sprite.crates, this.sprite.stars]);
        this.sprite.player.body.collideWorldBounds = true;
        this.sprite.zombies.setAll('body.collideWorldBounds', true);

        // init buttons

        //button to go to the next level
        //Adding visibility to next level
        this.button.mainMenu = game.add.button(1400,30,"MainMenu", (function() {
            game.state.start('main-menu');
            music.intro.stop();
        }).bind(this));
        this.button.mainMenu.scale.setTo(.1,.1);
        this.button.nextLevel = game.add.button(1400,950,'nextlevel', (function() {
            this.currentPhase = PHASE.PLAYING;
            game.state.start('state1');
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
            this.velocity.player = 300;
            game.state.start('tutorial');
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
            // bullets & map: collision
            game.physics.arcade.collide(this.sprite.bullets,[this.mapLayer.bush,this.mapLayer.pond], function(p, z) { p.kill(); });
            
            if (this.currentTutorialPhase === 1) {
                this.display.text1.visible = true;
                enableMovementControl.call(this);
                if (game.input.keyboard.isDown(CURSORS_ALT.two)) {
                    this.currentTutorialPhase = 2;
                }
            } else if (this.currentTutorialPhase === 2) {
                this.display.text1.visible = false;
                this.display.text2.visible = true;
                enableMovementControl.call(this);
                enableUsingPowerUps.call(this);
                if (game.input.keyboard.isDown(CURSORS_ALT.three)) {
                    this.currentTutorialPhase = 3;      
                }
            } else if (this.currentTutorialPhase === 3) {
                this.display.text2.visible = false;
                this.display.text3.visible = true;
                enableZombieTrack.call(this);
                enableMovementControl.call(this);
                enableUsingPowerUps.call(this);
                enableFireAbility.call(this);
            }
            function enableFireAbility() {
                // player & map: collision
                game.physics.arcade.collide(this.sprite.player,this.mapLayer.bush);
                game.physics.arcade.collide(this.sprite.player, this.mapLayer.pond, function(p, z) { 
                    p.kill();
                    
                });
                // player: fire ability
                if (this.sprite.player.alive && game.input.activePointer.isDown) {
                    this.animation.fire.call(this);
                }
                
                // player: rotate towards pointer
                this.sprite.player.rotation = game.physics.arcade.angleToPointer(this.sprite.player) + Math.PI / 4;

                // player: killed
                game.physics.arcade.overlap(this.sprite.player, this.sprite.zombies, function(p, z) { 
                    console.log("yee");
                    p.kill(); })

                // zombies: killed
                game.physics.arcade.overlap(this.sprite.bullets, this.sprite.zombies, (function(b, z) {
                    b.kill();
                    z.kill();
                    this.sound.zombieDeath.play();
                    this.count.zombie -= 1;
                }).bind(this));
            }

            function enableZombieTrack(){
            // zombies: track player
            this.sprite.zombies.children.forEach(z => {
                z.rotation = game.physics.arcade.angleBetween(z, this.sprite.player) + Math.PI / 2;
                game.physics.arcade.moveToObject(z, this.sprite.player);
            })
            }

            function enableMovementControl() {
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
            }

            if (!this.button.pause.visible) {
                this.button.pause.visible = true;
            }

            function enableUsingPowerUps() {
                // player: using power ups (10 sec; player grows and shrinks; shoot and move faster)
                if (game.input.keyboard.isDown(Phaser.Keyboard.SPACEBAR) && (this.count.powerUp > 0)){
                    this.count.powerUp -= 1;
                    this.tween.powerUp = game.add.tween(this.sprite.player.scale).to({x: 1.5, y: 1.5}, 1000, Phaser.Easing.Linear.None, true, 0, 1000, true);
                    this.fire.interval /= 1.2;
                    this.velocity.player *= 1.2;
                    this.time.events.add(Phaser.Timer.SECOND * 10, (function(){
                        this.tween.powerUp.stop();
                        this.fire.interval *= 1.2;
                        this.velocity.player /= 1.2; 
                    }).bind(this));
                    this.display.totalPowerUps.setText("Power Ups: " + this.count.powerUp);
                }

                // player: collect power up
                game.physics.arcade.overlap(this.sprite.player, this.sprite.crates, (function(player, crate) {
                    this.sound.powerUpContact.play();
                    crate.kill();
                    this.count.powerUp += 1;
                    this.display.totalPowerUps.setText("Power Ups: "+ this.count.powerUp);
                }).bind(this));

                // player: collect stars
                game.physics.arcade.overlap(this.sprite.player, this.sprite.stars, (function(player, star) {
                    this.sound.star.play();
                    star.kill();
                    this.count.numStars += 1;
                    this.display.totalStars.setText("Total Stars: "+ this.count.numStars);
                }).bind(this));
            }

            // zombies: all dead (go to ENDED)
            if ((this.count.zombie === 0) && !this.button.replay.visible && this.count.numStars == 1) {
                this.currentPhase = PHASE.ENDED;
                this.animation.stopAll.call(this);

                this.button.play.visible = false;
                this.button.pause.visible = false;
                this.button.nextLevel.visible = true;
                this.display.tip.text = 'You have killed all zombies and accuired all the stars!';
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
            if (this.tween.powerUp) {
                this.tween.powerUp.stop()
            }
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
