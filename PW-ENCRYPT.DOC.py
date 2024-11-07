#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- **************************************************************************************************************:
#-- ************************************************* ENCRYPT DOCS ***********************************************:
#-- **************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                      :
#-- Date:     2024.1.05                                                                                           :
#-- Script:   PW-ENCRYPT.DOC.py                                                                                   :
#-- Purpose:  A python script that encrypts MS WORD Documents.                                                    :
#-- Class:    python -m pip install spire                                                                         :
#-- Class:    python -m pip install spire.doc                                                                     :
#-- Version:  1.0                                                                                                 :
#-- **************************************************************************************************************:
#-- **************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, CLASSES         :
#-- ********************************************************:
from spire.doc import *
from spire.doc.common import *
#--
#-- GENERATE DOCUMENT OBJECT:
doc = Document()
#-- LOAD WORD DOCUMENT:
doc.LoadFromFile("Input.docx")
#--
#-- ENCRYPT WORD DOCUMENT WITH PW:
doc.Encrypt("ASDFASDF@1411")
#--
#-- SAVE WORD DOCUMENT AS NEW:
doc.SaveToFile("PasswordProtection.docx", FileFormat.Docx2016)
doc.Close()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: