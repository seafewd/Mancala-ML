from Field import PlayerField


class Board():

    #initialize placeholder list
    field_list = [None] * 14

    def __init__(self):
        for field in field_list:
            field = PlayerField()
        field_list[0] = BankField()
        field_list[7] = BankField()
