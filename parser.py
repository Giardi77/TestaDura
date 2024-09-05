import argparse

def parser() -> argparse.NameSpace:
    parser = argparse.ArgumentParser(description="Bruteforce Wordpress login")
    parser.add_argument('-t','--target', help="target's login page")
    parser.add_argument('-p','--passw', help="password wordlist")
    parser.add_argument('-u','--user', help="username wordlist")
    args = parser.parse_args()

    if not args.target:
        print('Please select a target with -t or --target')
        exit(0)
    
    return args