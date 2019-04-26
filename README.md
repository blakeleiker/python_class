
# Trajectories in Google Earth with Python

Instructions for plotting Trick sim trajectories in Google Earth.

## Getting started
First install pip and virtualenv

```shell
sudo apt-get install python-pip
pip install virtualenv
```

Next, clone the repository and setup your Python 2.7 virtualenv
```shell
git clone TBD
cd google_earth_trajectories
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate
pip install -r requirements.txt
```

Install Google Earth. Instructions for Ubuntu provided below. See 
[here](https://www.google.com/earth/download/gep/agree.html) 
for more info

```shell
wget https://dl.google.com/dl/earth/client/current/google-earth-stable_current_amd64.deb
sudo dpkg -i google-earth-stable*.deb
sudo apt-get -f install
```

Lastly, run the plot_trajectories application:

```shell
python plot_trajectories.py
```
