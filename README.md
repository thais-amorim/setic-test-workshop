# setic-test-workshop

Project base to be used on the workshop "Teste de software para não-testers".

Features
=========

+ Simple Calculator:
   + Add
   + Substract
   + Multiply
   + Divide
+ Tests:
   + Basic unit test
   + Parametrized test
   + Unit tests using white-box techniques
   + Unit tests using black-box techniques
+ CLI interface

Requirements
============

+ Python 3 
+ Pip 3
+ Virtualenv

How to install
============
```
# Clone the project to yout computer
$ git clone https://github.com/thasmarinho/setic-test-workshop.git

# Access the repo's folder
$ cd setic-test-workshop

# Create a virtual environment called "setic"
$ virtualenv setic

# Activate the virtual environment
$ source setic/bin/activate

# Install dependencies
$ pip3 install -r requirements.txt
```

How to use
-------------
```
$ python3 -m main --help

$ python3 -m main calc --help

$ python3 -m main calc -o 0 -x 5 -y 3 
```

How to test
-------------
```
$ python3 -m pytest -r test
```
