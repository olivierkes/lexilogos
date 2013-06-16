# -*- coding: utf-8 -*-

from PyQt4.QtXml import QDomDocument
from PyQt4.QtCore import QFile


class StrongParser():

    def __init__(self, lexicon="../lexicons/strongsgreek.xml"):
        self._doc = QDomDocument()
        print(self._doc.setContent(QFile(lexicon)))
            #print("ERROR: couldn't load lexicon. Please, try harder.'")
        self._entries = self._doc.documentElement()\
                                 .namedItem("entries").childNodes()

    def getGreekUnicode(self, number):
        return self.getStrong(number).namedItem("greek")\
                                     .toElement().attribute("unicode")

    def getStrong(self, number):
        return self._entries.at(number - 1)

    def getDefinition(self, number):
        s = self.getStrongDefinition(number)
        if not s:
            s = self.getKJVDefinition(number)
        return self.clean(s)

    def clean(self, s):
        s = s.replace("\n", " ")
        os = ""
        while s != os:
            os = s
            s = s.replace("  ", " ")
        return s.strip()


    def getStrongDefinition(self, number):
        return self.getStrong(number).namedItem("strongs_def")\
                                     .toElement().text()

    def getKJVDefinition(self, number):
        d = self.getStrong(number).namedItem("kjv_def").toElement().text()
        if d[:3] == ":--":
            d = d[3:]
        return self.clean(d)

