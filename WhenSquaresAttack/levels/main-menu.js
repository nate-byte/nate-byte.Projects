var whenSquaresAttack = {};
whenSquaresAttack.mainMenu = function(){};
whenSquaresAttack.mainMenu.prototype = {
    preload: function(){
        game.load.image('titlescreen', 'assets/tilemaps/titlescreen.png');
        game.load.image('MainPlay', 'assets/buttons/MainPlay.png');
        game.load.image('Levels', 'assets/buttons/levels.png');
        game.load.image('HowTo', 'assets/buttons/HowTo.png');
        game.load.audio('intro', 'assets/audios/introMusic.mp3');
        game.load.audio('zombDeath', 'assets/audios/zombieDeath.wav');
        game.load.audio('shoot', 'assets/audios/pistol.ogg');
        game.load.audio('powerUp', 'assets/audios/powerUpContact.wav')
        game.load.audio('power', 'assets/audios/poweronfx.wav');
        game.load.audio('star', 'assets/audios/star.wav');
    }, 
    create: function(){
        game.scale.scaleMode = Phaser.ScaleManager.SHOW_ALL;
        var titlescreen = game.add.sprite(0,0,'titlescreen');
        // intro music
        music.intro = game.add.audio('intro', 0.4, true); // 40% volume, loop

        createButton(game,'MainPlay', 750, 500, 300, 100, function(){
            music.intro.play();
            music.isPlaying = true;
            game.state.start('state1');
        });

        createButton(game, 'HowTo', 750, 650, 300, 100, function(){
            music.intro.play();
            music.isPlaying = true;
            game.state.start('tutorial');
        });

        createButton(game, 'Levels', 750, 800, 300, 100, function(){
            music.intro.play();
            music.isPlaying = true;
            game.state.start('level-screen');
        });
    }, 
    
    update: function(){
    
    },
};
