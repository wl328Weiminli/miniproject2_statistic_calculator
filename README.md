# miniproject2_statistic_calculator

[![Build Status](https://travis-ci.com/wl328Weiminli/miniproject2_statistic_calculator.svg?branch=master)](https://travis-ci.com/wl328Weiminli/miniproject2_statistic_calculator)

## Team members
 * Weimin Li UCID: wl328
 * Jiaxin Du UCID: jd688
 
## Change Log

- [x] add basic Calculators and run the test _--Weimin Li_
- [x] add Population Mean and run the test _--Weimin Li_
- [x] add Median and run the test _--Weimin Li_
- [x] add Mode and run the test _--Weimin Li_
- [x] add Population Standard Deviation and run the test _--Weimin Li_
- [x] add Variance of population proportion and run the test _--Weimin Li_
- [x] add Z-Score and run the test _--Weimin Li_
- [x] add Population Correlation Coefficient and run the test _--Weimin Li_
- [x] add Confidence Interval and run the test _--Weimin Li_
- [x] add Population Variance and run the test _--Weimin Li_
- [x] add and pass the travis-ci _--jiaxin Du_
- [x] build the sampe function to generate the sample _--jiaxin Du_
- [x] add P Value and run the test _--jiaxin Du_
- [x] add Proportion and run the test _--jiaxin Du_
- [x] add Sample Mean and run the test _--jiaxin Du_
- [x] add Sample Standard Deviation and run the test _--jiaxin Du_
- [x] add Variance of sample proportion and run the test _--jiaxin Du_

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

#### Definition
This article is about the statistical concept. For other uses, see Median (disambiguation).

Finding the median in sets of data with an odd and even number of values
The median is the value separating the higher half from the lower half of a data sample (a population or a probability distribution). For a data set, it may be thought of as the "middle" value. For example, in the data set {1, 3, 3, 6, 7, 8, 9}, the median is 6, the fourth largest, and also the fourth smallest, number in the sample. For a continuous probability distribution, the median is the value such that a number is equally likely to fall above or below it.

The median is a commonly used measure of the properties of a data set in statistics and probability theory. The basic advantage of the median in describing data compared to the mean (often simply described as the "average") is that it is not skewed so much by a small proportion of extremely large or small values, and so it may give a better idea of a "typical" value. For example, in understanding statistics like household income or assets, which vary greatly, the mean may be skewed by a small number of extremely high or low values. Median income, for example, may be a better way to suggest what a "typical" income is.

#### How to use it in my statistic
    population_mean()
in the (), you should input a list like [1, 2, 3, 4, 5]


### Mode

#### Definition
The mode of a sample is the element that occurs most often in the collection. For example, the mode of the sample [1, 3, 6, 6, 6, 6, 7, 7, 12, 12, 17] is 6. Given the list of data [1, 1, 2, 4, 4] the mode is not unique – the dataset may be said to be bimodal, while a set with more than two modes may be described as multimodal.

For a sample from a continuous distribution, such as [0.935..., 1.211..., 2.430..., 3.668..., 3.874...], the concept is unusable in its raw form, since no two values will be exactly the same, so each value will occur precisely once. In order to estimate the mode of the underlying distribution, the usual practice is to discretize the data by assigning frequency values to intervals of equal distance, as for making a histogram, effectively replacing the values by the midpoints of the intervals they are assigned to. The mode is then the value where the histogram reaches its peak. For small or middle-sized samples the outcome of this procedure is sensitive to the choice of interval width if chosen too narrow or too wide; typically one should have a sizable fraction of the data concentrated in a relatively small number of intervals (5 to 10), while the fraction of the data falling outside these intervals is also sizable. An alternate approach is kernel density estimation, which essentially blurs point samples to produce a continuous estimate of the probability density function which can provide an estimate of the mode.

#### How to use it in our project
    mode()
in the (), you should input a list like [1, 2, 3, 4, 5, 1, 1, 4, 8]

### Population Standard Deviation

#### Definition
In statistics, the standard deviation (SD, also represented by the lower case Greek letter sigma σ for the population standard deviation or the Latin letter s for the sample standard deviation) is a measure of the amount of variation or dispersion of a set of values.[1] A low standard deviation indicates that the values tend to be close to the mean (also called the expected value) of the set, while a high standard deviation indicates that the values are spread out over a wider range.

The standard deviation of a random variable, statistical population, data set, or probability distribution is the square root of its variance. It is algebraically simpler, though in practice less robust, than the average absolute deviation.[2][3] A useful property of the standard deviation is that, unlike the variance, it is expressed in the same units as the data.

In addition to expressing the variability of a population, the standard deviation is commonly used to measure confidence in statistical conclusions. For example, the margin of error in polling data is determined by calculating the expected standard deviation in the results if the same poll were to be conducted multiple times. This derivation of a standard deviation is often called the "standard error" of the estimate or "standard error of the mean" when referring to a mean. It is computed as the standard deviation of all the means that would be computed from that population if an infinite number of samples were drawn and a mean for each sample were computed.

#### Formula
![images](/images/a.PNG)

#### How to use it in our project
    population_standard_deviation()
in the (), you should input a list like [1, 2, 3, 4, 5, 1, 1, 4, 8]

### Population Variance

#### Definition
In the statistical description, the variance is used to calculate the difference between each variable (observation) and the population mean. In order to avoid the sum of the mean deviations being zero, the square of the mean difference and the content of the sample, the statistics use the sum of squared mean deviations to describe the degree of variation of the variables. The formula for calculating the variance of the population:
![images](/images/b.PNG)

#### How to use it in our project
    population_variance()
in the (), you should input a list like [1, 2, 3, 4, 5, 1, 1, 4, 8]

### Proportion

#### Definition
A proportion refers to the fraction of the total that possesses a certain attribute.

For example, suppose we have a sample of four pets - a bird, a fish, a dog, and a cat. We might ask what proportion has four legs. Only two pets (the dog and the cat) have four legs. Therefore, the proportion of pets with four legs is 2/4 or 0.50.

#### How to use it in our project
    proportion()
in the (), you should input a list like [1, 2, 3, 4, 5, 1, 1, 4, 8]
each number in the list will get a proportion. You will get a list of the each number's proportion.


### Variance of population proportion
#### Definition
It shows the distribution of the data in the proportion way. So we change each number in the data to the proportion and use the variance method to calculator it.
#### How to use it in our project
     variance_of_population_proportion(num)
in the (), you should input a list like [1, 2, 3, 4, 5, 1, 1, 4, 8]

### Z-Score

#### What Is a Z-Score?
A Z-score is a numerical measurement used in statistics of a value's relationship to the mean (average) of a group of values, measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score. A Z-score of 1.0 would indicate a value that is one standard deviation from the mean. Z-scores may be positive or negative, with a positive value indicating the score is above the mean and a negative score indicating it is below the mean.

#### Formula
![images](/images/c.PNG)

#### How to use it in our project
    z_score()
in the (), you should input a list like [1, 2, 3, 4, 5, 1, 1, 4, 8]
each number in the list will get a z_score. You will get a list of the each number's z score


### Standardized score
It is same with z score

#### Population Correlation Coefficient
Correlation coefficients measure the strength of association between two variables. The most common correlation coefficient, called the Pearson product-moment correlation coefficient, measures the strength of the linear association between variables measured on an interval or ratio scale.

Formula:
Population correlation coefficient. The correlation ρ between two variables is:

ρ = [ 1 / N ] * Σ { [ (Xi - μX) / σx ]
* [ (Yi - μY) / σy ] }

where N is the number of observations in the population, Σ is the summation symbol, Xi is the X value for observation i, μX is the population mean for variable X, Yi is the Y value for observation i, μY is the population mean for variable Y, σx is the population standard deviation of X, and σy is the population standard deviation of Y.

#### How to use it in our project
    population_correlation_coefficient(num, num1)
num and num1 represent two list. For example [1, 2, 3, 4, 5, 1, 1, 4, 8] and [1, 2, 3, 4, 5, 1, 1, 4, 8]


### Confidence Interval
In statistics, a confidence interval (CI) is a type of interval estimate, computed from the statistics of the observed data, that might contain the true value of an unknown population parameter. The interval has an associated confidence level, or coverage that, loosely speaking, quantifies the level of confidence that the deterministic parameter is captured by the interval. More strictly speaking, the confidence level represents the frequency (i.e. the proportion) of possible confidence intervals that contain the true value of the unknown population parameter. In other words, if confidence intervals are constructed using a given confidence level from an infinite number of independent sample statistics, the proportion of those intervals that contain the true value of the parameter will be equal to the confidence level.

Confidence intervals consist of a range of potential values of the unknown population parameter. However, the interval computed from a particular sample does not necessarily include the true value of the parameter. Based on the (usually taken) assumption that observed data are random samples from a true population, the confidence interval obtained from the data is also random.

The confidence level is designated prior to examining the data. Most commonly, the 95% confidence level is used.[4] However, other confidence levels can be used, for example, 90% and 99%.

Factors affecting the width of the confidence interval include the size of the sample, the confidence level, and the variability in the sample. A larger sample will tend to produce a better estimate of the population parameter, when all other factors are equal. A higher confidence level will tend to produce a broader confidence interval.

For a known standard deviation: 
![images](/images/d.PNG)

#### How to use it in our project
    confidence_interval()
in the (), you should input a list like [1, 2, 3, 4, 5, 1, 1, 4, 8]
and you will get a list contain the interval.


### P Value

**P** is a statistical measure that helps researchers to determine whether their hypothesis is correct. It helps determine the significance of results. The null hypothesis is a default position that there is no relationship between two measured phenomena. It is denoted by H0. An alternative hypothesis is the one you would believe if the null hypothesis is concluded to be untrue. 

P value is a number between 0 and 1. There are tables, spreadsheet programs and statistical software to help calculate the p-value. Level of significance (α) is a pre-defined threshold set by the researcher. It is generally 0.05. A very small p-value, which is lesser than the level of significance indicates that you reject the null hypothesis. P value which is greater than the level of significance indicates that we fail to reject the null hypothesis.

![images](/images/p.PNG)

The overhat_p is Sample Proportion. p0 is Assumed Population Proportion in the Null Hypothesis. n is the Sample Size

### Sample Mean
Random sampling of samples from a set of data, use the sample data calculate the mean.In our project, we have the ability to generate more than 30 sample modules (more than 30 are statistically significant samples, so start from 30) From this, calculate the sample mean.
#### How to use it in our project
    sample_mean()
in the (), you should input a list, the number of the list should more than 30.

### Sample Standard Deviation
Random sampling of samples from a set of data, use the sample data calculate the Standard Deviation.In our project, we have the ability to generate more than 30 sample modules (more than 30 are statistically significant samples, so start from 30) From this, calculate the Standard Deviation.

#### How to use it in our project
    Sample_Standard_Deviation()
in the (), you should input a list, the number of the list should more than 30.

### Variance of sample proportion
#### Definition
Random sampling of samples from a set of data, use the sample data calculate theVariance of sample proportion.In our project, we have the ability to generate more than 30 sample modules (more than 30 are statistically significant samples, so start from 30). And we have the module to change each data to proportion. From this, calculate the Variance of sample proportion.

#### How to use it in our project
    variance_of_population_proportion()
in the (), you should input a list, the number of the list should more than 30.

Please see https://github.com/dujiaxin/miniprogect1-601-djx/blob/master/miniproject2Term.md for additional terms.
