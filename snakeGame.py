import random
import curses

if __name__ == '__main__':
    # creating screen and getting it's dimensions
    s = curses.initscr()
    curses.curs_set(0)
    sh, sw = s.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    # getting input from keyboard
    w.keypad(1)
    w.timeout(100)

    # creating and displaying the snake in screen

    snk_x = sw // 4
    snk_y = sh // 2

    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    # create food
    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], curses.ACS_PI)

    # create key variable

    key = curses.KEY_RIGHT

    # game logic

    while True:
        # get key input from user
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # check if the snake hit the screen borders or hits itself the lose the game

        if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
            curses.endwin()
            quit()

        # control the snake movement

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1

        snake.insert(0, new_head)
