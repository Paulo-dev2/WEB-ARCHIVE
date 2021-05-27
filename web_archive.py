import requests,sys

arqv = []

def banner():
    print('''
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
            quit("Servidor indisponivel")
        for dir in arqv:
            url = '{}{}/{}'.format(type_request,site,dir)
            req = requests.get(url).status_code
            if req == 200:
                print("Diretorio encontrado => {}".format(url))

def set_arguments():
    pass

if __name__ == "__main__":
    banner()
    if len(sys.argv) != 3:
        quit("Errado")
    write_wl()
    main()