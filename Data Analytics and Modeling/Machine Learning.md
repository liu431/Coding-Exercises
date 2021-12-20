# Notes on Machine Learning

## Concepts

### Statistical Learning vs Machine Learning

 Different goals: 
 
 Statistical Learning: inference and generalization
 
 Machine Learning: maxmize prediction 
 
 > Machine learning is the science of getting computers to act without being explicitly programmed. - Andrew Ng
 
 > Field of study that gives computers the ability to learn without being explicitly programmed. -Arthur Samuel, IBM, 1959
 
### Model

Common form: <img src="https://render.githubusercontent.com/render/math?math=y=f(x)">+<img src="https://render.githubusercontent.com/render/math?math=\epsilon">; Interested in estimating functional form of f(x)
  
Approaches: 
* Parametric
* Non-parametric estimation
 
### Selecting and fitting a model

### Flexible models vs. inflexible models 
 
  `Flexibility` is a measure of how much a fitted model can vary with a given data.
  
  * Example of flexible models (high variance, low bias): splines, 10 degree curve, Support Vector Machines
  
  * Example of inflexible models (low variance, high bias): linear regression

 * When a inflexible model is preferred:
 
   1. interpretablility: understand how the explanatory variables affect the response variable
      
   2. a small e size (small n) and large number of predictors (large p)
   
   3. the variance of the error terms, i.e. <img src="https://render.githubusercontent.com/render/math?math=sigma^{2}=Var(\epsilon)">, is extremely high
 
 * When a flexible model is preferred:
   
   1. a large sample size (large n) and small number of predictors (small p)
   
   2. relationship between the predictors and response is highly non-linear
   
A flexible model will cause you to fit too much of the noise in the problem (when variance of the error terms is high).

