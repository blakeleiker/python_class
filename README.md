
# Introduction to Python 

This repository contains course materials for an introductory course on the Python programming language. 

## Getting started

Your first task is to create a new python virtual environment which will contain the packages that we need for this course. To do this, first you need to install pip3. 

Note that these instructions assuming that you are working in a Linux environment. The process is similar for OSX or Windows, but I don't cover it here. Refer to the official pip installation instructions for all possible installation methods.

Before attempting to install pip, check to see if you already have it installed! Do this by typing the following command in a terminal. If this command returns a version number, `pip3` is already installed, and you can skip ahead to the section on [creating the virtual environment](#Create-the-Virtual-Environment).


```shell
pip3 --version
```

### Installing Pip

Pip is the official package manager for python. You can use pip to install many useful packages, and we're going to use pip to install the packages required to complete the assignments in this course. 

On Ubuntu:

```shell
apt-get install python3-pip
```

On Centos:

```shell
yum install python3-pip
```

On Rocky8:

```shell
dnf install python3-pip
```

If you don't have permissions to install things via your system's package manager, here is the recommended method for installing `pip3` without root privileges:

```shell
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
```

You can test that pip is installed correctly by typing this command: `pip3 --version`

If it can't find `pip3`, pip has probably been installed somewhere that's not on your PATH. Try this:

```shell
PATH=$PATH:$HOME/.local/bin
```

### Create the Virtual Environment

Once you've got pip installed, you're ready to start the course!

The next step is to clone this repository and run the following commands to create your Python 3 virtual environment.

```shell
git clone https://github.com/blakeleiker/python_class.git
cd python_class
# Create a new environment named tutorial-env:
python3 -m venv tutorial-env
# Activate this environment:
source tutorial-env/bin/activate
```

Note that if your virtual environment has been activated successfully, your terminal prompt should now start with `(tutorial-env)`. Every time you open a new terminal session, you will need to run the command `source tutorial-env/bin/activate` to "activate" virtual environment in order to run the assignments in this course. 

But you're not done yet! We've created a new virtual environment, and now that we have activated the environment we can install our desired python packages to that environment. Run the following command to install all of our packages.

```shell
# Install all of the packages listed in requirements.txt to this environment:
pip3 install -r requirements.txt
```

What the above command is doing is installing every package contained in the file `requirements.txt`. You can open this file up to inspect which packages we've chosen to install. This is a common way for python projects to organize their package dependencies. 

Now, you're ready to start the [first assignment](modules/Assignment1)!

## References
Here's a list of useful resources for more information.

Documentation and tutorials:

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [The Full Python Language Reference](https://docs.python.org/3/index.html)
- [Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Pip](https://pypi.org/project/pip/)
- [General Python Tutorial](http://www.scipy-lectures.org/intro/language/python_language.html)
- [Modules and Code Re-Use](http://www.scipy-lectures.org/intro/language/reusing_code.html)
- [Object Oriented Programming](http://www.scipy-lectures.org/intro/language/oop.html)
- [Numpy Tutorial](https://numpy.org/doc/stable/)
- [Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/index.html)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Jupyter Notebook Tutorial](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

Interesting articles:

- [Ten Famous Python Applications](http://www.hartmannsoftware.com/Blog/Articles_from_Software_Fans/Most-Famous-Software-Programs-Written-in-Python)
- [The Incredible Growth of Python](https://stackoverflow.blog/2017/09/06/incredible-growth-python/)
- [Why Test Driven Development](https://medium.com/@gondy/the-importance-of-test-driven-development-f80b0d02edd8)
- [How to do Test Driven Development in Python](https://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137)
- [Python IDE Options](http://www.it4nextgen.com/7-best-ides-for-python-programming-in-2018/)

## Contacts

Need python help? Feel free to contact the course instructors: 

- Blake Leiker (blake.a.leiker@nasa.gov)
- Otney Crawford (otney.b.crawford@nasa.gov)
