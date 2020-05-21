# Data Generator

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Random Data Generator.

Create dataset with random data of datatypes int, float, str and date (more precisely python's datetime.datetime).

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
- currently, these Python's datatypes are supported: **int, str, float, datetime.datetime**

### OS differences

- there should be no problems running this utility on standard linux distro or on Windows 10
- only difference is:

  - on linux, use _python3_ command

  - on Windows 10, use _python_ command

### CLI syntax

- enter _python3 -m data_generator data -h_ to display basic help
- to specify integers:

  - <column_name>:int:<lower_bound>:<upper_bound> - lower_bound can be negative

- to specify floats:

  - <column_name>:float:<lower_bound>:<upper_bound> - lower_bound can be negative. You must provide decimal digit, even if it is zero, like so: xxx.0

- to specify str:

  - <column_name>:str:<lower_bound>:<upper_bound> - lower_bound cannot be negative.

- to specify date:

  - <column_name>`:date:`<format_template>

    - under the hood, generator works with Python's native datetime module. That means, that all datetime format codes listed <a href = "https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes">HERE</a> should be suppported.

    - as of now, **\_ and -** are permitted as separators

    - for example, format template can look like this: _%Y%m%d\_%H%M%S_. This will display generated random date in format "yyyymmdd_hhmmss".

    - minimum year is 1, maximum year is 9999. See <a href = "https://docs.python.org/3/library/datetime.html#constants">documentation</a>.

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

- python3 -m data*generator data random_dates_without_separators`:date:`%Y%m%d%H%M%S random_dates_with_separators`:date:`%Y-%m-%d_%H-%M-%S 10

  - geneates two columns of random dates with and without using the allowed separators
