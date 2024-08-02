

1. Data contains nulls, and outliers exist; first filling nulls and
extracting outliers, or vice versa?

# First, remove or eliminate (! clip) outliers, then fill the nulls


Numeric variable ==> salary, age, heart beat, credit score....


	filling ==> mean, meadian, normal distribution, guess....

	outlier ==> exclude!
	outlier ==> clip!

	outlier ==> split
	nulls   ==> split


2. What to do when the target is imbalanced. 
Also when some columns are imbalanced but have high corr to target.
If we take a sample in which class sizes are equal, 
will it result in data loss? Or any other solutions.


3. f1_score has a parameter 'average=macro or weighted'. 
Especially when data is imbalanced when applying this parameter, 
f1_score increases significantly.
Could it be used? If yes, when?


4. Can LDA and PCA be applied to every dataset?

Classification, Regression => LDA, PCA (supervised)
Clustering => PCA (unsupervised)

Time Series (!)


5. Main focus in clustering; 
how many clusters? 
2!,3,4,5,6,7,---10-12 (in general)
400 => can we manage it? NO 

How to know if it is well segmented?
Business department

6. Most points in the dataset labelled as -1 by DBSCAN. 
When increasing epsilon, all points labelled as 0. 
How to fix?  

>> In a real dataset it is most unlikely to happen
RANDOM,
MIXTURE,
SYNTECHIC





