# Does it always rain in Seattle?

This repository contains data, helpers and some information about the dataset
for the UCACCMET2J assignment "Does it always rain in Seattle".

Please make sure that you have first forked the repository to your own GitHub account
before cloning it to your computer and starting to work on it.

## Data

You are provided with two datasets:
one set contains weather stations associated with their locations, in the form of a CSV file.
This file is called `stations.csv` and contains 4 entries.
The other set contains rain in tenths of millimeters per day per weather station in 2010.
This file is called `precipitation.json` and contains approximately 1450 entries.

## Results

The desired output for is a `results.json` file;
each part will output this file, but the contents depends on the part.
This JSON file should contain a dictionary with the location name as the key,
and the value being another dictionary containing:
the corresponding state, weather station,
total precipitation per month (part 1),
relative precipitation per month (part 2),
total precipitation over the year (part 3),
and what proportion that is from all precipitation (part 3).
A partial example of correct output after part 3 (with values left out):

```python
{
    "Cincinnati": {
        "station": "GHCND:USW00093814",
        "state": "OH",
        "total_monthly_precipitation": [...],
        "total_yearly_precipitation": ...,
        "relative_monthly_precipitation": [...],
        "relative_yearly_precipitation": ...
    },
    "Tucson": {
    ...
}
```

## Plotting

This repository also contains a Python script called `plot_results.py`,
which you can run to visualise results.
This will only work if your code outputs a `results.json` file that follows
the exact specifications above.
Running this script is not an inherent part of the assignment, but it can be
a nice reward for staring at Python code for several hours, and additionally
it allows you to check whether the `results.json` file that you produced is in the correct format.

Before you can run the `plot_results.py` script,
you will need to install a Python package.
You should be able to do this by running the following command from your terminal
(either bash or PowerShell):

```python
    pip3 install plotnine
```
