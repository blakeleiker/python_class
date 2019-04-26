from unittest import TestCase
import os, sys
# Allows us to import our modules
sys.path.append(os.path.join('../', 'modules'))

class TestPart2(TestCase):
    def test_AverageLatitude(self):
        from TrickSimData import SingleRun
        from TrajectoryUtils import Trajectory
        sim_data = SingleRun(sim_data_dir=os.path.join('..', 'sample_data'), dr_group="sample_run")
        test_trajectory = Trajectory(name="RUN_1",
                              alt= sim_data["altitude"],
                              lat= sim_data["latitude"],
                              lon= sim_data["longitude"],
                              convert_degrees=True)
        self.assertAlmostEquals(test_trajectory.AverageLatitude, 28.5672, 4)

    def test_AverageLongitude(self):
        from TrickSimData import SingleRun
        from TrajectoryUtils import Trajectory
        sim_data = SingleRun(sim_data_dir=os.path.join('..', 'sample_data'), dr_group="sample_run")
        test_trajectory = Trajectory(name="RUN_1",
                              alt= sim_data["altitude"],
                              lat= sim_data["latitude"],
                              lon= sim_data["longitude"],
                              convert_degrees=True)
        self.assertAlmostEquals(test_trajectory.AverageLongitude, -80.5732, 4)

    def test_PeakAlititude(self):
        from TrickSimData import SingleRun
        from TrajectoryUtils import Trajectory
        sim_data = SingleRun(sim_data_dir=os.path.join('..', 'sample_data'), dr_group="sample_run")
        test_trajectory = Trajectory(name="RUN_1",
                              alt= sim_data["altitude"],
                              lat= sim_data["latitude"],
                              lon= sim_data["longitude"])
        self.assertAlmostEquals(test_trajectory.PeakAltitude, 2661.47322, 4)
