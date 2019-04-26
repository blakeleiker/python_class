from lxml import etree
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX
# Example of a Python module with Google Style docstrings:
# Reference for documentation style guide:
# http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html


class TrajectoryTrace(object):

    def __init__(self, file_name="trajectory.kml"):
        self.__filename__ = file_name
        self.KmlDoc = KML.kml(KML.Document(KML.name(self.__filename__)))
        return

    def AddTrajectoryTrace(self, name="trajectory", alt=[], lat=[], lon=[], color='FF0078F0'):
        coordinate_string_ = ''
        for alt, lat, lon in zip(alt, lat, lon):
            coordinate_string_ += str(lon) + ',' + str(lat) + ',' + str(alt) + '\n'
        trace_ = KML.Polygon(
            KML.extrude(0),
            KML.altitudeMode('absolute'),
            KML.outerBoundaryIs(
                KML.extrude(0),
                KML.LinearRing(
                    KML.extrude(0),
                    KML.tessellate(0),
                    KML.altitudeMode('absolute'),
                    KML.coordinates(coordinate_string_),
                ),
            ),
        )
        place_marker_ = KML.Placemark(
            KML.name(name),
            KML.visibility(1),
            KML.description(''),
            KML.Style(
                KML.LineStyle(
                    KML.color(color),
                    KML.width(2.00)
                ),
                KML.PolyStyle(
                    KML.color('00ffffff')
                ),
            ),
            trace_,
        )
        self.KmlDoc.Document.append(place_marker_)
        return

    def SetView(self, lat=0.0, lon=0.0, heading=0.0, tilt=0.0, view_range=0.0):
        look_at_ = KML.LookAt(
            KML.longitude(lon),
            KML.latitude(lat),
            KML.heading(heading),
            KML.tilt(tilt),
            KML.range(view_range),
            GX.altitudeMode('absolute'),
        )
        self.KmlDoc.Document.append(look_at_)

    def WriteFile(self):
        kml_str_ = etree.tostring(self.KmlDoc, pretty_print=True)
        with open(self.__filename__, 'w+') as f:
            f.write(kml_str_.decode('utf-8'))
        return self.__filename__