[Quora answer](https://www.quora.com/What-are-flexible-statistical-learning-methods)

### Error

Error = Irreducible Error + <img src="https://render.githubusercontent.com/render/math?math=Bias^2"> + Variance

### Error/ Bias / Variance

#### Bias

Error caused by choosing an algorithm that cannot accurately model the signal in the data, i.e. the model is too general or was incorrectly selected. For example, selecting a simple linear regression to model highly non-linear data would result in error due to bias.

#### Variance

Error from an estimator being too specific and learning relationships that are specific to the training set but do not generalize to new samples well. Variance can come from fitting too closely to noise in the data, and models with high variance are extremely sensitive to changing inputs. Example: Creating a decision tree that splits the training set until every leaf node only contains 1 sample.

#### Irreducible error 

error caused by noise in the data that cannot be removed through modeling. Example: inaccuracy in data collection causes irreducible error.

[Kyle McKiou Blog](https://www.linkedin.com/posts/kylemckiou_datascience-dsdj-qanda-activity-6619603364747575296-w0Ka)

[Tradeoff Infographics](https://elitedatascience.com/bias-variance-tradeoff)


#### Bias-variance tradeoff

trade-off between underfitting and overfitting

From simple to complex models, flexibility increases, variance increases, bias decreases.

As you decrease variance, you tend to increase bias. As you decrease bias, you tend to increase variance.

<img src="/images/ML/Biasvariance.png" class="img-responsive" alt=""> 

Metrics for evaluating models

"No Free Lunch Theorem"

### TPR/FPR/TNR/FNR

Optimization Methods

1. Netwon's method

2. Quasi-Newton methods (ex. LBFGS)

3. Gradient Descent

### Overfitting

When a model makes much better predictions on known data (data included in the training set) than unknown data (data not included in the training set); High variance, low bias; Flexible model

Combate overfitting:

* simplify the model by use fewer parameters
* simply the model by changing the hyperparameters
* simplify the model by introducing regularization
* select a different model
* use more training data
* gather better quality data

[Kyle McKiou Blog](https://www.linkedin.com/posts/kylemckiou_datascience-dsdj-machinelearning-activity-6613065673839120386-vAYB)


Hyper-parameter tuning 

### Resampling Methods

* Essential to test and evaluate statistical models

* Repeatedly draw from your original sample to obtain additional information about the model

### Encoding categorical data

* Label encoding (non-ordinal) - each category is assigned a numeric value not representing any ordering. Example: [red, blue, green] could be encoded to [8, 5, 11].

* Label encoding (ordinal) - each category is assigned a numeric value representing an ordering. Example: [small, medium, large] could be encoded to [1, 2, 3]

* One-hot encoding - each category is transformed into a new binary feature, with all records being marked 1/True or 0/False. Example: color = [red, blue, green] could be encoded to color_red = [1, 0, 0], color_blue = [0, 1, 0], color_green = [0, 0, 1]

[Kyle McKiou Blog](https://www.linkedin.com/posts/kylemckiou_describe-basic-feature-encoding-for-categorical-activity-6621763235186118656-PKU7)

### Train and testing set

* training set is used for model construction (can be reused many times to build different models)

* test set is used to evaluate the performance of the final model (can be used only once)

### Validation

* Intuition: fit the model and evaluate it many times on the same data

* Method: split half of the training data as validation set

* Drawback: validation estimates of the test error rates can be highly variable depending on which observations are sampled into the training and validation sets (ex. outliers in the validation sets)

### Cross-validation

_for evaluating a model’s performance relative to other models_

1. LOOCV: leave-one-out cross validation

only remove one observation for the validation set, and keep all remaining observations in the training set

 <img src="https://render.githubusercontent.com/render/math?math= CV_N = {\frac{1}{N}}{\sum_{i=1}^{N}}MSE_i <img src="https://render.githubusercontent.com/render/math?math=

* Pro: unbiased compared to naive 1-stage validation approach

* Pro: highly flexible and works with any kind of predictive modeling

* Cro: high variance because the N "training sets" are so similar to one another; 

* Cro: computationally expensive

2. K-fold cross-validation: divides the observations into K folds of approximately equal size

Typical K= 5 or 10; Random sampling without replacement

 <img src="https://render.githubusercontent.com/render/math?math= CV_K = \frac{1}{K}\sum_{i=1}^{K}MSE_i <img src="https://render.githubusercontent.com/render/math?math=

* Pro: less variance in test error estimate compared with LOOCV

* Cro: leads to a slight increase in usually bias

3. Other validations

* Stratified cross-validation

* Repeated cross-validation 

* Cross-validation with time series data

### Bootstrapping

_non-parametric measure of the accuracy of a parameter estimate or method_

Purpose: quantify uncertainty associated with some estimator

Loss

1. MSE/Sum of squared errors

2. Cross-entropy

3. Kullback-Leibler (KL) divergence

4. Gini impurity for decision tree

5. Information gain

### Estimators of errors

adjusting the training error to penalize additional features

#### Mallows’s Cp

 <img src="https://render.githubusercontent.com/render/math?math=C_{p} = \frac{1}{n}(RSS+2d hat{\sigma}^2)">
[Wiki](https://en.wikipedia.org/wiki/Mallows%27s_Cp)

#### AIC

 <img src="https://render.githubusercontent.com/render/math?math=AIC= −2logL + 2 × d">

In the linear model, <img src="https://render.githubusercontent.com/render/math?math=−2LogL = \frac{RSS}{hat{\sigma}^2)}">

#### BIC

 <img src="https://render.githubusercontent.com/render/math?math=BIC = \frac{1}{n}(RSS+log(n) * hat{\sigma}^2)">

(imposes harsher penalty on models with more features, resulting in selection of less complex models)

#### Adjusted R^2

">Adjust R^2 = 1-\frac{RSS/(n-d-1)}{TSS/(n-1)}">

### 1SE Rule

The rule suggests to not necessarily choose the model with minimum error, but to choose the simplest model within one SE of the min error.

### Data Preparation

* Cleaning/Pre-processing

* Missing data
* Unbalanced data

[How to fix an Unbalanced Dataset@KDnuggets](https://www.kdnuggets.com/2019/05/fix-unbalanced-dataset.html)

[Resampling strategies for imbalanced datasets@Kaggle](https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets)

[Diving Deep with Imbalanced Data@Datacamp](https://www.datacamp.com/community/tutorials/diving-deep-imbalanced-data)

* Feature engineering

Purpose: improve the model performance by selecting and transforming the most relevant variables from raw data using domain knowledge

* Numeric Data transformation
 - scaling to a range:  converting floating-point feature values from their natural range into a standard range—usually 0 and 1
 - clipping: caps all feature values above (or below) a certain value to fixed value
 - log scaling: improve linear model performance when data has power law distribution (when a handful of your values have many points, while most other values have few points)
 - z-score: represents the number of standard deviations away from the mean; ensure your feature distributions have mean = 0 and std = 1

* Feature selection

* Effective sample size

* Time correaltions

 - backward

 - forward

  -subset

* L1

* L2

* PCA

### Ensemble learning

1. Bagging

2. Boosting 

3. Xgboost

* xgboost vs DT

* xgboost vs RF

* xgboost vs boosting

Estimation Methods

1. MLE / MAP

2. Expectation-Maxmization algorithm

Occam's Razor
  
  "the simplest solution is most likely the right one"
  
  "when presented with competing hypotheses that make the same predictions, one should select the solution with the fewest assumptions"
  
[Wikipedia](https://en.wikipedia.org/wiki/Occam%27s_razor)

### Building ML Model

<img src="/images/ML/ML.jfif" class="img-responsive" alt=""> 

### Model parameter v.s. Learning hyperparameter

* Model parameters are the rules that mathematically describe the final model that makes predictions, such as slopes or intercept in a linear regression model.

* Learning hyperparameter describes the way in which a model parameter is learned and settings for training the model, e.g. learning rate, penalty terms, number of features to include in a weak predictor, etc.

Model parameters: determined/fitted using the training data set

Hyperparameters: adjustable parameters to be tuned for optimal performance

### [Model hyperparameter tuning](https://machinelearningmastery.com/hyperparameter-optimization-with-random-search-and-grid-search/)
Goal: find the optimal hyperparameters of a model which results in the most ‘accurate’ predictions

* Random Search: randomly sample points in the search place.
* Grid Search: evaluate every position in the search place.

## Supervised Machine Learning

[scikit-learn linear models](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model)

[glmnet in R](https://web.stanford.edu/~hastie/glmnet/glmnet_alpha.html)

### Regression

#### Linear Model
 
Two assumptions: 1. Linear; 2. Additive (unit changes)
  
The coefficients in a least squares model typically are interpreted as the expected change in the outcome of interest associated with a unit change in the predictors, <img src="https://render.githubusercontent.com/render/math?math=Y = \beta_{0}+\beta_{1}X_{1}+...+\beta_{p}X_{p}+\epsilon">

* Unconditional marginal effects are the expected change in Y associated with a unit change in X (partial derivative), 
 <img src="https://render.githubusercontent.com/render/math?math=\frac{\partial Y}{\partial X_{1}} = \beta_{1}">

(constant values where we are directly observing the change in slope of Y, given X)

* Conditional marginal effects are the expected change in Y associated with a unit change in X (partial derivative), 
such as <img src="https://render.githubusercontent.com/render/math?math=\frac{\partial Y}{\partial X_{1}} = \beta_{1}+\beta_{2}X_{1}"> or <img src="https://render.githubusercontent.com/render/math?math=\frac{\partial Y}{\partial X_{1}} = \beta_{1}+2\beta_{2}X_{1}"> 

3 types of marginal effects:

* Marginal effects at representative values (MERs) - MFX at a particularly interesting combination of X values

* Marginal effects at means (MEMs) - MFX of each feature at the means of the others

* Average marginal effects (AMEs) - MFX at every observed value of X, averaged across the effect estimates

(a single quantity summary that reflects the full distribution of X as observed in the sample )

#### OLS (ordinary least squares)

Linear model selection

1. Linearity

2. Correlation vs Causality

3. Multicollinearity

4. Interaction variables (ex. x1*x2)

5. Normality

6. Homoscedasticity

7. Monotonic relationship

### [Shrinkage/Regularization](https://www.datacamp.com/community/tutorials/tutorial-ridge-lasso-elastic-net)

shrinkage employs a technique to constrain or regularize the coefficient estimates

can significantly reduce their variance, and ultimately the error in the model, resulting in stronger predictions


1. Ridge

estimates the coefficients that minimize <img src="https://render.githubusercontent.com/render/math?math=RSS + \lambda \sum_{j=1}^{p} {\beta_{j}}^2">

where <img src="https://render.githubusercontent.com/render/math?math=\lambda"> is a tuning parameter, which is the penalty we are imposing on the estimates

2. Lasso 

3. Elastic-net

Bayesian linear regression

Local regression

Generalized additive model

Logistic regression

#### K-Nearest regression 

kNN regression uses a moving average to generate the regression line

Given a value for <img src="https://render.githubusercontent.com/render/math?math=K"> and a prediction point <img src="https://render.githubusercontent.com/render/math?math=x_{0}">, kNN regression identifies the <img src="https://render.githubusercontent.com/render/math?math=K"> training observations nearest to the prediction point <img src="https://render.githubusercontent.com/render/math?math=x_{0}">, represented by <img src="https://render.githubusercontent.com/render/math?math=N_{0}">

Estimates <img src="https://render.githubusercontent.com/render/math?math=f(x_{0})"> as the average of all the training responses in <img src="https://render.githubusercontent.com/render/math?math=N_{0}">,
 <img src="https://render.githubusercontent.com/render/math?math=\hat{f(x_{0})} = \frac{1}{K}\sum_{x_{i}∈N_{0}}^{}y_{i}">

* When K is small, flexible, low bias but high variance

* When K is large, inflexible, low variance but higher bias

KNN erforms worse as the number of predictors p increases.

Application in marketing: likealike model

#### Non-Linear Estimation

* Polynomial regression: adding additional predictors obtained by raising each to a power

* Step function: split the range of a feature into k regions and fits a piecewise constant function

* Regression splines: polynomials + step functions that provide more flexibility; split the range of X into k distinct regions and within each region, fit a polynomial function

* Smoothing splines: smoothing splines result from minimizing an RSS criterion subject to a smoothness penalty

* Local regression: regions are allowed to overlap to allow for improved smoothness

* Generalized additive models: multiple predictors

#### Non-parametric regression

How: can divide X into many narrow intervals just like we would for a histogram and estimate the conditional distribution of Y and estimate the conditional mean of Y within each bin

Bottom line: Unless your dataset is extremely large or you have a small handful of variables with a low number of unique values, naive nonparametric estimation will not be effective


### Classification

Task: 

* Build a function C(X) that takes the feature vector X and predicts its value for Y , i.e. C(X) ∈ C

* Classify observations as a function of some vector of features

* Model the probability that Y belongs to a particular category instead of Y directly

 <img src="https://render.githubusercontent.com/render/math?math=f(X) = \frac{e^{\beta_{0}}+\beta_{1}*X}}{1 + e^{\beta_{0}}+\beta_{1}*X}}">

Threshold: f(X)>=0.5, <img src="https://render.githubusercontent.com/render/math?math=\hat{Y}=1">; f(X)<0.5, <img src="https://render.githubusercontent.com/render/math?math=\hat{Y}=1">

#### Imbalanced class distribution
[Article]https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/)
Issue: the distribution of examples across the known classes is biased or skewed. This results in models that have poor predictive performance, specifically for the minority class. 
Tactics:
1. Collect more data
2. Change [performance metrics](https://machinelearningmastery.com/classification-accuracy-is-not-enough-more-performance-measures-you-can-use/) from Accuracy to Confusion Matrix/Precision/Recall/F1 Score/ROC Curves
3. Resample data
4. Generate synthetic samples

#### Odds

Probability of one outcome divided by the probability of the other outcome <img src="https://render.githubusercontent.com/render/math?math=\frac{}{}">

#### [Key terms: Sensitivity_and_specificity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity)

<img src="/images/ML/CLassficationTerms.png" class="img-responsive" alt=""> 

[Data Science in Medicine](https://medium.com/@alon.lek/should-i-look-at-precision-recall-or-specificity-sensitivity-3946158aace1)

Purpose: categorize all the variables that form the output

Softmax classifier

K-nearest neighbors

Naïve bayes

Support vector machine

#### Evaluation metrics for classification

* Accuracy 

measures the percentage of the time you correctly classify samples: (true positive + true negative) / all samples

* Precision 

measures the percentage of the predicted members that were correctly classified: true positives / (true positives + false positives)

* Recall

measures the percentage of true members that were correctly classified by the algorithm: true positives / (true positives + false negative)

* F1

measurement that balances accuracy and precision (or you can think of it as balancing Type I and Type II error)

* AUC

Area Under The Curve---represents degree or measure of separability

describes the probability that a classifier will rank a randomly chosen positive instance higher than a randomly chosen negative one

[Blog](https://arogozhnikov.github.io/2015/10/05/roc-curve.html)

* ROC

Receiver Operating Characteristics---probability curve

[Blog](https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5)

* Gini

a scale and centered version of AUC

* Log-loss

similar to accuracy but increases the penalty for incorrect classifications that are "further" away from their true class. For log-loss, lower values are better.

Source: [Kyle McKiou Blog](https://www.linkedin.com/posts/kylemckiou_datascience-dsdj-qanda-activity-6622850903802290179-jJeS)
  

#### K-Nearest classification 

Similar to kNN regression, given a positive integer K and a test observation x0, the kNN classifier identifies the K nearest training observations to x0, represented by N0.

The conditional probability for class j is the fraction of points in <img src="https://render.githubusercontent.com/render/math?math=N_{0}"> whose response values equal j,
 <img src="https://render.githubusercontent.com/render/math?math=Pr(Y = j|X = x_{0}) = \frac{1}{K}\sum_{x_{i}∈N_{0}}^{} I(y_{i}=j)">

where I is an indicator variable that equals 0 for correct classification and equals 1 for incorrect classification

#### Bayes decision boundary

For classification problems, the test error rate is minimized by a simple classifier that assigns each observation to the most likely class given its predictor values, <img src="https://render.githubusercontent.com/render/math?math=Pr(Y = j|X = x_{0})"> where <img src="https://render.githubusercontent.com/render/math?math=x_{0}"> is the test observation and each possible class is represented
by J

(conditional probability that Y = j, given the observed predictor vector <img src="https://render.githubusercontent.com/render/math?math=x_{0}">)

The Bayes classifer produces the lowest possible test error rate, called the Bayes error rule, because it will always assign observations based on the maximum conditional probability,
 <img src="https://render.githubusercontent.com/render/math?math=1 − E(\underset{j}{\operatorname{max}} Pr(Y = j|X))"> where the expectation averages the probability over all possible values of X

#### Naive Bayes

Bayes Theorem: By combining our observed information, we update the prior information on probabilities to compute a posterior probability that an observation belongs to class Ck, <img src="https://render.githubusercontent.com/render/math?math=Posterior = \frac{Prior × Likelihood}{Evidence}">

The Naive Bayes assumes the predictors are conditionally independent of one another

For continuous predictors, we typically make an additional assumption of normality so that we can use the probability from the probability density function (PDF).


#### Discriminant analysis (LDA, QDA)

#### Packages & Tools

[Lime: Explaining the predictions of any machine learning classifier](https://github.com/marcotcr/lime)


### Regression vs Classification

Different `y`: 
 
Regression: response is quantitative (continuous)
 
Classification: response is qualitative (binary/multinomial)

Different loss functions

### Tree-based Methods

#### Classification trees

#### Boosted regression trees

#### Random forests

#### GBDT: Gradient Boosting Decision Tree

[Quora: RF vs GTB](https://www.quora.com/What-are-the-differences-between-Random-Forest-and-Gradient-Tree-Boosting-algorithms)

GBDT loss fucntion


## Unsupervised Machine Learning

### Exploratoty data analysis

### Visualization 

1. Histograms

2. Boxplot

3. t-SNE

### Factor analysis

### Discriminant analysis

### Clustering

1. Distance

2. Clusterability

3. Kmeans

4. Hard partitioning

5. Soft partitioning

6. Hierarchical clustering

7. Gaussian mixture models

### Association rule mining

## Dimensionality reduction

TO solve problems such as multicollinearity, overfitting, and curse of dimensionality

### Principal component analysis
[Python example](https://vitalflux.com/pca-explained-variance-concept-python-example/)
Objective: transform the predictors and then fit a least squares model using the transformed variables instead of the original predictors

 <img src="https://render.githubusercontent.com/render/math?math=Z_m = \sum_{j=1}^p \varphi_jm X_j <img src="https://render.githubusercontent.com/render/math?math=	

* Uses an eigen decomposition to transform the original data into linearly independent eigenvectors
* Explained variance represents the information explained using a particular principal components (eigenvectors)
* Explained variance is calculated as ratio of eigenvalue of a articular principal component (eigenvector) with total eigenvalues.
* Most important vectors (with highest eigenvalues) are then selected to represent the features in the transformed space

### Non-negative matrix factorization (NMF)

* can be used to reduce dimensionality for certain problem types while preserving more information than PCA

### Embedding techniques 

* various embedding techniques, e.g. finding local neighbors as done in Local Linear Embedding, can be used to reduce dimensionality

### Clustering or centroid techniques 

* each value can be described as a member of a cluster, a linear combination of clusters, or a linear combination of cluster centroids

Source: [Kyle McKiou](https://www.linkedin.com/posts/kylemckiou_datascience-qanda-activity-6624299953705627648-WNjl/)


### Application: Chatbox

#### Ex: Return ngrams

Q: write a function to return ngram(string,n)  eg: ngram("abc",2) ---> ["a","b","c","ab","bc"]

### Text Summarization

[Towards DS: Text Summarization with Amazon Reviews](https://towardsdatascience.com/text-summarization-with-amazon-reviews-41801c2210b)

## Reinforcement Learning

Purpose: max the performance of the machine in a way that helps it to grow

GAN

## Deep Learning

[Book by Amazon Scientists: Dive into Deep Learning](http://d2l.ai/)

[Neural network charts](https://towardsdatascience.com/the-mostly-complete-chart-of-neural-networks-explained-3fb6f2367464)

Single layer and multi-layer perceptron neural nets

Convolutional Neural Network

Recursive Neural Network

Self-organizing maps

Dropout

Batch Normalization

Back propagation

Keras

Tensorflow

## Recommendation Systems

Collaborative Filtering

## Information Retrieval

Search/Display

Ads retrieval and recommendation

Spam-traffic and click-farm detection

Infrastructure development

Traffic and revenue prediction

Ads pricing

Audience expansion

## Links to online resources
[Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/ml-intro)

[An Introduction to Statistical Learning](https://faculty.marshall.usc.edu/gareth-james/ISL/ISLR%20Seventh%20Printing.pdf)

[The Elements of Statistical Learning (2nd edition)](https://web.stanford.edu/~hastie/ElemStatLearn/printings/ESLII_print12.pdf)

[Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)

[Understanding Machine Learning: From Theory to Algorithms](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf)

[Machine Learning Yearning](https://d2wvfoqc9gyqzf.cloudfront.net/content/uploads/2018/09/Ng-MLY01-13.pdf)

[CS231n Convolutional Neural Networks for Visual Recognition](http://cs231n.github.io/)

[Penn CIS520: Machine Learning](https://alliance.seas.upenn.edu/~cis520/dynamic/2019/wiki/index.php?n=Main.HomePage)

[Unofficial Google Colaboratory Notebook and Repository Gallery](https://github.com/firmai/awesome-google-colab)

[Awesome Machine Learning Jupyter Notebooks for Google Colaboratory](https://github.com/toxtli/awesome-machine-learning-jupyter-notebooks-for-colab)

[Toronto CSC401/2511: Natural Language Computing](https://www.cs.toronto.edu/~frank/csc401/)

[Stanford CS224N: NLP with Deep Learning | Winter 2019](https://www.youtube.com/playlist?list=PLoROMvodv4rOhcuXMZkNm7j3fVwBBY42z)

[Stanford CS231n: Convolutional Neural Networks for Visual Recognition | Spring 2019](http://cs231n.stanford.edu/)

[Toronto CSC 421/2516: Neural Networks and Deep Learning | Winter 2019](https://www.cs.toronto.edu/~rgrosse/courses/csc421_2019/)

[Machine Learning Interview Questions](https://github.com/andrewekhalel/MLQuestions)




<details>
<summary> 
  
</summary>
<br>
  
<br>
</details>
