# import <
from time import sleep
from os import system, path

# >


# global <
gDirectory = '/'.join(path.realpath(__file__).split('/')[:-1])

# >


# main <
if (__name__ == '__main__'):

    while (True):

        # run patch <
        # wait <
        system(command = f'bash {gDirectory}/patch.sh')
        sleep(150)

        # >

# >
