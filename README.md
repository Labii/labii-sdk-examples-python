# labii-sdk examples

[labii-sdk](https://pypi.org/project/labii-sdk/) is an SDK for the [Labii ELN & LIMS platform](https://www.labii.com) that provides interaction with the [Labii API](https://docs.labii.com/api/overview).

In this repository, you'll find some example code on using the Labii SDK.

This page is also available at []()

## Install
```
pip install labii-sdk
```

## Usage
```python
# 1. Install the Labii SDK
pip install labii-sdk

# 2. Import the package
from labii_sdk.sdk import LabiiObject

# 3. Initial the API object
labii = LabiiObject()

# 4. Start querying
labii.api.login()
# get a list of tables
labii.Tables.list()
```

## Pre-request
* python3.8
* labii-sdk
* one labii account. Create one at [https://www.labii.com/signup/](https://www.labii.com/signup/)

## Example 1
![Address widget](https://www.labii.com/media/docs/widget-column-address-readonly.png)
![Address widget](https://www.labii.com/media/docs/widget-column-edit-readonly.png)
To handle address information, Labii recently released a new column widget - Address. In the past, you may have had a few fields to handle one address:
* street address
* city
* state
* zip code
* country

The following example demonstrates how to migrate data from five columns into one address column.

The python document can be found at [./examples/migrate_labii_address.py](./examples/migrate_labii_address.py), then
```
update_address()
```

## About Labii Inc.
[Labii (https://www.labii.com)](https://www.labii.com) facilitates research and development by providing a user-friendly, customizable Electronic Lab Notebook (ELN) and Laboratory Information Management System (LIMS) to document, manage, and interpret data. Labii ELN & LIMS can be configured for any type of data, and the functions can easily be enhanced and expanded by stand-alone applications. We address the unique needs of each of our customers and are the trusted provider of hundreds of biotech companies and academic labs.
