from bs4 import BeautifulSoup
import requests


def ExtractPayload(htmlPage: bytes) -> dict:
    '''
    Create the payload by extracting login form's values.
    '''
    Soup = BeautifulSoup(htmlPage, 'html.parser')
    LoginForm = Soup.find('form')
    Payload = {}

    for input_tag in LoginForm.find_all('input'):
        name = input_tag.get('name')
        value = input_tag.get('value')

        if input_tag.get('type') == 'checkbox':
            break
        
        if name:
            Payload[name] = value
    
    return Payload

def Testata(target: str, session: requests.Session, username: str, password: str, payload=str) -> requests.Response | None :
    '''
    Try a new password and username combination against the target.
    Returns the HTTP Response or a None if something bad happend.
    '''
    payload['log'] = username
    payload['pwd'] = password

    try:

        return session.post(url=target, data=payload).raw
    except Exception as e:
        print('An error occurred')
        print(e)
        return False
