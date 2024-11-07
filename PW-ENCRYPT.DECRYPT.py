#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- ************************************************************************************************************:
#-- **************************************** ENCRYPT OR DECRYPT PASSWORD ***************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.3.07                                                                                         :
#-- Script:   PW-ENCRYPT.DECRYPT.py                                                                             :
#-- Purpose:  A python script that encrypts & decrypts passwords.                                               :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- python -m pip install -U Fernet
#-- python3 -m pip install -U Fernet
#-- python -m pip install Fernet
#-- python3 -m pip install Fernet
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
from cryptography.fernet import Fernet 
#--
def encrypt(text, key): 
    f = Fernet(key) 
    ENCRYPTxt = f.encrypt(text.encode()) 
    return ENCRYPTxt 
#--
def decrypt(ENCRYPTxt, key): 
    f = Fernet(key) 
    DECRYPTxt = f.decrypt(ENCRYPTxt).decode() 
    return DECRYPTxt 
#--
text = "BLAH@GL4ADF"
key = Fernet.generate_key() 
ENCRYPTxt = encrypt(text, key) 
print("ENCRYPTED TEXT: ", ENCRYPTxt) 
#--
DECRYPTxt = decrypt(ENCRYPTxt, key) 
print("DECRYPTED TEXT: ", DECRYPTxt)
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: