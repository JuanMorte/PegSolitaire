import time
fg_white = "\033[97m"
fg_magenta = '\033[95m'
fg_red = '\033[91m'
fg_blue = '\033[94m'
bg_black = "\033[101m"
bg_yellow = "\033[43m"
bg_cyan = "\033[43m"
bg_red = "\033[41m"
reset = '\033[0m'
bold = '\033[1m'
space = '                                          '
def p(x):
    if x == 'win':
        print(space+fg_red+'██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗'+reset)
        time.sleep(0.1)
        print(space+fg_red+'╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║'+reset)
        time.sleep(0.1)
        print(space+fg_red+' ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║'+reset)
        time.sleep(0.1)
        print(space+fg_red+'  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝'+reset)
        time.sleep(0.1)
        print(space+fg_red+'   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗'+reset)
        time.sleep(0.1)
        print(space+fg_red+'   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝'+reset)
    if x == 'lose':
        print(space+fg_red+'████████╗██████╗ ██╗   ██╗     █████╗  ██████╗  █████╗ ██╗███╗   ██╗')
        time.sleep(0.1)
        print(space+fg_red+'╚══██╔══╝██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔════╝ ██╔══██╗██║████╗  ██║')
        time.sleep(0.1)
        print(space+fg_red+'   ██║   ██████╔╝ ╚████╔╝     ███████║██║  ███╗███████║██║██╔██╗ ██║')
        time.sleep(0.1)
        print(space+fg_red+'   ██║   ██╔══██╗  ╚██╔╝      ██╔══██║██║   ██║██╔══██║██║██║╚██╗██║')
        time.sleep(0.1)
        print(space+fg_red+'   ██║   ██║  ██║   ██║       ██║  ██║╚██████╔╝██║  ██║██║██║ ╚████║')
        time.sleep(0.1)
        print(space+fg_red+'   ╚═╝   ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝')
 

