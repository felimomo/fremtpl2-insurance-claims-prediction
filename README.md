# Predicting Insurance Claims with GLMs and GLMMs

In this repository I fit statistical models to insurance claim data using the
[fremtpl2](https://www.kaggle.com/datasets/cbalona/fremtpl2freq) dataset.
Specifically I focus on how the variables in the dataset can be used to predict
insurance claim number and amount.

Up to now: MLE for a GLM and a GLMM predicting number of claims. These two models
give pretty similar results which hints at the random effect used not being
especially informative. Upcoming: Bayesian inference on the GLMM using PyMC.

To recreate the environment which I used and run the analysis, use the `reproduce.sh` 
script.

Work in progress...
