var game = new Phaser.Game(1500,1000,Phaser.AUTO); //want big game world for crisper image
game.state.add('main-menu', whenSquaresAttack.mainMenu);
game.state.add('level-screen', whenSquaresAttack.levelScreen);
game.state.add('state1', whenSquaresAttack.state1);
game.state.add('state2', whenSquaresAttack.state2);
game.state.add('state3', whenSquaresAttack.state3);
game.state.add('state4', whenSquaresAttack.state4);
game.state.add('state5', whenSquaresAttack.state5);
game.state.add('endscreen', whenSquaresAttack.endscreen);
game.state.add('tutorial', whenSquaresAttack.tutorial);
game.state.start('main-menu');