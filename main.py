import utils
import parser
import core

Passwords = []
Usernames = []

def main(args):
    Target = args.target
    Session, htmlPage = utils.Prepare(Target)
    FormPayload = core.ExtractPayload(htmlPage)
    

if __name__=='__main__':
    main(parser.parser())