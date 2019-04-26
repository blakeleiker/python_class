# Reference for documentation style guide:
# http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

class Trajectory(object):

    def __init__(self, **kwargs):
        self.Name = kwargs["name"]
        # Your code here

    @property
    def AverageLatitude(self):
        # Your code here
        return 0.0

    @property
    def AverageLongitude(self):
        # Your code here
        return 0.0

    @property
    def PeakAltitude(self):
        # Your code here
        return 0.0

    def ConvertToDegrees(self):
        # Your code here
        return 0.0

    def ConvertToRadians(self):
        # Your code here
        return 0.0



