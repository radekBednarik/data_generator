# Data Generator

![Upload Python Package](https://github.com/bednaJedna/data_generator/workflows/Upload%20Python%20Package/badge.svg)

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Random Data Generator.

Create dataset with random data of datatypes int, float, str, date (more precisely python's datetime.datetime) and timestamp (as float).

Data can be exported to .csv, .xlsx or .json files.

Data are created using CLI commands or via TOML file specification.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

- Python 3.8+ with pip

### Installing

- just use `[sudo] pip[3] install Data-Generator`

OR:

- clone this repo
- switch to project directory root
- run `[sudo] python3 setup.py install`

## Usage <a name = "usage"></a>

- data parameters can be provided via:

  - command line

  - TOML file

- currently, these Python's datatypes are supported: **int, str, float, datetime.datetime**
- generated data can be exported as **.csv, .xlsx or .json** files

  - using .csv file format does not impact memory, since data is written in the file as they are generated

  - using .xlsx file format does not impact memory, since memory is flushed after each row of data is written. For details, see xlsxwriter's <a href="https://xlsxwriter.readthedocs.io/working_with_memory.html">documentation</a>

  - using .json file format has a memory impact, so be careful about that - this is given by Python's json module implementation, see Note <a href="https://docs.python.org/3/library/json.html#json.dump">HERE</a>. Data has to be firstly completely generated in memory and then written into the file

### OS differences

- there should be no problems running this utility on standard linux distro or on Windows 10
- only difference is:

  - on linux, use _python3_ command

  - on Windows 10, use _python_ command

### CLI syntax

#### General CLI commands

- to display help for main parser in console, run `python[3] -m data_generator -h`
- to display help for **data** parser (when entering specifications via CLI), run `python[3] -m data_generator data -h`
- to display help for **toml** parser (when entering specifications via TOML file), run `python[3] -m data_generator toml -h`

#### Specify output file format

- use optional parameter _-sa_ or _--save_as_

- this parameter belongs to main parser and has to be used before _data_ or _toml_ subparsers and their arguments

- if this parameter is not specified, default output file format is .csv

- parameter's values:

  - csv: csv

  - json: json

  - xlsx: xlsx

- example: `python[3] -m data_generator -sa json data ...`

#### Specify output destination

- use optional parameter _-f_ or _--folder_

- this parameter belongs to main parser and has to be used before _data_ or _toml_ subparsers and their arguments

- example: `python[3] -m data_generator -f my_output_folder ...`

#### Data parser

- to specify integers:

  - `<column_name>:int:<lower_bound>:<upper_bound>` - lower_bound can be negative

- to specify floats:

  - `<column_name>:float:<lower_bound>:<upper_bound>` - lower_bound can be negative. You must provide decimal digit, even if it is zero, like so: xxx.0

- to specify str:

  - `<column_name>:str:<lower_bound>:<upper_bound>` - lower_bound cannot be negative.

- to specify date:

  - `<column_name>:date:<format_template>`

    - under the hood, generator works with Python's native datetime module. That means, that all datetime format codes listed <a href = "https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes">HERE</a> should be suppported.

    - as of now, **\_ and -** are permitted as separators

    - for example, format template can look like this: _%Y%m%d\_%H%M%S_. This will display generated random date in format "yyyymmdd_hhmmss".

    - minimum year is 1, maximum year is 9999. See <a href = "https://docs.python.org/3/library/datetime.html#constants">documentation</a>.

- to specify timestamp:

  - `<column_name>:timestamp:`

  - generator will generate datetime.datetime object of random date, with minimum year of 1970 and from it returns corresponding POSIX timestamp as float. For details see <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp">documentation</a>

##### Formatting checks

Basic check is done after CLI command is entered, whether argument values for data parser conforms to the syntax described above. It is not exhaustive, but should stop you from the major typos like forgetting the :, or .0, etc...

##### CLI examples for Data parser:

- `python3 -m data_generator data column1:str:0:50 column2:str:101:101 column3:int:10:10 column4:int:0:1000 column5:float:0.0:1000.0 1000`

  - this will generate .csv file with 1000 rows of five columns with random data. First columns is of datatype str, it is str with variable length between 0 - 50 chars. Second column is str with fixed lenght of 101 chars. Third columns is int of the SAME VALUE of 10. Fourth column is int of variable size between 0 - 1000. Fifth column is float of variable size between 0.0 - 1000.0.

  - 1000 - indicates how many rows will be generated

  - generated .csv file is saved into default _output_ folder. This can be changed using _-f_ or _--folder_ parameter

- `python3 -m data_generator -f my_output_folder/subfolder data header_with_underscore:str:10:10 100`

  - this will generate one "column" of random str data of fixed 10 chars lenght with 100 rows into the target folder of your choice. If the folder does not exist, it will be created

  - notice, that you can use \_ separator in the header names. Other separators like - are not permitted.

- `python3 -m data_generator data data_with_negative_int:int:-1000:1000 data_with_negative_float:float:-100000.0:0.0 10000`

  - this will generate 10 rows of data with integer in the interval <-1000, 1000> and float in the inteval <-100000.0, 0.0>

- `python3 -m data_generator data random_dates_without_separators:date:%Y%m%d%H%M%S random_dates_with_separators:date:%Y-%m-%d_%H-%M-%S 10`

  - generates two columns of random dates with and without using the allowed separators

- `python3 -m data_generator -sa json data data_with_negative_int:int:-1000:1000 data_with_negative_float:float:-100000.0:0.0 10000`

  - this will generate data as .json file

#### TOML parser

- when you want to generate datafile with lots of fields, or event multiple files with different specs, it may be useful to be able to specify properties of fields permanently.

- in this case, you can use configuration files, which use <a href="https://github.com/toml-lang/toml">TOML syntax</a>. Two example files can be found in the root of this project. Just copy & paste and add as many fields as you like.

- files can be saved anywhere, just have the path ready

##### CLI examples for TOML parser

- `python[3] -m data_generator toml data_config_example01.toml data_config_example02.toml`

  - this will generate two outputs files according to specifications in these two .TOML files.

- `python[3] -m data_generator toml /custom/path/to/data_config_example01.toml`

  - this will generate one output via specification file in custom location
