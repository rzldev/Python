def play() :
    board = [' '] * 9
    player_turn = choose_turn()

    for index, turn in enumerate(board) :
        if index == 0 :
            pass

        board = check_turn(index, player_turn, board)
        print(board)
        display_board(board)

def choose_turn() :
    marker = ''
    while marker != 'X' and marker != 'O' :
        marker = input("Player 1, choose X or O: ")

    if marker == 'X' :
        player1 = marker
        player2 = 'O'
    else :
        player1 = marker
        player2 = 'X'

    return (player1, player2)

def check_turn(turn, players, board) :
    player1 = players[0]

    if turn == 0 :
        return board
    elif player1 == 'X' and turn % 2 == 0 :
        return (update_block(2, board, 'O'))
    elif player1 == 'X' and turn % 2 == 1 :
        return (update_block(1, board, 'X'))
    elif player1 == 'O' and turn % 2 == 0 :
        return (update_block(1, board, 'O'))
    elif player1 == 'O' and turn % 2 == 1 :
        return (update_block(2, board, 'X'))

def update_block(player, board, symbol) :
    changed = False
    while changed != True :
        player_input = int(input('player{}: Choose the block (1-9): '.format(player)))

        if board[player_input] == ' ' :
            changed = True
            board[player_input] = symbol
        else :
            print('The block already has symbol')

    return board

def display_board(board) :
    print ('''
    {7}|{8}|{9}
    {4}|{5}|{6}
    {1}|{2}|{3}
    '''.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], ' '))

play()
