class Game {
    Player player1;
    Player player2;
	List<Field> fieldList;

	public Game(fieldList) {
		this.fieldList = new ArrayList<>(0, 2, 3);
		this.player1 = new Player();
		this.player2 = new Player();
	}

    boolean makeTurn(fieldIndex) {
        boolean oneMoreTurn = false;

        stonesInField = fieldList(chosenFieldIndex).getStones();
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
