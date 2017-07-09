# BloodTransfusion_prediction

This exercise is aimed to be an introduction to the typical data science pipeline. The problem at hand is as follows. Given a set of features, one has to predict whether the person will come for blood donation again at a point of time in the future.
The workflow is as follows:
1. We read in the data and do a primary scrutiny of the data.
2. Remove redundant features and add in more features if required
3. Make an educated guess about the algorithm that might work on this class of problems
4. Run the algorithm. Compute some accuracy metric.
5. Tweak the parameters. Compare the accuracy.

Up until now, we have made significant headways into this problem. We observed that, the average volume of blood donated per visit is same for all. So this feature is discarded. We think of adding a new feature that encapsulates the monthly frequency of the blood donations made by a person.

Next since this is a simple class of problem, we avoid using neural nets. We start off with SVM. The best accuracy is given by a Radial Basis Function Kernel with C = 1.0 (overfitting parameter). We get a best case accuracy of 0.895

Next we try nearest neighbors, Linear Discriminant Analysis algorithms. They give lesser accuracy than SVM. Next we try decision trees which gives an accuracy of 0.9375.
