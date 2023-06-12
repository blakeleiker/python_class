
# Introduction to Python 

This repository contains course materials for an introductory course on the Python programming language. 

## Getting started

Your first task is to create a new python virtual environment. To do this, first you need to install pip3 and virtualenv.

On Ubuntu:

```shell
apt-get install python3-pip
pip3 install virtualenv
```

On Centos:

```shell
yum install python3-pip
pip3 install virtualenv
```

If you don't have permissions to install things via `apt-get` or `yum`, here is the recommended method for installing `pip3` without root privileges:

```shell
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
```

Next, check that `pip3` and `virtualvenv` are working properly:

```shell
pip3 --version
virtualenv --version
```

If the version numbers for pip and virtualvenv are output, then everything is installed correctly. If it can't find `pip3`, it probably installed it somewhere that's not on your PATH. Try this:

```shell
PATH=$PATH:$HOME/.local/bin
```

Next, clone this repository and create your Python 3 virtualenv.

```shell
git clone https://github.com/blakeleiker/python_class.git
cd python_class/py_env
# Create a new environment named venv:
virtualenv -p /usr/bin/python3 venv
# Activate this environment:
source venv/bin/activate
# Install all of the packages listed in requirements.txt to this environment:
pip3 install -r requirements.txt
```

Now, you're ready to start the [first assignment](modules/Assignment1)!

## References
Here's a list of useful resources for more information.

Documentation and tutorials:

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
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
