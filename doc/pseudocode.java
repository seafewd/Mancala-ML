class Game {
    Player player1 = new Player();
    Player player2 = new Player();

    boolean makeTurn(chosenFieldIndex) {
        boolean oneMoreTurn = false;

        stonesInField = fieldList(a).getStones();
        fieldList(chosenFieldIndex).empty();
        for(i = 1; i <= stonesInField; i++) {
            fieldList(chosenFieldIndex + i).increment();

            if (fieldList(i).getInstanceOf() == bankField) {
                oneMoreTurn = true;
            }
        }
    return oneMoreTurn;
  }

  void startGame() {
  }

  void stopGame() {

  }

  void displayWinner() {
      if player1.score
  }
}
