import requests
import setproctitle
from typing import Tuple, List

def file_to_list(filename: str) -> List[str] | None:
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        return lines
    
    except Exception as e:
        print(f'\nAn error occurred while tryin\' to open {filename}\n\n{e}')
        return None

def Prepare(Target) -> Tuple[requests.Session, bytes] :
    setproctitle.setproctitle(f'TestaDura: {Target}')
    Session = requests.Session()

    try:
        htmlPage = Session.get(Target).content
        return Session, htmlPage
    
    except Exception as e:
        print(f'\n Unable to retrieve the page. \n\n {e}')
        exit(1)