from __future__ import print_function
import os, collections, glob, csv
# Example of a Python module with Google Style docstrings:
# Reference for documentation style guide:
# http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html


def parse_trick_ascii(csv_file):
    """ Function that converts Trick simulation data in an ASCII (CSV)
        format into a Python dictionary.

    Args:
        csv_file (str): Full name of a CSV file containing Trick
            ASCII simulation data.

    Returns:
        dict: Trick simulation data as a Python dictionary with
            the simulation variable as the key and a list of values
            as the value.
    Example:
        Here's an example of how to call this function and access
        your simulation data::

            $ sim_data_dict = parse_trick_ascii("sample_file.csv")
            $ print sim_data_dict["sys.exec.out.time"]
    """
    data_file = csv.DictReader(open(csv_file))
    single_run_data_dict = {'altitude' : [0.0],
                            'latitude' : [0.0],
                            'longitude' : [0.0]}
    # Your code here
    # ...
    # return the dict
    return single_run_data_dict


def parse_mc_data_trick_ascii(mc_data_dir, dr_group):
    sim_data_all_runs = {}
    # Your code here
    # ...
    # return the dict
    return sim_data_all_runs

class SingleRun(collections.MutableMapping):

    def __init__(self, *args, **kwargs):
        self.store = parse_trick_ascii(os.path.join(kwargs["sim_data_dir"], kwargs["dr_group"] + ".csv"))
        # Do not want to add these as keys to our dictionary object
        kwargs.pop("sim_data_dir")
        kwargs.pop("dr_group")
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)


class MonteCarloRun(collections.MutableMapping):

    def __init__(self, *args, **kwargs):
        self.store = dict()
        if not os.path.isdir(kwargs["sim_data_dir"]) : raise IOError
        self.store = parse_mc_data_trick_ascii(kwargs["sim_data_dir"], kwargs["dr_group"])
        if not self.store.keys():
            print("Sim data for group : " + kwargs["dr_group"] + " not found in " + kwargs["sim_data_dir"])
            print("Check your data.")
            raise IOError
        # Do not want to add these as keys to our dictionary object
        kwargs.pop("sim_data_dir")
        kwargs.pop("dr_group")
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)
