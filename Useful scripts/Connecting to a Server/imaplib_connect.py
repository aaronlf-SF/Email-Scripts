import imaplib
import configparser
import os

SERVER = 'server'
HOSTNAME = 'hostname'
USERNAME = 'username'
PASSWORD = 'password'


def open_connection(verbose=False):

    # Connect to the server
    if verbose:
        print('Connecting to', HOSTNAME)
    connection = imaplib.IMAP4_SSL(HOSTNAME)

    # Login to our account
    if verbose:
        print('Logging in as', USERNAME)
    connection.login(USERNAME, PASSWORD)
    return connection


	
if __name__ == '__main__':
    with open_connection(verbose=True) as c:
        print(c)