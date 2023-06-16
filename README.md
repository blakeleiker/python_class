
# Introduction to Python 

This repository contains course materials for an introductory course on the Python programming language. 

## Getting started

Your first task is to create a new python virtual environment. To do this, first you need to install pip3 and virtualenv. 

Note that these instructions assuming that you are working in a Linux environment. The process is similar for OSX or Windows, but I don't cover it here. Refer to the official pip installation instructions for all possible installation methods.

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

If you don't have permissions to install things via your system's package manager, here is the recommended method for installing `pip3` without root privileges:

```shell
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
```

You can test that pip is installed correctly by typing this command:

```shell
pip3 --version
```

If it can't find `pip3`, pip has probably been installed somewhere that's not on your PATH. Try this:

```shell
PATH=$PATH:$HOME/.local/bin
```

### Installing Virtualenv

Once pip has been installed, you can use pip to install a package called virtualenv. This package provides a helpful interface to create and manage your python virtual environments.

```shell
pip3 install virtualenv
```

Again, its possible that you won't be able to run this command because you don't have installation permissions in your current working environment. You can install virtualenv to an allowable location by adding the `--user` option, shown below.

```shell
pip3 install --user virtualenv
```

Next, check that `virtualvenv` is working properly by typing this command:

```shell
virtualenv --version
```

If you're able to get the version numbers for pip and virtualvenv, then everything is installed correctly. 

Next, clone this repository and create your Python 3 virtualenv.

```shell
git clone https://github.com/blakeleiker/python_class.git
cd python_class/py_env
# Create a new environment named venv:
virtualenv -p /usr/bin/python3 venv
# Activate this environment:
source venv/bin/activate
```

Note that if your virtual environment has been activated successfully, your terminal prompt should now start with `(venv)`. Every time you open a new terminal session, you will need to `source` the `activate` script in order to run the assignments in this course. 

But you're not done yet! We've created a new virtual environment, and now that we have activated the environment we can install our desired python packages to that environment. Run the following command to install all of our packages.

```shell
# Install all of the packages listed in requirements.txt to this environment:
pip3 install -r requirements.txt
```

Note that in the above command, we're installing every package contained in the file `py_env/requirements.txt`. You can open this file up to inspect which packages we've chosen to install. This is a common way for python projects to organize their package dependencies. 

Now, you're ready to start the [first assignment](modules/Assignment1)!

## References
Here's a list of useful resources for more information.

Documentation and tutorials:

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [The Full Python Language Reference](https://docs.python.org/3/index.html)
- [Virtual Environments](https://virtualenv.pypa.io)
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
