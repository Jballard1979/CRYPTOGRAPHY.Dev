#--!/usr/bin/env python
#-- -*- coding: Latin-1 -*-
#--
#-- ************************************************************************************************************:
#-- ******************************************** ENCRYPT PDF FILES *********************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.7.18                                                                                         :
#-- Script:   PDF-ENCRYPT.py                                                                                    :
#-- Purpose:  A python script that Encrypts PDF files.                                                          :
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
pdf.LoadFromFile("TEST.pdf")
#--
#-- BUILD SECURITY POLICY & SET CREDENTIALS:
SECURITYPol = PdfPasswordSECURITYPol("userpassword", str())
#--
#-- SET ENCRYPTION ALGORITHM:
SECURITYPol.EncryptionAlgorithm = PdfEncryptionAlgorithm.AES_256
#--
#-- APPLY SECURITY POLICY FOR ENCRYPTION:
pdf.Encrypt(SECURITYPol)
#--
#-- SAVE ENCRYPTED PDF AS NEW FILE:
pdf.SaveToFile("ENCRYPTED.pdf")
#--
pdf.Close()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: