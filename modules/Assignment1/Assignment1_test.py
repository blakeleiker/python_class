import os
from unittest import TestCase
import pandas as pd
from Assignment1 import Assignment1


class TestAssignment1(TestCase):

    def test_parse_csv(self):
        my_assignment = Assignment1()

        # Run the parse_csv method on the test data. 
        df = my_assignment.parse_csv(os.path.join("data", "accel_data.csv"))

        # Test the contents of the output dataframe. 
        # Note that that the TestCase class (from the unittest package)
        # provides us with a lot of useful class methods, like assertAlmostEqual.
        self.assertAlmostEqual(df['Accel_x {m/s2}'].iloc[0], -0.014885, 4)
        self.assertAlmostEqual(df['Accel_x {m/s2}'].iloc[-1], 0.000276, 4)
        self.assertAlmostEqual(df['Accel_y {m/s2}'].iloc[0], 0.005174, 4)
        self.assertAlmostEqual(df['Accel_y {m/s2}'].iloc[-1], -0.007508, 4)
        self.assertAlmostEqual(df['Accel_z {m/s2}'].iloc[0], -0.000827, 4)
        self.assertAlmostEqual(df['Accel_z {m/s2}'].iloc[-1], -0.004876, 4)

        # Check the name of the index - it should be Time {s}
        assert df.index.name == "Time {s}"

        # Check the column names. 
        assert df.columns[0] == "Accel_x {m/s2}"
        assert df.columns[1] == "Accel_y {m/s2}"
        assert df.columns[2] == "Accel_z {m/s2}"

        # Check the length of the dataframe. There should be exactly 1000 rows.
        assert len(df.index) == 1000
        

    def test_compute_magnitude(self):
        my_assignment = Assignment1()

        # Create a dataframe containing mock data.
        test_df = pd.DataFrame({
            "Time {s}": [0.0, 0.1, 0.2, 0.3],
            "Accel_x {m/s2}": [0.01, 0.020, 0.0, -0.020],
            "Accel_y {m/s2}": [0.01, 0.015, 0.0, -0.010],
            "Accel_z {m/s2}": [0.01, 0.010, 0.0, -0.015],
        })
        test_df.set_index("Time {s}", inplace=True)

        # Run the compute_magnitude method.
        df = my_assignment.compute_magnitude(test_df)

        # Test the output dataframe.
        self.assertAlmostEqual(df['Accel_mag {m/s2}'].iloc[0], 0.017321, 4)
        self.assertAlmostEqual(df['Accel_mag {m/s2}'].iloc[1], 0.026926, 4)
        self.assertAlmostEqual(df['Accel_mag {m/s2}'].iloc[2], 0.0, 4)
        self.assertAlmostEqual(df['Accel_mag {m/s2}'].iloc[3], 0.026926, 4)

        # Check the column names. 
        assert df.columns[0] == "Accel_x {m/s2}"
        assert df.columns[1] == "Accel_y {m/s2}"
        assert df.columns[2] == "Accel_z {m/s2}"
        assert df.columns[3] == "Accel_mag {m/s2}"
        

    def test_plot_acceleration(self):
        # To make sure we're testing a clean directory, remove any plots before 
        # running the test routine.
        if os.path.exists("Accel_Components.png"):
            os.remove("Accel_Components.png")

        if os.path.exists("Accel_Magnitude.png"):
            os.remove("Accel_Magnitude.png")

        my_assignment = Assignment1()

        # Create a dataframe containing mock data.
        test_df = pd.DataFrame({
            "Time {s}": [0.0, 0.1, 0.2, 0.3],
            "Accel_x {m/s2}": [0.01, 0.020, 0.0, -0.020],
            "Accel_y {m/s2}": [0.01, 0.015, 0.0, -0.010],
            "Accel_z {m/s2}": [0.01, 0.010, 0.0, -0.015],
            "Accel_mag {m/s2}": [0.017321, 0.026926, 0.0, 0.026926],
        })
        test_df.set_index("Time {s}", inplace=True)

        # Run the plot_acceleration method.
        my_assignment.plot_acceleration(test_df)
        
        # Check that a figure has been created in the current working directory.
        assert os.path.exists("Accel_Components.png")
        assert os.path.exists("Accel_Magnitude.png")


    def test_check_requirement(self):
        my_assignment = Assignment1()

        # Create a dataframe containing mock data.
        test_df = pd.DataFrame({
            "Time {s}": [0.0, 0.1, 0.2, 0.3],
            "Accel_x {m/s2}": [0.01, 0.020, 0.0, -0.020],
            "Accel_y {m/s2}": [0.01, 0.015, 0.0, -0.010],
            "Accel_z {m/s2}": [0.01, 0.010, 0.0, -0.015],
            "Accel_mag {m/s2}": [0.017321, 0.026926, 0.0, 0.026926],
        })
        test_df.set_index("Time {s}", inplace=True)
        
        # Run the check_requirement method.
        pass_status = my_assignment.check_requirement(test_df)

        # Using this test data, the requirement should pass.
        # Note that this is equivalent to assert pass_status == True
        assert pass_status


    def test_main(self):
        # Perform a full integrated test using the supplied test data.
        my_assignment = Assignment1()

        pass_status = my_assignment.main(os.path.join("data", "accel_data.csv"))

        # Using the real data, the pass status should be false.
        # Note that this is equivalent to assert pass_status == False
        assert not pass_status