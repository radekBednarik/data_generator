# Data Generator

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Random Data Generator.

Create dataset with random data of datatypes int, float and str. Other datatypes, most importantly date will be added in the future.

Data are exported to .csv files.

Data are created using CLI commands.

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
- currently, these datatypes are supported: **int, str, float**

### CLI syntax

- enter _python3 -m data_generator data -h_ to display basic help
- to specify integers:

  - <column_name>:int:<lower_bound>:<upper_bound> - lower_bound can be negative

- to specify floats:

  - <column_name>:float:<lower_bound>:<upper_bound> - lower_bound can be negative. You must provide decimal digit, even if it is zero, like so: xxx.0

- to specify str:

  - <column_name>:str:<lower_bound>:<upper_bound> - lower_bound cannot be negative.

#### Formatting checks

Basic check is done after CLI command is entered, whether argument values for data parser conforms to the syntax described above. It is not exhaustive, but should stop you from the major typos like forgetting the :, or .0, etc...

### Examples:

- python3 -m data_generator data column1:str:0:50 column2:str:101:101 column3:int:10:10 column4:int:0:1000 column5:float:0.0:1000.0 1000

  - this will generate .csv file with 1000 rows of five columns with random data. First columns is of datatype str, it is str with variable length between 0 - 50 chars. Second column is str with fixed lenght of 101 chars. Third columns is int of the SAME VALUE of 10. Fourth column is int of variable size between 0 - 1000. Fifth column is float of variable size between 0.0 - 1000.0.

  - 1000 - indicates how many rows will be generated

  - generated .csv file is saved into default _output_ folder. This can be changed using _-f_ or _--folder_ parameter

- python3 -m data_generator data -h

  - this will display help

- python3 -m data_generator data header_with_underscore:str:10:10 100 -f my_output_folder/subfolder

  - this will generate one "column" of random str data of fixed 10 chars lenght with 100 rows into the target folder of your choice. If the folder does not exist, it will be created

  - notice, that you can use \_ separator in the header names. Other separators like - are not permitted.

- python3 -m data_generator data data_with_negative_int:int:-1000:1000 data_with_negative_float:float:-100000.0:0.0 10000

  - this will generate 10 rows of data with integer in the interval <-1000, 1000> and float in the inteval <-100000.0, 0.0>
