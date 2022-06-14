
# Introduction to Python 

This repository contains course materials for an introductory course on the Python programming language. 

## Getting started

First, install pip3 and virtualenv.

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

To check that `pip3` and `virtualvenv` are working properly:

```shell
pip3 --version
virtualenv --version
```

If it can't find `pip3`, it probably installed it somewhere that's not on your PATH. Try this:
```shell
PATH=$PATH:$HOME/.local/bin
```


Next, clone this repository and setup your Python 3 virtualenv.
```shell
git clone https://github.com/blakeleiker/python_class.git
cd python_class/py_env
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Now, you're ready to start the [first assignment](modules/Assignment1)!

## References
Here's a list of useful resources for more information.

1. [Ten Famous Python Applications](http://www.hartmannsoftware.com/Blog/Articles_from_Software_Fans/Most-Famous-Software-Programs-Written-in-Python)
2. [The Incredible Growth of Python](https://stackoverflow.blog/2017/09/06/incredible-growth-python/)
3. [Official Python Tutorial](https://docs.python.org/3/tutorial/)
4. [Why Test Driven Development](https://medium.com/@gondy/the-importance-of-test-driven-development-f80b0d02edd8)
5. [How to do Test Driven Development in Python](https://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137)
6. [Python IDE Options](http://www.it4nextgen.com/7-best-ides-for-python-programming-in-2018/)
7. [Virtual Environments](https://virtualenv.pypa.io)
8. [Pip](https://pypi.org/project/pip/)
9. [General Python Tutorial](http://www.scipy-lectures.org/intro/language/python_language.html)
10. [Modules and Code Re-Use](http://www.scipy-lectures.org/intro/language/reusing_code.html)
11. [Object Oriented Programming](http://www.scipy-lectures.org/intro/language/oop.html)
12. [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
13. [Jupyter Notebook Tutorial]()

## Contacts

Need python help? Feel free to contact the course instructors: 

- Blake Leiker (blake.a.leiker@nasa.gov)
- Otney Crawford (otney.b.crawford@nasa.gov)
