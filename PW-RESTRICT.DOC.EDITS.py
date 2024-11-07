#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- **************************************************************************************************************:
#-- ************************************************ RESTRICT EDITS **********************************************:
#-- **************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                      :
#-- Date:     2024.1.05                                                                                           :
#-- Script:   PW-RESTRICT.DOC.EDITS.py                                                                            :
#-- Purpose:  A python script that restricts edits to a MS WORD Document.                                         :
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
doc.LoadFromFile("MATH-CALC.docx")
#--
#-- PROTECT WORD DOCUMENT FROM EDITS USING SPECIFIC TYPE OF RESTRICTIONS:
doc.Protect(ProtectionType.AllowOnlyComments, "DDF@DDDSSa@1411")
#--
#-- SAVE WORD DOCUMENT AS NEW:
doc.SaveToFile("MATH-CALC.RST.EDITS.docx", FileFormat.Docx2016)
doc.Close()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: