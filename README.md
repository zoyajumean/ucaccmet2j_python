# UCACCMET2J Python assignment

This file contains some information about the dataset you will be working with for this assignment. The data itself is included with this repository. Please make sure that you have first forked the repository to your own GitHub account before cloning it to your computer and starting to work on it.

## Does it always rain in Seattle?

### The data

You are provided with two datasets: one set contains weather stations associated with their locations, in the form of a CSV file. This file is called `stations.csv` and contains 4 entries. The other set contains rain in tenths of millimeters per day per weather station in 2010. This file is called `precipitation.json` and contains approximately 1450 entries. Take a look at the two files and their structure.

### The big data

Load the JSON data and loop through it. We want you to calculate the monthly mm of rain for Seattle, as well as the total mm of rain over the whole year.

### Relatively rainy

Next, we want you to calculate the percentage of the yearly rain per month; i.e., if 20% of the rain in 2010 in Seattle fell in November, the corresponding value should read 0.2.

### Results

Save these results in a single JSON file called `result[i].json`, where `[i]` should be replaced with the part of the assignment you have gotten to (so `result1.json` for part 1, `result2.json` for part 2, or `result3.json` for part 3). Save your data as a dictionary with the location name as the key, and the value being another dictionary containing the corresponding state, weather station, precipitation per month, relative precipitation per month, and total precipitation.

An partial example of correct output (with values left out) for Cincinnati would be:

```python
{
	"Cincinnati": {
		"station": "GHCND:USW00093814", 
		"state": "OH", 
		"totalMonthlyPrecipitation": [...], 
		"relativeMonthlyPrecipitation": [...], 
		"totalYearlyPrecipitation": ...,
		"relativeYearlyPrecipitation": ...
	},
	...
}
```
