#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************* ENCRYPT/DECRYPT FILES ******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.10.24                                                                                        :
#-- Script:   FILE-ENCRYPT.DECRYPT.v1.py                                                                        :
#-- Purpose:  A python script that uses cryptographic algorithms (AES/RSA) to encrypt/decrypt sensitive files.  :
#-- Class:    python -m pip install cryptography                                                                :
#-- Class:    python -m pip install argparse                                                                    :
#-- Class:    python -m pip install Fernet                                                                      :
#-- Class:    python -m pip install getpass                                                                     :
#-- Test:     C:\0_SVN\2_DEV\3_PYTHON.Src\1_USEFUL.Dev\ENCRYPTION.DECRYPTION.Src\FILES.TXT.Dev\CRYPTOGRAPHY.jeb :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES, & LIBS :
#-- ********************************************************:
import os
import sys
import argparse
import getpass
from cryptography.fernet import Fernet
#--
#-- CLASS - SELF GENERATING KEY:
class EncryptionTool:
    #--
    #-- FUNCTION - INIT KEY:
    def __init__(self):
        self._key = None
    #--
    #-- FUNCTION - GENERATING & ENCODE NEW KEY:
    @staticmethod
    def GEN_Key(self):
        self._key = Fernet.generate_key()
    #--
    #-- FUNCTION - SAVE KEY:
    def SAVE_Key(self, key, filename="key.key"):
        with open(filename, "wb") as KEYFile:
            KEYFile.write(key)
    #--
    #-- FUNCTION - LOAD KEY:
    @staticmethod
    def LOAD_Key(filename="key.key"):
        if not os.path.isfile(filename):
            return None
        with open(filename, "rb") as KEYFile:
            return KEYFile.read()
    #--
    #-- FUNCTION - GENERATE MISSING KEY:
    def ENC_File(self, INFile, OUTFile=None):
        if self._key is None:
            print("******************************************")
            print("ERROR - MISSING KEY, PLEASE GENERATE KEY: ")
            print("******************************************")
            #--
            self._key = self.GEN_Key()
            self.SAVE_Key(self._key)
        #--
        cipher = Fernet(self._key)
        with open(INFile, "rb") as in_f:
            data = in_f.read()
        ENCData = cipher.encrypt(data)
        with open(OUTFile or f"{os.path.basename(INFile)}.enc", "wb") as out_f:
            out_f.write(ENCData)
        #--
        print(f"NOTE - FILE '{INFile}' WAS ENCRYPTED & SAVED: ")
    #--
    #-- FUNCTION - DECRYPT FILE:
    def DEC_File(self, INFile, OUTFile=None):
        if self._key is None:
            print("**********************************************")
            print("ERROR - MISSING KEY, PLEASE GENERATE NEW KEY: ")
            print("**********************************************")
            #--
            return
        #--
        cipher = Fernet(self._key)
        with open(INFile, "rb") as in_f:
            ENCData = in_f.read()
        DECData = cipher.decrypt(ENCData)
        with open(OUTFile or f"{os.path.basename(INFile)}.dec", "wb") as out_f:
            out_f.write(DECData)
        print(f"FILE DECRYPTED & SAVED '{OUTFile or f'{os.path.basename(INFile)}.dec'}': \n")
#--
#-- FUNCTION - MAIN:
def main():
    et = EncryptionTool()
    et.GEN_Key(et)
    print("*****************************************")
    print("FILE ENCRYPTION/DECRYPTION TOOL ver.1.0: ")
    print("*****************************************")
    #--
    while True:
        action = input("USER - PLEASE SELECT DESIRED OPTION FROM THE BELOW MENU:\n 1 - ENCRYPT FILE:\n 2 - DECRYPT FILE:\n 3 - GENERATE NEW KEY:\n 4 - EXIT TOOL:\n")
        if action.isdigit() and int(action) in (1, 2, 3):
            #-- OPTION 1 - FILE ENCRYPTION:
            if action == "1":
                INFile = input("USER (ENCRYPTION) - ENTER DESIRED FILE NAME: ")
                et.ENC_File(INFile)
            #-- OPTION 2 - FILE DECRYPTION:
            elif action == "2":
                INFile = input("USER (DECRYPTION) - ENTER DESIRED FILE NAME: ")
                et.DEC_File(INFile)
            #-- OPTION 3 - GENERATE NEW ENCODED KEY:
            elif action == "3":
                et._key = et.GEN_Key()
                et.SAVE_Key(et._key)
        #--
        #-- OPTION 4 - EXIT TOOL:
        elif action == "4":
            break
        else:
            print("********************************************************")
            print("ERROR - USER SELECTED INVALID ACTION, PLEASE TRY AGAIN: ")
            print("********************************************************")
#--
#-- MAIN:
if __name__ == "__main__":
    main()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: