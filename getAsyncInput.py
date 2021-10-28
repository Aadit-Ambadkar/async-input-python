import sys, termios, atexit
from select import select
from threading import Thread
import time

# save the terminal settings
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# new terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)


# switch to normal terminal
def set_normal_term():
    # fd = sys.stdin.fileno()
    # new_term = termios.tcgetattr(fd)
    # old_term = termios.tcgetattr(fd)
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

# switch to unbuffered terminal
def set_curses_term():
    # fd = sys.stdin.fileno()
    # new_term = termios.tcgetattr(fd)
    # old_term = termios.tcgetattr(fd)
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)
    
def initialize():
    atexit.register(set_normal_term)
    set_curses_term()

def putch(ch):
    sys.stdout.write(ch)

def getch():
    return sys.stdin.read(1)

def getche():
    ch = getch()
    putch(ch)
    return ch

def kbhit():
    dr,dw,de = select([sys.stdin], [], [], 0)
    return dr != []
