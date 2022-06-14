# Assignment 1 

You're a hotshot engineer testing a new, experimental accelerometer. The lab just sent over a CSV file containing acceleration data from a test, and its up to you to use your incredible python skills to process this data and ensure that the sensor meets performance requirements. Your task is to write a class to parse the csv file, compute the magnitude of the data, and plot the results.

To help you succeed, I went ahead and wrote the test for this class to ensure that it behaves as expected. To run the test, navigate into the `modules/Assignment1` directory and run pytest. Make sure that your virtual environment is active first! 

```bash
cd modules/Assignment1
pytest
```

Pytest will automatically detect that the file `Assignment1_test.py` is a unit test, and it will run every test function in the `TestAssignment1` class. Try running the test before completing the assignment to see what it looks like when a test fails horribly.

Alternatively, you can run the `Assignment1.py` script directly.

```bash 
python Assignment.py
```

## Part 1

Load the csv located in `data/accel_data.csv` into a Pandas dataframe. Set the index of your dataframe to be the Time column of the csv. Return the dataframe.

## Part 2

Compute and plot the magnitude of the acceleration signal. Put the acceleration signal into a new column named `Accel_mag {m/s2}`. Return the updated dataframe.

## Part 3 

Plot the acceleration components and the acceleration magnitude. Save one figure to a PNG file named `Accel_Components.png`, and save the other to a file called `Accel_Magnitude.png`.

## Part 4

Check if the magnitude of the signal is ever higher than **0.03 m/s2**. Return `True` if the magnitude is always less than this requirement and return `False` if the magnitude is ever greater than or equal to the requirement.

#### Hints

- Pandas includes a handy `read_csv` function. Read the docs!
- To compute the magnitude, you want to compute the norm (`numpy.linalg.norm`) across the columns `Accel_x {m/s2}`, `Accel_y {m/s2}`, and `Accel_z {m/s2}`.
- StackOverflow is your friend. 