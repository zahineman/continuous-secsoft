from http import client
from itertools import count
from venv import create
import hvac 
import random 

def makeConn():
    hvc_client = client = hvac.Client(url='http://127.0.0.1:8200', token='hvs.TxuSZSkHynnOgyIckK0au2GR' ) 
    return hvc_client 

def storeSecret( client,  secr1 , cnt  ):
    secret_path     = 'SECRET_PATH_' + str( cnt  )
    create_response = client.secrets.kv.v2.create_or_update_secret(path=secret_path, secret=dict(password =  secr1 ) )
    # print( type( create_response ) )
    # print( dir( create_response)  )

def retrieveSecret(client_, cnt_): 
    secret_path        = 'SECRET_PATH_' + str( cnt_  )
    read_response      = client_.secrets.kv.read_secret_version(path=secret_path) 
    secret_from_vault  = read_response['data']['data']['password']
    print('The secret we have obtained:')
    print(secret_from_vault)

if __name__ == '__main__': 
    clientObj    =  makeConn() 
    secret2store = str(  random.randint(1, 100000) )
    counter      = 0 

    print('The secret we want to store:', secret2store)
    print('='*50)
    storeSecret( clientObj,   secret2store, counter )
    print('='*50)
    retrieveSecret( clientObj,  counter )
    print('='*50)
#============================================================#
    storeSecret(clientObj, "root_user", 1)
    print('='*50)
    retrieveSecret( clientObj,  1 )
    print('='*50)

    storeSecret(clientObj, "test_password", 2)
    print('='*50)
    retrieveSecret( clientObj,  2 )
    print('='*50)

    storeSecret(clientObj, "ghp_ahAyHoRwoQ", 3)
    print('='*50)
    retrieveSecret( clientObj,  3 )
    print('='*50)

    storeSecret(clientObj, "MTIzANO=", 4)
    print('='*50)
    retrieveSecret( clientObj,  4 )
    print('='*50)

    storeSecret(clientObj, "t5f28U", 5)
    print('='*50)
    retrieveSecret( clientObj,  5 )
    print('='*50)