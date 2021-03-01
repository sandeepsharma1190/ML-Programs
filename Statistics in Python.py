# Statistics in Python

# Example of the Shapiro-Wilk Normality Test

# Hypothesis : - A statistical hypothesis is an assumption made about a population parameter. This assumption may or may not be right.

# Null Hypothesis : - Study, which exists
# Alternate Hypothesis : - Study, which can replace already existed Hypothesis.

# Significance level of P can determine whether Alternate hypothesis will takes place or not

# We have many statistical hypothesis tests available in Python, which can be accessed through Scipy in Python. By importing scipy.stats to be more granular.

# https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/

# from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau
from scipy.stats import ttest_rel
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import friedmanchisquare
from scipy.stats import chi2_contingency


from scipy import stats

data1 = [1,2,3,4,5,6,7,8]
data2 = [4,5,6,7,8,9,1,2]
data3 = [8,9,1,2,3,4,5,6]

# data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
# data2 = [0.353, 3.517, 0.125, -7.545, -0.555, -1.536, 3.350, -1.578, -3.537, -1.579]
# data3 = [-0.208, 0.696, 0.928, -1.148, -0.213, 0.229, 0.137, 0.269, -0.870, -1.204]

# Normality Test
stat, p = stats.normaltest(data1)
print('stat = %.2f, p = %.2f' % (stat, p))

# Pearson’s Correlation
stat, p = stats.pearsonr(data1, data2)
print('stat = %.2f, p = %.2f' % (stat, p))

# Spearman’s Rank Correlation
stat, p = stats.spearmanr(data1, data2)
print('stat = %.2f, p = %.2f' % (stat, p))

# Kendall’s Rank Correlation
stat, p = stats.kendalltau(data1, data2, data3)
print('stat = %.2f, p = %.2f' % (stat, p))

# T-Test
# means of two independent samples
stat, p = stats.ttest_ind(data1, data2)
print('stat = %.2f, p = %.2f' % (stat, p))

# means of two paired samples
stat, p = stats.ttest_rel(data1, data2)
print('stat = %.2f, p = %.2f' % (stat, p))

# Analysis of Variance (ANOVA)
stat, p = stats.f_oneway(data1, data2)
print('stat = %.2f, p = %.2f' % (stat, p))

stat, p = stats.f_oneway(data1, data2, data3)
print('stat = %.2f, p = %.2f' % (stat, p))

# Friedman Test
stat, p = stats.friedmanchisquare(data1, data2, data3)
print('stat = %.2f, p = %.2f' % (stat, p))



# Chi-Squared Test

stat, p, dof, expected = stats.chi2_contingency([data1, data2, data3])
print('stat = %.2f, p = %.2f' % (stat, p))
print ('dof = %.2f' %dof)

stat, p, dof, expected = stats.chi2_contingency([data1, data2])
print('stat = %.2f, p = %.2f' % (stat, p))
print ('dof = %.2f' %dof)


stat, p = stats.chi2_contingency([data1, data2, data3])
print('stat = %.2f, p = %.2f' % (stat, p))


# significance level, also denoted as alpha or α
if p > 0.05:
	print('signifies a greater than 5%')
else:
	print('signifies a smaller than 5%')

































    