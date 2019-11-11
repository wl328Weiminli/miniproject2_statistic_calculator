# miniproject2_statistic_calculator

[![Build Status](https://travis-ci.com/wl328Weiminli/miniproject2_statistic_calculator.svg?branch=master)](https://travis-ci.com/wl328Weiminli/miniproject2_statistic_calculator)

## Team members
 * Weimin Li UCID: wl328
 * Jiaxin Du UCID: jd688
 
## Change Log

- [x] add basic Calculators _--Weimin Li_
- [ ] add Population Mean
- [ ] add Median
- [ ] add Mode
- [ ] add Population Standard Deviation
- [ ] add Variance of population proportion
- [ ] add Z-Score
- [ ] add Standardized score
- [ ] add Population Correlation Coefficient
- [ ] add Confidence Interval
- [ ] add Population Variance
- [ ] add P Value
- [ ] add Proportion
- [ ] add Sample Mean
- [ ] add Sample Standard Deviation
- [ ] add Variance of sample proportion

## Functions
Function description

### Population Mean
The population mean is an average of a group characteristic. The group could be a person, item, or thing, like “all the people living in the United States” or “all dog owners in Georgia”. A characteristic is just an item of interest. For example:

The formula to find the population mean is:

μ = (Σ * X)/ N

where:

**Σ** means “the sum of.”

**X** = all the individual items in the group.

**N** = the number of items in the group.

### Median
### mean of Median
This article is about the statistical concept. For other uses, see Median (disambiguation).

Finding the median in sets of data with an odd and even number of values
The median is the value separating the higher half from the lower half of a data sample (a population or a probability distribution). For a data set, it may be thought of as the "middle" value. For example, in the data set {1, 3, 3, 6, 7, 8, 9}, the median is 6, the fourth largest, and also the fourth smallest, number in the sample. For a continuous probability distribution, the median is the value such that a number is equally likely to fall above or below it.

The median is a commonly used measure of the properties of a data set in statistics and probability theory. The basic advantage of the median in describing data compared to the mean (often simply described as the "average") is that it is not skewed so much by a small proportion of extremely large or small values, and so it may give a better idea of a "typical" value. For example, in understanding statistics like household income or assets, which vary greatly, the mean may be skewed by a small number of extremely high or low values. Median income, for example, may be a better way to suggest what a "typical" income is.

### How to use it in my statistic
    population_mean()
in the (), you should input a list like [1, 2, 3, 4, 5]


### Mode
### What is mean
The mode of a sample is the element that occurs most often in the collection. For example, the mode of the sample [1, 3, 6, 6, 6, 6, 7, 7, 12, 12, 17] is 6. Given the list of data [1, 1, 2, 4, 4] the mode is not unique – the dataset may be said to be bimodal, while a set with more than two modes may be described as multimodal.

For a sample from a continuous distribution, such as [0.935..., 1.211..., 2.430..., 3.668..., 3.874...], the concept is unusable in its raw form, since no two values will be exactly the same, so each value will occur precisely once. In order to estimate the mode of the underlying distribution, the usual practice is to discretize the data by assigning frequency values to intervals of equal distance, as for making a histogram, effectively replacing the values by the midpoints of the intervals they are assigned to. The mode is then the value where the histogram reaches its peak. For small or middle-sized samples the outcome of this procedure is sensitive to the choice of interval width if chosen too narrow or too wide; typically one should have a sizable fraction of the data concentrated in a relatively small number of intervals (5 to 10), while the fraction of the data falling outside these intervals is also sizable. An alternate approach is kernel density estimation, which essentially blurs point samples to produce a continuous estimate of the probability density function which can provide an estimate of the mode.
### How to use it in our project
    mode()
in the (), you should input a list like [1, 2, 3, 4, 5, 1, 1, 4, 8]

### Population Standard Deviation
### What is the mean of Standard Deviation
In statistics, the standard deviation (SD, also represented by the lower case Greek letter sigma σ for the population standard deviation or the Latin letter s for the sample standard deviation) is a measure of the amount of variation or dispersion of a set of values.[1] A low standard deviation indicates that the values tend to be close to the mean (also called the expected value) of the set, while a high standard deviation indicates that the values are spread out over a wider range.

The standard deviation of a random variable, statistical population, data set, or probability distribution is the square root of its variance. It is algebraically simpler, though in practice less robust, than the average absolute deviation.[2][3] A useful property of the standard deviation is that, unlike the variance, it is expressed in the same units as the data.

In addition to expressing the variability of a population, the standard deviation is commonly used to measure confidence in statistical conclusions. For example, the margin of error in polling data is determined by calculating the expected standard deviation in the results if the same poll were to be conducted multiple times. This derivation of a standard deviation is often called the "standard error" of the estimate or "standard error of the mean" when referring to a mean. It is computed as the standard deviation of all the means that would be computed from that population if an infinite number of samples were drawn and a mean for each sample were computed.
### Formula
![images](/images/a.PNG)
where {\displaystyle \textstyle \{x_{1},\,x_{2},\,\ldots ,\,x_{N}\}}{\displaystyle \textstyle \{x_{1},\,x_{2},\,\ldots ,\,x_{N}\}} are the observed values of the sample items and {\displaystyle \textstyle {\bar {x}}}{\displaystyle \textstyle {\bar {x}}} is the mean value of these observations, while the denominator N stands for the size of the sample: this is the square root of the sample variance, which is the average of the squared deviations about the sample mean.
### How to use it in our project
    population_standard_deviation()
in the (), you should input a list like [1, 2, 3, 4, 5, 1, 1, 4, 8]

### Variance of population proportion
In the statistical description, the variance is used to calculate the difference between each variable (observation) and the population mean. In order to avoid the sum of the mean deviations being zero, the square of the mean difference and the content of the sample, the statistics use the sum of squared mean deviations to describe the degree of variation of the variables. The formula for calculating the variance of the population:
![images](/images/b.PNG)
### How to use it in our project
     population_variance()
in the (), you should input a list like [1, 2, 3, 4, 5, 1, 1, 4, 8]

### Z-Score
### What Is a Z-Score?
A Z-score is a numerical measurement used in statistics of a value's relationship to the mean (average) of a group of values, measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score. A Z-score of 1.0 would indicate a value that is one standard deviation from the mean. Z-scores may be positive or negative, with a positive value indicating the score is above the mean and a negative score indicating it is below the mean.

Formual


### Standardized score


### Population Correlation Coefficient


### Confidence Interval


### Population Variance


### P Value


### Proportion


### Sample Mean


### Sample Standard Deviation


### Variance of sample proportion
