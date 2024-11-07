#--!/usr/bin/env python
#-- -*- coding: Latin-1 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************** DECRYPT PDF FILES *********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.7.18                                                                                         :
#-- Script:   PDF-DECRYPT.py                                                                                    :
#-- Purpose:  A python script that Decrypts PDF files.                                                          :
#-- Class:    python -m pip install Spire                                                                       :
#-- Class:    python -m pip install --upgrade Spire.Pdf                                                         :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
from spire.pdf.common import *
from spire.pdf import *
#--
#-- GENERATE OBJECT & LOAD PDF FILE:
pdf = PdfDocument()
pdf.LoadFromFile("ENCRYPTED.pdf", "userpassword")
#--
#-- DECRYPT LOADED PDF:
pdf.Decrypt("ownerpassword")
#--
#-- SAVE ENCRYPTED PDF AS NEW FILE:
pdf.SaveToFile("DECRYPTED.pdf")
#--
pdf.Close()
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: