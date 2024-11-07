#--!/usr/bin/env python3
#-- -*- coding: Latin-1 -*-
#--
#-- **************************************************************************************************************:
#-- ********************************************** CLEAR RESTRICTIONS ********************************************:
#-- **************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                      :
#-- Date:     2024.1.05                                                                                           :
#-- Script:   PW-CLR.RESTRICTIONS.DOC.py                                                                          :
#-- Purpose:  A python script that restricts clears all edit restrictions.                                        :
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
doc.LoadFromFile("MATH-CALC.docx", FileFormat.Auto, "afds@dfdfd@1411")
#--
#-- CLEAR ALL EDITING RESTRICTIONS:
doc.Protect(ProtectionType.NoProtection)
#--
#-- SAVE WORD DOCUMENT AS NEW:
doc.SaveToFile("MATH-CALC.RST.EDITS.docx", FileFormat.Docx2016)
doc.Close()
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: