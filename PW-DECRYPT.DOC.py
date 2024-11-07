#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- **************************************************************************************************************:
#-- ************************************************* DECRYPT DOCS ***********************************************:
#-- **************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                      :
#-- Date:     2024.1.05                                                                                           :
#-- Script:   PW-DECRYPT.DOC.py                                                                                   :
#-- Purpose:  A python script that decrypts MS WORD Documents.                                                    :
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
doc.LoadFromFile("MATH-CALC.docx", FileFormat.Auto, "JDKDKDK@1411")
#--
#-- DECRYPT WORD DOCUMENT:
doc.RemoveEncryption()
#--
#-- SAVE WORD DOCUMENT AS NEW:
doc.SaveToFile("DECRYPTED.DOC.docx", FileFormat.Docx2016)
doc.Close()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: