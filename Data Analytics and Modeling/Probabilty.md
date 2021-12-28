## Probability Notes

### Terms and properties

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



