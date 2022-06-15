import os
import pandas as pd
import numpy as np


class Assignment1:

    def main(self, data_path=""):
        df = self.parse_csv(data_path)
        df = self.compute_magnitude(df)
        self.plot_acceleration(df)
        pass_status = self.check_requirement(df)

        return pass_status

    def parse_csv(self, csv_path):
        # Part 1! Load the csv into a DataFrame, and return the DataFrame.

        pass

    def compute_magnitude(self, df):
        # Part 2! Compute the magnitude, and return the DataFrame, including a 
        # new column containing the magnitude.

        pass

    def plot_acceleration(self, df):
        # Part 3! Plot the acceleration components, as well as the acceleration magnitude.

        pass

    def check_requirement(self, df):
        # Part 4! Check every element in the Magnitude column against the requirement.

        pass

 
if __name__ == "__main__":

    # Instantiate an instance of an "Assignment1" object
    my_assignment_object = Assignment1()

    # Run the "main" method
    my_assignment_object.main(os.path.join("data", "accel_data.csv"))