# MarvinTheParanoidAndroid

[![Build Status](https://travis-ci.org/lnstempunks/MarvinTheParanoidAndroid.svg?branch=master)](https://travis-ci.org/lnstempunks/MarvinTheParanoidAndroid)
[![Documentation Status](https://readthedocs.org/projects/marvintheparanoidandroid/badge/?version=latest)](https://marvintheparanoidandroid.readthedocs.io/en/latest/?badge=latest)

Our code for the 2019 FIRST Robotics Competition Season. This goes with our 2019 robot, Rosetta.



## Installation: 

```git clone https://github.com/lnstempunks/marvintheparanoidandroid```

```pip3 install pipenv```

```pipenv install```

## Style

Run ```black .``` prior to committing any changes, as style is enforced by CI.
See [PEP 8](https://www.python.org/dev/peps/pep-0008/) and [PEP 257](https://www.python.org/dev/peps/pep-0257/) for style guidance.

## Checks

Code should pass ```pyflakes .``` prior to commit, as static analysis is also checked by CI.

## Running

### Run simulator
```python3 robot.py sim```
### Run tests
```python3 robot.py test```
### Deploy to robot
```python3 robot.py deploy```

To edit any changes in IPs or radios, edit or delete the ```.deploy_cfg``` file.
