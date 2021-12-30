## Statistical Inference

### Statistic
* [Standard error](https://www.investopedia.com/terms/s/standard-error.asp): measures how accurate is a sample represents a population.
* [Standard deviation](https://www.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/a/calculating-standard-deviation-step-by-step): measure the statistical accuracy of an estimate. 

[Difference](https://keydifferences.com/difference-between-standard-deviation-and-standard-error.html)



#### [Degrees of freedom](https://www.scribbr.com/statistics/t-test/)
Related to your sample size, and shows how many 'free' data points are available in your test for making comparisons. The greater the degrees of freedom, the better your statistical test will work





### Hypothesis Testing
#### [Hypothesis](https://www.scribbr.com/statistics/hypothesis-testing/)
Null hypothesis: a prediction of no relationship between the variables you are interested in
Alternate hypothesis: there is a relationship between variables

#### p value

When testing an hypothesis, the p-value is the likelihood that we would observe results at least as extreme as our result due purely to random chance if the null hypothesis were true.

  - A small p-value (typically ≤ 0.05) indicates strong evidence against the null hypothesis, so we say that the result is "statistically significant" and reject the null hypothesis. In other words, it is unlikely that the differences between these groups came about by chance.

  - A large p-value (> 0.05) indicates weak evidence against the null hypothesis, so we fail to reject the null hypothesis. In other words, any difference you measure between groups is due to chance.

  - p-values very close to the cutoff (0.05) are considered to be marginal (could go either way). Always report the p-value so our readers can draw their own conclusions.
  [Link](https://www.dummies.com/education/math/statistics/what-a-p-value-tells-you-about-statistical-data/)

#### Confidence Interval

95% confidence interval: a range of values that you can be 95% certain contains the population mean; range of numbers within which the true difference in means will be 95% of the time

[Using Confidence Intervals to Compare Means](https://statisticsbyjim.com/hypothesis-testing/confidence-intervals-compare-means/)

#### [Errors](https://machinelearningmastery.com/statistical-power-and-power-analysis-in-python/)
Type I Error: reject the null hypothesis when there is in fact no significant effect (false positive). The p-value is optimistically small.
Type II Error: not reject the null hypothesis when there is a significant effect (false negative). The p-value is pessimistically large.


#### Significance level 
- Boundary for specifying a statistically significant finding when interpreting the p-value, such as 0.05
- Probability of rejecting the null hypothesis if it were true (false positive / Type 1 Error)

#### [Statistical Power](https://machinelearningmastery.com/statistical-power-and-power-analysis-in-python/)
- Probability that the test correctly rejects the null hypothesis (true positive); COmmon: 0.8
  - Power = 1 - Type II Error
  - Pr(True Positive) = 1 - Pr(False Negative)
  - Low Statistical Power: Large risk of committing Type II errors, e.g. a false negative.
  - High Statistical Power: Small risk of committing Type II errors. 
- It is only useful when the null hypothesis is rejected.
- Can be used to estimate the minimum sample size required for an experiment, given a desired significance level, effect size, and statistical power

#### [Effect size]((https://machinelearningmastery.com/statistical-power-and-power-analysis-in-python/))
- The quantified magnitude of a result present in the population. 
- Calculated using a specific statistical measure, such as Pearson’s correlation coefficient for the relationship between variables or Cohen’s d for the difference between groups

##### [Cohen's d](https://en.wikiversity.org/wiki/Cohen%27s_d)
- An effect size used to indicate the standardised difference between two means. 
- Calculated as the difference between the means divided by the pooled SD:
 <img src="https://render.githubusercontent.com/render/math?math=\frac{Mean Difference}{Standard Deviation}">
- [Computation of Effect Sizes] (https://www.psychometrica.de/effect_size.html)
- Ex. The effect size was d=0.1, n1 is the number of units in treatment group, n2 is the number of units in control group


#### Tests
[Statistical Tests — When to use Which](https://towardsdatascience.com/statistical-tests-when-to-use-which-704557554740)

[Interactive Visualization of Statistical Power and Significance Testing](https://rpsychologist.com/d3/nhst/)

[Overview of statistical tests](https://www.r-bloggers.com/2019/03/overview-of-statistical-tests/)

![](http://philipppro.github.io/images/Overview_statistical_tests.png)

[Equations of statistical tests](https://www.pinterest.com/pin/3799980919780691/)

![](https://i.pinimg.com/originals/50/d9/b3/50d9b31222262b570f91b4967aa2374b.png)



### Mediation Analysis

[Various package options for conducting mediation analysis](https://m-clark.github.io/posts/2019-03-12-mediation-models/)


### Posterior distributions

Confidence and credible intervals

Likelihood ratio tests

Multinomial distributions

Chi-square tests

Diagnostic plots

Bootstrapping

Comparison of Bayesian and frequentist inference

Conditioning 


### Jensen's Inequality

[Note on Brillant](https://brilliant.org/wiki/jensens-inequality/)

Chebyshev's inequality

[Note on Brilliant](https://brilliant.org/wiki/chebyshev-inequality/)'

The exponential family

Generalized linear modeling

Study design/power analyses


Nonparametric statistical testing

Expected values and variance of a random variable

Likelihood ratios

Time series and longitudinal regression methods

Stochastic processes

Measurement models (SEMs, factor analysis…)

## Regressions

### Linear Regression
Model the relationship between a single dependent variable Y and one or more predictors
* [4 Assumptions](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/R/R5_Correlation-Regression/R5_Correlation-Regression4.html)
  - Linearity: the relationship between X and the mean of Y is linear.
  - Homoscedasticity: the variance of residual is the same for any value of X.
  - Independence: observations are independent of each other.
  - Normality: for any fixed value of X, Y is normally distributed.

* Multicolinearity
  - Multicollinearity: condition when there is a significant dependency or association between the independent variables or the predictor variables
  - Issue: overestimate the coefficients and interpretations can be misleading 
  - Detect: Variance Inflation Factor (VIF) (threshold: 5) corresponding to every independent variable in the data.

[Beyond OLS](https://stats.idre.ucla.edu/stata/webbooks/reg/chapter4/regressionwith-statachapter-4-beyond-ols-2/)

### Logistic Regression

[Maxmimum Likelihood Estimation](https://towardsdatascience.com/probability-concepts-explained-maximum-likelihood-estimation-c7b4342fdbb1)
  - Determines values for the parameters of a model that maximise the likelihood that the process described by the model produced the data that were actually observed

### Generalized Linear Models

[UChicago_STAT34700_Winter 2020](https://www.jingshuw.org/stat347.html)

### Discrete Choice Modeling

### AB Test and Experiments


Sample Size

Metrics

Time 

Ex. Evaluate and prototype Bayesian alternatives to measuring statistical significance of A/B tests

#### Online resources

[A/B Testing, A Data Science Perspective](https://www.oreilly.com/library/view/ab-testing-a/9781491934777/)

## Simulation

## Bayesian Statistics

Monte-Carlo Simulation

[Brilliant](https://brilliant.org/wiki/monte-carlo/)

MCMC

Bayes's Formula

Hierarchical Bayesian models

## Econometrics & Casual Inference

Potential Outcome Framework

Simpson's paradox: [Quora answer](https://www.quora.com/What-is-Simpsons-paradox)

Instrument Variables

Difference in Differnce

Regression Discontinuity

Propensity Score Matching

Mediation

Moderation

Spillover Effects	

### Readings:

[Causal Inference in A Nutshell](https://econometricsense.blogspot.com/2012/12/causal-inference-in-nutshell.html)

[Introducing CausalNex](https://medium.com/@QuantumBlack/introducing-causalnex-driving-models-which-respect-cause-and-effect-a561545f0a5e)

[Quasi-experimental tools in the age of A/B tests](https://medium.com/@pabloalejandrocrespo/a-regression-discontinuity-love-story-quasi-experimental-tools-in-the-age-of-a-b-tests-8a8c172fb42c)

[Identifying Cause & Effect With Causal Reasoning](https://medium.com/@QuantumBlack/identifying-cause-effect-with-causal-reasoning-5ee4a6efc828)

[Causal Inference using Difference in Differences, Causal Impact, and Synthetic Control](https://towardsdatascience.com/causal-inference-using-difference-in-differences-causal-impact-and-synthetic-control-f8639c408268)

## Non-parametric Methods

Kernel density estimators

Linear interpolation

Cubic splines

Histograms

Confidence sets

Orthogonal functions

Random processes

## Numerical Methods

High performance computing/parallel programming (MPI and OpenMP)

Matrix decompositions (SVN, QN-LQ, Choleski, eigenvector-eigenvalue)

Orthogonal polynomials

Numerical derivatives

Nnumerical integration

Equidistributed sequences for quasi-Monte Carlo simulation

Measure theory

## Optimization algorithms

Linear programming

Simplex, Newton and quasi-Newton methods

Conjugate gradient methods

Duality theory

Optimality conditions

Intractability results

Unconstrained and constrained optimization

## Psychometrics

Item response theory (IRT)

Factor analysis

## Time Series

## Multilevel Modeling

Multilevel regression with poststratification

## Survival Analysis

* Contingency table analysis

* Kaplan-Meier survival analysis

* Cox proportional-hazards survival analysis

## Spatial Data Analysis

## Survey Research

## Longitudinal Data Analysis

### Multiple Testing


<details>
<summary> 
  
</summary>
<br>
  
<br>
</details>
