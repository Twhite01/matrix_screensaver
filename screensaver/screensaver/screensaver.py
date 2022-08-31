import shutil
import random
import sys
import time
import os

#setup constants.
min_stream_length = 6 
max_stream_length = 14
pauze = 0.1
stream_chars = ['0', '1']

#density
density = 0.10

# terminal size
WIDTH = shutil.get_terminal_size()[0]

WIDTH -= 1


def matrix():
    
    line_1_matrix = 'Wake up, Neo...\n'
    line_2_matrix = 'The Matrix has you...\n'
    line_3_matrix = 'Follow the white rabbit.'
    space_line_0 = '\n'
    line_4_matrix ='Knock, knock, Neo\n\n'
    

    for char in line_1_matrix:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    time.sleep(0.6)

    for char in line_2_matrix:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    time.sleep(0.6)
    
    for char in line_3_matrix:
        time.sleep(0.10)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(0.6)

    print(space_line_0)

    time.sleep(0.6)

    for char in line_4_matrix:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    time.sleep(2)   
    
    try:
        columns = [0] * WIDTH
        while True:
            for i in range(WIDTH):
                if columns[i] == 0:
                    if random.random() <= density:
                        columns[i] = random.randint(min_stream_length,
                                                    max_stream_length)

                if columns[i] > 0:
                    print(random.choice(stream_chars), end='')
                    columns[i] -= 1
                else:
                    print(' ', end='')
            print()
            sys.stdout.flush()
            time.sleep(pauze)
    except KeyboardInterrupt:
        sys.exit()

matrix()