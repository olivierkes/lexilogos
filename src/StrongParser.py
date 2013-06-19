# -*- coding: utf-8 -*-

from PyQt4.QtXml import QDomDocument
from PyQt4.QtCore import QFile


class StrongParser():
    """
    This class is used to load a strong lexicon in XML, parse it, and query
    infos.
    """

    def __init__(self, lexicon="../lexicons/Strongs_EN/strongsgreek.xml"):
        "Takes the path to the lexicon as argument, or uses the default one."
        self._doc = QDomDocument()
        if not self._doc.setContent(QFile(lexicon)):
            print("ERROR: couldn't load lexicon. Please, try harder.'")
        self._entries = self._doc.documentElement()\
                                 .namedItem("entries").childNodes()

    def getGreekUnicode(self, number):
        "Returns the greek lexical form in unicode for the given strong number."
        return self.getStrong(number).namedItem("greek")\
                                     .toElement().attribute("unicode")

    def getStrong(self, number):
        """Returns a QDomNode for the given strong number.
        Used mainly internally."""
        return self._entries.at(number - 1)

    def getDefinition(self, number):
        """Returns the word definition from the strong lexicon. Uses first the
        strong definition, and if not the KJV definition.
        """
        s = self.getStrongDefinition(number)
        if not s:
            s = self.getKJVDefinition(number)
        return self.clean(s)

    def clean(self, s):
        "Used to clean some text: removes line breaks, and multiple spaces."
        s = s.replace("\n", " ")
        os = ""
        while s != os:
            os = s
            s = s.replace("  ", " ")
        return s.strip()

    def getStrongDefinition(self, number):
        "Returns the strong definition for the given strong number."
        return self.getStrong(number).namedItem("strongs_def")\
                                     .toElement().text()

    def getKJVDefinition(self, number):
        "Returns the KJV definition for the given strong number."
        d = self.getStrong(number).namedItem("kjv_def").toElement().text()
        if d[:3] == ":--":
            d = d[3:]
        return self.clean(d)

