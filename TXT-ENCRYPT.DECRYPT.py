#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************* ENCRYPT/DECRYPT TEXT *******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.3.07                                                                                         :
#-- Script:   TXT-ENCRYPT.DECRYPT.py                                                                            :
#-- Purpose:  A python script that encrypts & decrypts text.                                                    :
#-- Class:    python -m pip install pycryptodome                                                                :
#-- Test:     C:\0_SVN\2_DEV\3_PYTHON.Src\1_USEFUL.Dev\ENCRYPTION.DECRYPTION.Src\FILES.TXT.Dev\CRYPTOGRAPHY.jeb :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import sys
import secrets
import os
import Crypto
#--
from binascii import b2a_hex
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
#--
#-- SET KEY TO ALL ZEROS:
key = b'\x00' * AES.block_size
#--
#-- FUNCTION - GENERATE NON-REPEATABLE KEY VECTOR W/LENGTH EQUAL TO SIZE OF AES BLOCK:
def generate_key():
    return get_random_bytes(AES.block_size)
#--
#-- FUNCTION - ADD IV KEY VECTOR TO FRONT-END OF ENCRYPTED CYPHER TEXT & TRANSMIT AS 1:
def encode_ciphertext(iv, plaintext):
    cipher = AES.new(generate_key(), mode=AES.MODE_CFB, iv=iv)
    return iv + cipher.encrypt(pad(plaintext, AES.block_size))
#--
#-- FUNCTION - GENERATE A NEW AES BLOCK OBJECT & DECRYPT CYPHERTEXT:
def decode_ciphertext(iv, ciphertext):
    cipher = AES.new(generate_key(), mode=AES.MODE_CFB, iv=iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)
#--
#-- FUNCTION - RETURN RANDOM BYTES:
def generate_iv():
    return get_random_bytes(AES.block_size)
#--
#-- FUNCTION - MAIN:
def main():
    #--
    print("""TEXT ENCRYPTION/DECRYPTION USING AES-128 CFB MODE TOOL v1.0:
        PLEASE SELECT AN OPTION FROM THE MENUE BELOW:
        1) ENCRYPT
        2) DECRYPT
        """)
    choice = input("USER - PLEASE ENTER AN OPTION (1 or 2): ")
    if choice not in ['1', '2']:
        print("ERROR - INVALID OPTION SELECTED, EXITING TOOL: ")
        sys.exit()
    #--
    #-- OPTION 1 - ENCRYPT FILE:
    if choice == '1':
        file_name = input("USER - PLEASE ENTER THE DESIRED FILENAME TO ENCRYPT: ")
        with open(file_name, "rb") as f:
            plaintext = f.read()
            iv = generate_key()
            ciphertext = encode_ciphertext(iv, plaintext)
            #-- SAVE IV CIPHERTEXT TO SEPERATE FILE FOR FUTURE DECRYPTION:
            with open('{}_IV'.format(file_name), 'wb') as iv_file:
                iv_file.write(iv)
            with open('{}_CT'.format(file_name), 'wb') as ct_file:
                ct_file.write(ciphertext)
        print("NOTE - FILE SUCCESSFULLY ENCRYPTED: ")
    #--
    #-- OPTION 2 - DECRYPT FILE:
    elif choice == '2':
        file_name = input("USER - PLEASE ENTER THE DESIRED FILENAME TO DECRYPT: ")
        with open('{}_IV'.format(file_name), 'rb') as iv_file:
            iv = iv_file.read()
        with open('{}_CT'.format(file_name), 'rb') as ct_file:
            ciphertext = ct_file.read()
        plaintext = decode_ciphertext(iv, ciphertext)
        with open(file_name, "wb") as f:
            f.write(plaintext)
    else:
        print("THE DECRYPTED DATA IS: ")
#--
#-- MAIN:
if __name__ == "__main__":
    main()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: