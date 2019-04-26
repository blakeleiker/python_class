from unittest import TestCase
import os, sys
# Allows us to import our modules
sys.path.append(os.path.join('../', 'modules'))

class TestPart1(TestCase):
    def test_parse_trick_ascii(self):
        from TrickSimData import parse_trick_ascii
        sim_data = parse_trick_ascii(os.path.join('..', 'sample_data','sample_run.csv'))
        self.assertAlmostEquals(sim_data['altitude'][0], 48.08326, 4)
        self.assertAlmostEquals(sim_data['latitude'][0], 0.49850, 4)
        self.assertAlmostEquals(sim_data['longitude'][0], -1.4063, 4)

    def test_parse_trick_ascii_no_file(self):
        from TrickSimData import parse_trick_ascii
        # check that s.split fails when the separator is not a string
        with self.assertRaises(IOError):
            parse_trick_ascii("bogus_file.csv")

    def test_parse_single_run(self):
        from TrickSimData import SingleRun
        sim_data = SingleRun(sim_data_dir=os.path.join('..', 'sample_data'), dr_group="sample_run")
        self.assertAlmostEquals(sim_data['altitude'][0], 48.08326, 4)
        self.assertAlmostEquals(sim_data['latitude'][0], 0.49850, 4)
        self.assertAlmostEquals(sim_data['longitude'][0], -1.4063, 4)

    def test_bad_sim_data_dir(self):
        from TrickSimData import SingleRun
        with self.assertRaises(IOError):
            sim_data = SingleRun(sim_data_dir="bogus", dr_group="sample_run")

    def test_bad_dr_group(self):
        from TrickSimData import SingleRun
        with self.assertRaises(IOError):
            sim_data = SingleRun(sim_data_dir=os.path.join('..', 'sample_data'), dr_group="bad_group")

    def test_no_args(self):
        from TrickSimData import SingleRun
        with self.assertRaises(KeyError):
            sim_data = SingleRun()

    def test_parse_mc_data(self):
        from TrickSimData import MonteCarloRun
        sim_data = MonteCarloRun(sim_data_dir=os.path.join('..', 'sample_data', 'sample_mc_data'), dr_group="sample_run")
        self.assertAlmostEquals(sim_data['RUN_00000']['altitude'][0], 48.08326, 4)
        self.assertAlmostEquals(sim_data['RUN_00001']['altitude'][100], 1304.3468, 4)
        self.assertAlmostEquals(sim_data['RUN_00000']['latitude'][0], 0.49850, 4)
        self.assertAlmostEquals(sim_data['RUN_00000']['longitude'][0], -1.4063, 4)

    def test_bad_sim_data_dir(self):
        from TrickSimData import MonteCarloRun
        with self.assertRaises(IOError):
            sim_data = MonteCarloRun(sim_data_dir="bogus", dr_group="sample_run")

    def test_bad_dr_group(self):
        from TrickSimData import MonteCarloRun
        with self.assertRaises(IOError):
            sim_data = MonteCarloRun(sim_data_dir=os.path.join('..', 'sample_data', 'sample_mc_data'), dr_group="bad_group")