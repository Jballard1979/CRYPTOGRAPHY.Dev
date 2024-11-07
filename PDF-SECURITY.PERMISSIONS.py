#--!/usr/bin/env python
#-- -*- coding: Latin-1 -*-
#--
#-- ************************************************************************************************************:
#-- ***************************************** SET SECURITY PERMISSIONS *****************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2024.7.18                                                                                         :
#-- Script:   PDF-SECURITY.PERMISSIONS.py                                                                       :
#-- Purpose:  A python script that sets security permissions in a PDF file.                                     :
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
SECURITYPol = PdfPasswordSECURITYPol("userpassword", "ownerpassword")
#--
#-- SET ENCRYPTION ALGORITHM:
SECURITYPol.EncryptionAlgorithm = PdfEncryptionAlgorithm.AES_256
#--
#-- SET PDF PERMISSIONS TO RESTRICT ALL EXCEPT PRINTING:
SECURITYPol.DocumentPrivilege = PdfDocumentPrivilege.ForbidAll()
SECURITYPol.DocumentPrivilege.AllowPrint = True
#--
#-- ENCRYPT PDF CONTENT EXCEPT METADATA:
SECURITYPol.EncryptMetadata = False
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