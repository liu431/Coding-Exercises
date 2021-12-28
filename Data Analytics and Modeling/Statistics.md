## Statistical Inference

### Standard error; Standard deviation


[Standard error](https://www.investopedia.com/terms/s/standard-error.asp) measures how accurate is a sample represents a population.

[Standard Error](https://www.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/a/calculating-standard-deviation-step-by-step) is used to measure the statistical accuracy of an estimate. 

[Difference](https://keydifferences.com/difference-between-standard-deviation-and-standard-error.html)

### p value

When testing an hypothesis, the p-value is the likelihood that we would observe results at least as extreme as our result due purely to random chance if the null hypothesis were true.

  * A small p-value (typically ≤ 0.05) indicates strong evidence against the null hypothesis, so we say that the result is "statistically significant" and reject the null hypothesis.
  
  (relatively rare for the our results to be purely from random variations in observations.)

  * A large p-value (> 0.05) indicates weak evidence against the null hypothesis, so we fail to reject the null hypothesis.

  * p-values very close to the cutoff (0.05) are considered to be marginal (could go either way). Always report the p-value so our readers can draw their own conclusions.
  [Link](https://www.dummies.com/education/math/statistics/what-a-p-value-tells-you-about-statistical-data/)

### Statistical Tests 
* z-score
* t-test
* Chi-square test
* ANOVA
[Statistical Tests — When to use Which](https://towardsdatascience.com/statistical-tests-when-to-use-which-704557554740)

[Interactive Visualization of Statistical Power and Significance Testing](https://rpsychologist.com/d3/nhst/)

### Confidence Interval

95% confidence interval: a range of values that you can be 95% certain contains the population mean

[Using Confidence Intervals to Compare Means](https://statisticsbyjim.com/hypothesis-testing/confidence-intervals-compare-means/)


### Effect size

Cohen's d is an effect size used to indicate the standardised difference between two means. 

Cohen's d can be calculated as the difference between the means divided by the pooled SD:
 <img src="https://render.githubusercontent.com/render/math?math=\frac{Mean Difference}{Standard Deviation}">

[Cohen's d](https://en.wikiversity.org/wiki/Cohen%27s_d)

[Computation of Effect Sizes] (https://www.psychometrica.de/effect_size.html)

Ex. The effect size was d=0.1, n1 is the number of units in treatment group, n2 is the number of units in control group

```{r}
library(psych)
cohen.d.ci(d = .1, n1 = 100, n2 = 100)
````

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

## Statistics

### Linear Regression

4 Assumptions

Remove multicolinearity

[Beyond OLS](https://stats.idre.ucla.edu/stata/webbooks/reg/chapter4/regressionwith-statachapter-4-beyond-ols-2/)

### Logistic Regression

Maxmimum Likelihood Estimation

### Generalized Linear Models

[UChicago_STAT34700_Winter 2020](https://www.jingshuw.org/stat347.html)

### Discrete Choice Modeling

### AB Test and Experiments

Power

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
