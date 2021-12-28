## Notes

### Probability

A, B, and C are distinct events; 

X is a random variable that can take different values (Ex. X=1 if an individual is a female and 0 if a male)

P(X=1): probability that an individual randomly drawn from a population is female, which corresponds to the proportion of the population that are female

0 ≤ P(A) ≤ 1

P(A) + P(Ā) = 1, where Ā denotes all other events that are not A

<img src="https://render.githubusercontent.com/render/math?math=P(A, B) = P(A) * P(B \mid A)">;  <img src="https://render.githubusercontent.com/render/math?math=P(B|A) = \frac{P(A,B)}{P(A)}">


P(A, B) = 0 if A and B are mutually exclusive; B = Ā

Chain rule: <img src="https://render.githubusercontent.com/render/math?math=P(A, B, C) = P(A) * P(B \mid A) * P(C \mid B,A)">

* Joint probability: probability of two events occurring simultaneously.
* Marginal probability: probability of an event irrespective of the outcome of another variable.
* Conditional probability: probability of one event occurring in the presence of a second event. 


#### Statistical independence

If A and B are statistically independent events, then <img src="https://render.githubusercontent.com/render/math?math=P(B \mid A) = P(B)"> and <img src="https://render.githubusercontent.com/render/math?math=P(A,B) = P(A) * P(B)">

If x and y are independent, then f(x,y) = f(x)f(y)

#### Bayes’ Theorem

 <img src="https://render.githubusercontent.com/render/math?math=P(B|A)=\frac{P(A|B) * P(B)}{P(A)}">

* Bayes’ Theorem for continuous random variables X and Y

 <img src="https://render.githubusercontent.com/render/math?math=f(y|x) = \frac{f(x,y)}{f(x)} = \frac{f(x|y)f(y)}{f(x)}">
 
#### Probability density for continuous random variables

For a discrete random variable Y, P(Y = y) is the probability that Y takes value y, and <img src="https://render.githubusercontent.com/render/math?math=1=\sum_{k}^{} P(Y=y)">.

For a continuous random variable Y, 𝑓(𝑦) is the probability density of y, and <img src="https://render.githubusercontent.com/render/math?math=1=\int_{y}^{} f(y)dy=1">.



#### Expectation

a and b are constants; X, Y, and Z are random variables

If X is a discrete random variable, <img src="https://render.githubusercontent.com/render/math?math=E(X) = \sum_{x}^{} xP(X=x)">.

When X is a binary indicator (0 and 1), E(X) = P(X = 1)

* E(a) = a
* E(a+X) = a + E(X)
* E(aX) = aE(X)
* E(X+Y) = E(X) + E(Y)
* E(aX+bY) = aE(X) + bE(Y)

 <img src="https://render.githubusercontent.com/render/math?math=E(\sum_{i=1}^{k} a_{i} X_{i}) = \sum_{i=1}^{k} a_{i} E(X_{i})">

If X and Y are statistically independent, then E(XY) = E(X)E(Y)

#### Conditional expectation

If Y is a discrete random variable, then <img src="https://render.githubusercontent.com/render/math?math=E(Y \mid X=x) = \sum_{y}^{} yP(Y=y) \mid X=x">

If Y is a continuous random variable, then <img src="https://render.githubusercontent.com/render/math?math=E(Y \mid X=x) = \int_{y}^{} yf(y \mid x)dy">

#### Marginal expectation

If Y is a discrete random variable, then
 <img src="https://render.githubusercontent.com/render/math?math=E(Y \mid X=x) = \sum_{x}^{} E(Y \mid X=x)P(X=x) = \sum_{x}^{}\sum_{y}^{} yP(Y=y \mid X=x)P(X=x)">

If Y is a discrete random variable, then
 <img src="https://render.githubusercontent.com/render/math?math=E(Y) = \int_{}^{} \int_{}^{} yf(y \mid x)f(x)dydx">

#### Variance and Covariance

1. <img src="https://render.githubusercontent.com/render/math?math=Var(X) = E{[X-E(X)]^{2}} = E(X^{2})-[E(X)]^{2}">

2. <img src="https://render.githubusercontent.com/render/math?math=Var(a) = 0">

3. <img src="https://render.githubusercontent.com/render/math?math=Var(a+X) = Var(X)">

4. <img src="https://render.githubusercontent.com/render/math?math=Var(aX) = a^{2}Var(X)">

5. If X and Y are statistically independent, then <img src="https://render.githubusercontent.com/render/math?math=Var(X+Y) = Var(X)+Var(Y)">

Otherwise, <img src="https://render.githubusercontent.com/render/math?math=Var(X+Y) = Var(X)+Var(Y)+2Cov(X,Y)">

6. <img src="https://render.githubusercontent.com/render/math?math=Cov(X,Y) = E{[X-E(X)][Y-E(Y)]} = E(XY)-E(X)E(Y)">

7. <img src="https://render.githubusercontent.com/render/math?math=Cov(a,X) = 0">

8. <img src="https://render.githubusercontent.com/render/math?math=Cov(aX,Y) = aCov(X,Y)">

9. <img src="https://render.githubusercontent.com/render/math?math=Cov(aX, bY) = abCov(X,Y)">

10. <img src="https://render.githubusercontent.com/render/math?math=Cov(a+bX,Y) = Cov(a,Y)+Cov(bX,Y)=bCov(X,Y)">

11. <img src="https://render.githubusercontent.com/render/math?math=Cov(X+Y,Z) = Cov(X,Z)+Cov(Y,Z)">

#### Central Limit Theorem (CLT)
The distribution of the sampling distribution tends toward a normal disyrbution when n is large

#### Law of Large Number
As the number of identically distributed, randomly generated variables/trials increases, the sample mean (average) approaches their theoretical mean (expected mean).

#### Distributions
[Discrete Probability Distributions](https://www.dummies.com/article/academics-the-arts/math/statistics/discrete-probability-distributions-188347)

![](https://www.dummies.com/wp-content/uploads/250474.image0.jpg)

[Continuous probability distributions](https://www.dummies.com/article/academics-the-arts/math/statistics/probability-for-dummies-cheat-sheet-208653)

![](https://www.dummies.com/wp-content/uploads/250463.image0.jpg)

[Distribution charts](https://www.adrian.idv.hk/2018-03-19-distribution/)

![](https://www.adrian.idv.hk/img/distribution.png)

#### Stochastic probability
Discrete time Markov chain

Poisson process

Continuous time Markov process

Renewal process

Brownian motion

Conditional probability and independence

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

### Law of Large Number

Wiki def: the average of the results obtained from a large number of trials should be close to the expected value, and will tend to become closer to the expected value as more trials are performed. 

### Central Limit Theorem

Def: probability distribution of the average of independent random variables will converge to a normal distribution, as the number of observations increases

[Brilliant](https://brilliant.org/wiki/central-limit-theorem/)

[Medium](https://medium.com/@saisourabh12/law-of-large-numbers-and-central-limit-theorem-the-two-pillars-of-statistics-3b311816d172)

### Jensen's Inequality

[Note on Brillant](https://brilliant.org/wiki/jensens-inequality/)

Chebyshev's inequality

[Note on Brilliant](https://brilliant.org/wiki/chebyshev-inequality/)'

The exponential family

Generalized linear modeling

Study design/power analyses

Basic statistical tests (z-score, t-test, Chi-square test, ANOVA…)

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

