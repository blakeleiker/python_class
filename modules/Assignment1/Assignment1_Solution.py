import os
import numpy as np
import pandas as pd


class Assignment1:

    requirement_limit = 0.03

    def main(self, data_path=""):
        df = self.parse_csv(data_path)
        df = self.compute_magnitude(df)
        self.plot_acceleration(df)
        pass_status = self.check_requirement(df)
        print(f"pass_status={pass_status}")

        return pass_status

    def parse_csv(self, csv_path):

        # File path can be passed directly into pandas.read_csv.
        df = pd.read_csv(csv_path)

        df.set_index("Time {s}", inplace=True)

        return df

    def compute_magnitude(self, df):
        magnitude = np.linalg.norm(
            df[["Accel_x {m/s2}", "Accel_y {m/s2}", "Accel_z {m/s2}"]].values,
            axis=1,
        )

        df["Accel_mag {m/s2}"] = magnitude

        return df

    def plot_acceleration(self, df):

        # Plot the acceleration vector components.
        ax = df[["Accel_x {m/s2}", "Accel_y {m/s2}", "Accel_z {m/s2}"]].plot(
            title="Acceleration Data",
            grid=True,
        )
        ax.set_ylabel("Acceleration [m/s2]")
        ax.legend(["X", "Y", "Z"], loc="best")

        ax.get_figure().savefig("Accel_Components.png")

        # Plot the acceleration magnitude.
        ax = df[["Accel_mag {m/s2}"]].plot(
            title="Acceleration Magnitude",
            grid=True,
        )

        # Plot the acceleration requirement on top of the magnitude.
        ax.plot(
            df.index, 
            np.ones(len(df))*self.requirement_limit, 
            label="Requirement",
            color="r",
            linestyle="dashed"
        )

        ax.set_ylabel("Acceleration [m/s2]")
        ax.legend(loc="best")

        ax.get_figure().savefig("Accel_Magnitude.png")

    def check_requirement(self, df):

        return (df["Accel_mag {m/s2}"] < self.requirement_limit).all()


if __name__ == "__main__":
    my_assignment_object = Assignment1()

    my_assignment_object.main(os.path.join("data", "accel_data.csv"))
