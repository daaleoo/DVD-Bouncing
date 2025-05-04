import curses
import random
import time

# DVD text
dvd_text = "DVD"

def dvd_bounce(stdscr):
    # Clear screen and set up the terminal window
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(50)  # Set the timeout for screen update (in milliseconds)

    # Terminal dimensions
    height, width = stdscr.getmaxyx()

    # Initial position and direction
    x = random.randint(0, width - len(dvd_text))
    y = random.randint(0, height - 1)
    dx = random.choice([1, -1])  # Random horizontal direction
    dy = random.choice([1, -1])  # Random vertical direction

    while True:
        stdscr.clear()  # Clear the screen before drawing the new frame
        stdscr.addstr(y, x, dvd_text)  # Draw the "DVD" text at the current position
        stdscr.refresh()  # Refresh the screen to show the changes

        # Update position
        x += dx
        y += dy

        # Check for bounce conditions
        if x <= 0 or x >= width - len(dvd_text):
            dx = -dx  # Reverse horizontal direction
        if y <= 0 or y >= height - 1:
            dy = -dy  # Reverse vertical direction

        # Add delay for smoother animation
        time.sleep(0.05)

# Initialize curses and run the DVD bounce animation
curses.wrapper(dvd_bounce)

