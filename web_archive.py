import requests,sys

arqv = []

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

def banner():
    print(colors.fg.red + '''
        __      __  ___   ___       _     ___    ___   _  _   ___  __   __  ___ 
        \ \    / / | __| | _ )     /_\   | _ \  / __| | || | |_ _| \ \ / / | __|
         \ \/\/ /  | _|  | _ \    / _ \  |   / | (__  | __ |  | |   \ V /  | _| 
          \_/\_/   |___| |___/   /_/ \_\ |_|_\  \___| |_||_| |___|   \_/   |___|

    ''')

def write_wl():
    worddir = "/usr/share/dirb/wordlists/common.txt"
    wordopen = open(worddir,"r")
    wordline = wordopen.readlines()
    for line in wordline:
        line = line.rstrip()
        arqv.append(line)

def main():
    if 'http://' in sys.argv[1] or 'https://' in sys.argv[1]:
        type_request = sys.argv[1]
        site = sys.argv[2]
        full_url = '{}{}/'.format( type_request,site)
        if requests.get(full_url).status_code != 200:
            quit(colors.fg.red + "Servidor indisponivel")
        for dir in arqv:
            url = '{}{}/{}'.format(type_request,site,dir)
            req = requests.get(url).status_code
            if req == 200:
                print(colors.fg.green + "Diretorio encontrado => {}".format(url))
    else:
        err()

def set_arguments():
    pass

def err():
    print(colors.fg.lightblue + "Mode of use\n")
    print(colors.fg.orange + "python3 {} http:// or https:// site".format(sys.argv[0]))

if __name__ == "__main__":
    try:
        banner()
        if len(sys.argv) != 3:
            quit(err())
        write_wl()
        main()
    except KeyboardInterrupt:
        print(colors.fg.purple + "press control-c again to quit")
