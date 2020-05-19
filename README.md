# Data Generator

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Random Data Generator.

Create dataset with random data of datatypes int, float and str.

Data are exported to .csv files.

Data are created using CLI commands.

**This project is in alpha stage, so expect bugs and debug logs in the console. Also, some part of the codebase is still a mess, sorry for that :)**.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

- Python 3.8+ with pip

### Installing

- clone this repo
- switch to project directory root
- run _[sudo] python3 setup.py install_

## Usage <a name = "usage"></a>

- data parameters are provided via CLI commands
- currently, these datatypes are supported: int, str, float

### CLI syntax

- enter _python3 -m data_generator data -h_ to display basic help
- to specify integers:

  - <column_name>:int:<lower_bound>:<upper_bound> - lower_bound can be negative

- to specify floats:

  - <column_name>:float:<lower_bound>:<upper_bound> - lower_bound can be negative. You must provide decimal digit, even if it is zero, like so: xxx.0

- to specify str:

  - <column_name>:str:<lower_bound>:<upper_bound> - lower_bound cannot be negative.

### Examples:

- python3 -m data_generator data column1:str:0:50 column2:str:100:100 column3:int:10:10 column4:int:0:1000 column5:float:0.0:1000.0 1000

  - this will generate .csv file with 1000 rows of five columns with random data. First columns is of datatype str, it is str with variable length between 0 - 50 chars. Second column is str with fixed lenght of 100 chars. Third columns is int of fixed size of 10. Fourth column is int of variable size between 0 - 1000. Fifth column is float of variable size between 0.0 - 1000.0.

  - 1000 - indicates how many rows will be generated

- python3 -m data_generator data -h

  - this will display help
