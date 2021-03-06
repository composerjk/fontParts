import warnings

# A collection of deprecated roboFab methods.
# Those methods are added to keep scripts and code compatible.

class RemovedWarning(DeprecationWarning):
    """Warning for things removed from FontParts that were in RoboFab"""


# ========
# = base =
# ========

class RemovedBase(object):

    def setParent(self, parent):
        objName = self.__class__.__name__.replace("Removed", "")
        raise RemovedWarning("'%s.setParent()'" % objName)


class DeprecatedBase(object):

    def update(self):
        objName = self.__class__.__name__.replace("Deprecated", "")
        warnings.warn("'%s.update': use %s.changed()"
                      % (objName, objName), DeprecationWarning)
        self.changed()

    def setChanged(self):
        objName = self.__class__.__name__.replace("Deprecated", "")
        warnings.warn("'%s.setChanged': use %s.changed()"
                      % (objName, objName), DeprecationWarning)
        self.changed()


# ==================
# = transformation =
# ==================

class DeprecatedTransformation(object):

    def move(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        warnings.warn("'%s.move()': use %s.moveBy()"
                      % (objName, objName), DeprecationWarning)
        self.moveBy(*args, **kwargs)

    def translate(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        warnings.warn("'%s.translate()': use %s.moveBy()"
                      % (objName, objName), DeprecationWarning)
        self.moveBy(*args, **kwargs)

    def scale(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        warnings.warn("'%s.scale()': use %s.scaleBy()"
                      % (objName, objName), DeprecationWarning)
        if "center" in kwargs:
            kwargs["origin"] = kwargs["center"]
            del kwargs["center"]
        self.scaleBy(*args, **kwargs)

    def rotate(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        warnings.warn("'%s.rotate()': use %s.rotateBy()"
                      % (objName, objName), DeprecationWarning)
        if "offset" in kwargs:
            kwargs["origin"] = kwargs["offset"]
            del kwargs["offset"]
        self.rotateBy(*args, **kwargs)

    def transform(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        warnings.warn("'%s.transform()': use %s.transformBy()"
                      % (objName, objName), DeprecationWarning)
        self.transformBy(*args, **kwargs)

    def skew(self, *args, **kwargs):
        objName = self.__class__.__name__.replace("Deprecated", "")
        warnings.warn("'%s.skew()': use %s.skewBy()"
                      % (objName, objName), DeprecationWarning)
        if "offset" in kwargs:
            kwargs["origin"] = kwargs["offset"]
            del kwargs["offset"]
        self.skewBy(*args, **kwargs)


# =========
# = Point =
# =========

class RemovedPoint(RemovedBase):

    def select(self, state=True):
        raise RemovedWarning("'Point.select'")


class DeprecatedPoint(DeprecatedBase, DeprecatedTransformation):

    def _generateIdentifier(self):
        warnings.warn("'Point._generateIdentifier()': use 'Point._getIdentifier()'",
                      DeprecationWarning)
        return self._getIdentifier()

    def generateIdentifier(self):
        warnings.warn("'Point.generateIdentifier()': use 'Point.getIdentifier()'",
                      DeprecationWarning)
        return self.getIdentifier()

    def getParent(self):
        warnings.warn("'Point.getParent()': use 'Point.contour'",
                      DeprecationWarning)
        return self.contour


# ==========
# = BPoint =
# ==========

class RemovedBPoint(RemovedBase):

    pass


class DeprecatedBPoint(DeprecatedBase, DeprecatedTransformation):

    def _generateIdentifier(self):
        warnings.warn("'BPoint._generateIdentifier()': use 'BPoint._getIdentifier()'",
                      DeprecationWarning)
        return self._getIdentifier()

    def generateIdentifier(self):
        warnings.warn("'BPoint.generateIdentifier()': use 'BPoint.getIdentifier()'",
                      DeprecationWarning)
        return self.getIdentifier()

    def getParent(self):
        warnings.warn("'BPoint.getParent()': use 'BPoint.contour'",
                      DeprecationWarning)
        return self.contour


# ==========
# = Anchor =
# ==========

class RemovedAnchor(RemovedBase):

    def draw(self, pen):
        raise RemovedWarning("'Anchor.draw': UFO3 is not drawing anchors into pens")

    def drawPoints(self, pen):
        raise RemovedWarning(("'Anchor.drawPoints': UFO3 is not drawing "
                              "anchors into point pens"))


class DeprecatedAnchor(DeprecatedBase, DeprecatedTransformation):

    def _generateIdentifier(self):
        warnings.warn("'Anchor._generateIdentifier()': use 'Anchor._getIdentifier()'",
                      DeprecationWarning)
        return self._getIdentifier()

    def generateIdentifier(self):
        warnings.warn("'Anchor.generateIdentifier()': use 'Anchor.getIdentifier()'",
                      DeprecationWarning)
        return self.getIdentifier()

    def getParent(self):
        warnings.warn("'Anchor.getParent()': use 'Anchor.glyph'",
                      DeprecationWarning)
        return self.glyph


# =============
# = Component =
# =============

class RemovedComponent(RemovedBase):

    pass


class DeprecatedComponent(DeprecatedBase, DeprecatedTransformation):

    def _get_box(self):
        warnings.warn("'Component.box': use Component.bounds",
                      DeprecationWarning)
        return self.bounds

    box = property(_get_box, doc="Deprecated Component.box")

    def _generateIdentifier(self):
        warnings.warn(("'Component._generateIdentifier()': use "
                       "'Component._getIdentifier()'"),
                      DeprecationWarning)
        return self._getIdentifier()

    def generateIdentifier(self):
        warnings.warn(("'Component.generateIdentifier()': "
                       "use 'Component.getIdentifier()'"),
                      DeprecationWarning)
        return self.getIdentifier()

    def getParent(self):
        warnings.warn("'Component.getParent()': use 'Component.glyph'",
                      DeprecationWarning)
        return self.glyph


# ===========
# = Segment =
# ===========

class RemovedSegment(RemovedBase):

    def insertPoint(self, point):
        raise RemovedWarning("Segment.insertPoint()")

    def removePoint(self, point):
        raise RemovedWarning("Segment.removePoint()")


class DeprecatedSegment(DeprecatedBase, DeprecatedTransformation):

    def getParent(self):
        warnings.warn("'Segment.getParent()': use 'Segment.contour'",
                      DeprecationWarning)
        return self.contour


# ===========
# = Contour =
# ===========

class RemovedContour(RemovedBase):

    pass


class DeprecatedContour(DeprecatedBase, DeprecatedTransformation):

    def _get_box(self):
        warnings.warn("'Contour.box': use Contour.bounds", DeprecationWarning)
        return self.bounds

    box = property(_get_box, doc="Deprecated Contour.box")

    def reverseContour(self):
        warnings.warn("'Contour.reverseContour()': use 'Contour.reverse()'",
                      DeprecationWarning)
        self.reverse()

    def _generateIdentifier(self):
        warnings.warn("'Contour._generateIdentifier()': use 'Contour._getIdentifier()'",
                      DeprecationWarning)
        return self._getIdentifier()

    def generateIdentifier(self):
        warnings.warn("'Contour.generateIdentifier()': use 'Contour.getIdentifier()'",
                      DeprecationWarning)
        return self.getIdentifier()

    def _generateIdentifierforPoint(self):
        warnings.warn(("'Contour._generateIdentifierforPoint()': use "
                       "'Contour._getIdentifierforPoint()'"), DeprecationWarning)
        return self._getIdentifierforPoint()

    def generateIdentifierforPoint(self):
        warnings.warn(("'Contour.generateIdentifierforPoint()': use "
                       "'Contour.getIdentifierforPoint()'"), DeprecationWarning)
        return self.getIdentifierforPoint()


# =========
# = Glyph =
# =========

class RemovedGlyph(RemovedBase):

    def center(self, padding=None):
        raise RemovedWarning("'Glyph.center()'")

    def clearVGuides(self):
        raise RemovedWarning("'Glyph.clearVGuides()': use Glyph.clearGuidelines()")

    def clearHGuides(self):
        raise RemovedWarning("'Glyph.clearHGuides()': use Glyph.clearGuidelines()")


class DeprecatedGlyph(DeprecatedBase, DeprecatedTransformation):

    def _get_mark(self):
        warnings.warn("'Glyph.mark': use Glyph.markColor", DeprecationWarning)
        return self.markColor

    def _set_mark(self, value):
        warnings.warn("'Glyph.mark': use Glyph.markColor", DeprecationWarning)
        self.markColor = value

    mark = property(_get_mark, _set_mark, doc="Deprecated Mark color")

    def _get_box(self):
        warnings.warn("'Glyph.box': use Glyph.bounds", DeprecationWarning)
        return self.bounds

    box = property(_get_box, doc="Deprecated Glyph.box")

    def getAnchors(self):
        warnings.warn("'Glyph.getAnchors()': use Glyph.anchors",
                      DeprecationWarning)
        return self.anchors

    def getComponents(self):
        warnings.warn("'Glyph.getComponents()': use Glyph.components",
                      DeprecationWarning)
        return self.components

    def getParent(self):
        warnings.warn("'Glyph.getParent()': use 'Glyph.font'",
                      DeprecationWarning)
        return self.font

    def isEmpty(self):
        warnings.warn("'Glyph.isEmpty()': use 'Glyph.isEmpty'",
                      DeprecationWarning)
        return self.isEmpty

    def readGlyphFromString(self, glifData):
        warnings.warn(("'Glyph.readGlyphFromString()': use "
                       "'Glyph.loadFromGLIF()'"),
                      DeprecationWarning)
        return self.loadFromGLIF(glifData)

    def writeGlyphToString(self, glyphFormatVersion=2):
        warnings.warn(("'Glyph.writeGlyphToString()': use "
                       "'Glyph.dumpToGLIF()'"),
                      DeprecationWarning)
        return self.dumpToGLIF(glyphFormatVersion)

# =============
# = Guideline =
# =============


class RemovedGuideline(RemovedBase):

    pass


class DeprecatedGuideline(DeprecatedBase, DeprecatedTransformation):

    def _generateIdentifier(self):
        warnings.warn(("'Guideline._generateIdentifier()': "
                       "use 'Guideline._getIdentifier()'"), DeprecationWarning)
        return self._getIdentifier()

    def generateIdentifier(self):
        warnings.warn(("'Guideline.generateIdentifier()': "
                       "use 'Guideline.getIdentifier()'"), DeprecationWarning)
        return self.getIdentifier()

    def getParent(self):
        warnings.warn(("'Guideline.getParent()': use 'Guideline.glyph'"
                       " or 'Guideline.font'"),
                      DeprecationWarning)
        glyph = self.glyph
        if glyph is not None:
            return glyph
        return self.font


# =======
# = Lib =
# =======

class RemovedLib(RemovedBase):

    pass


class DeprecatedLib(DeprecatedBase):

    def getParent(self):
        warnings.warn("'Lib.getParent()': use 'Lib.glyph' or 'Lib.font'",
                      DeprecationWarning)
        glyph = self.glyph
        if glyph is not None:
            return glyph
        return self.font


# ==========
# = Groups =
# ==========

class RemovedGroups(RemovedBase):

    pass


class DeprecatedGroups(DeprecatedBase):

    def getParent(self):
        warnings.warn("'Groups.getParent()': use 'Groups.font'",
                      DeprecationWarning)
        return self.font


# ===========
# = Kerning =
# ===========

class RemovedKerning(RemovedBase):

    def setParent(self, parent):
        raise RemovedWarning("'Kerning.setParent()'")

    def swapNames(self, swaptable):
        raise RemovedWarning("Kerning.swapNames()")

    def getLeft(self, glyphName):
        raise RemovedWarning("Kerning.getLeft()")

    def getRight(self, glyphName):
        raise RemovedWarning("Kerning.getRight()")

    def getExtremes(self):
        raise RemovedWarning("Kerning.getExtremes()")

    def add(self, value):
        raise RemovedWarning("Kerning.add()")

    def minimize(self, minimum=10):
        raise RemovedWarning("Kerning.minimize()")

    def importAFM(self, path, clearExisting=True):
        raise RemovedWarning("Kerning.importAFM()")

    def getAverage(self):
        raise RemovedWarning("Kerning.getAverage()")

    def combine(self, kerningDicts, overwriteExisting=True):
        raise RemovedWarning("Kerning.combine()")

    def eliminate(self, leftGlyphsToEliminate=None,
                  rightGlyphsToEliminate=None, analyzeOnly=False):
        raise RemovedWarning("Kerning.eliminate()")

    def occurrenceCount(self, glyphsToCount):
        raise RemovedWarning("Kerning.occurrenceCount()")

    def implodeClasses(self, leftClassDict=None,
                       rightClassDict=None, analyzeOnly=False):
        raise RemovedWarning("Kerning.implodeClasses()")

    def explodeClasses(self, leftClassDict=None,
                       rightClassDict=None, analyzeOnly=False):
        raise RemovedWarning("Kerning.explodeClasses()")


class DeprecatedKerning(DeprecatedTransformation):

    def setChanged(self):
        warnings.warn("'Kerning.setChanged': use Kerning.changed()",
                      DeprecationWarning)
        self.changed()

    def getParent(self):
        warnings.warn("'Kerning.getParent()': use 'Kerning.font'",
                      DeprecationWarning)
        return self.font


# ========
# = Info =
# ========

class RemovedInfo(RemovedBase):

    pass


class DeprecatedInfo(DeprecatedBase):

    def getParent(self):
        warnings.warn("'Info.getParent()': use 'Info.font'",
                      DeprecationWarning)
        return self.font


# =========
# = Image =
# =========

class RemovedImage(RemovedBase):

    pass


class DeprecatedImage(DeprecatedBase):

    def getParent(self):
        warnings.warn("'Image.getParent()': use 'Image.glyph'",
                      DeprecationWarning)
        return self.glyph


# ============
# = Features =
# ============

class RemovedFeatures(RemovedBase):

    def round(self):
        raise RemovedWarning("'Feature.round()'")


class DeprecatedFeatures(DeprecatedBase):

    def getParent(self):
        warnings.warn("'Features.getParent()': use 'Features.font'",
                      DeprecationWarning)
        return self.font


# =========
# = Layer =
# =========

class RemovedLayer(RemovedBase):

    pass


class DeprecatedLayer(DeprecatedBase):

    def getParent(self):
        warnings.warn("'Layer.getParent()': use 'Layer.font'",
                      DeprecationWarning)
        return self.font


# ========
# = Font =
# ========

class RemovedFont(RemovedBase):

    def getParent(self):
        raise RemovedWarning("'Font.getParent()'")

    def generateGlyph(self, *args, **kwargs):
        raise RemovedWarning("'Font.generateGlyph()'")

    def compileGlyph(self, *args, **kwargs):
        raise RemovedWarning("'Font.compileGlyph()'")

    def getGlyphNameToFileNameFunc(self):
        raise RemovedWarning("'Font.getGlyphNameToFileNameFunc()'")


class DeprecatedFont(DeprecatedBase):

    def _get_fileName(self):
        warnings.warn("'Font.fileName': use os.path.basename(Font.path)",
                      DeprecationWarning)
        return self.path

    fileName = property(_get_fileName, doc="Deprecated Font.fileName")

    def getWidth(self, glyphName):
        warnings.warn("'Font.getWidth(): use Font[glyphName].width'",
                      DeprecationWarning)
        return self[glyphName].width

    def getGlyph(self, glyphName):
        warnings.warn("'Font.getGlyph(): use Font[glyphName]'",
                      DeprecationWarning)
        return self[glyphName]

    def _get_selection(self):
        warnings.warn("'Font.selection: use Font.selectedGlyphNames'",
                      DeprecationWarning)
        return self.selectedGlyphNames

    def _set_selection(self, glyphNames):
        warnings.warn("'Font.selection: use Font.selectedGlyphNames'",
                      DeprecationWarning)
        self.selectedGlyphNames = glyphNames

    selection = property(_get_selection, _set_selection,
                         doc="Deprecated Font.selection")
