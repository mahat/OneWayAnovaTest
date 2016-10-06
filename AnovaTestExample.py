import pandas as pd
import scipy.stats as stats

#One Way ANOVA Example
# data is taken from: http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_HypothesisTesting-ANOVA/BS704_HypothesisTesting-Anova_print.html

# creating data frame 
d = {'Normal Bone Density': pd.Series([1200,1000,980,900,750,800]),
     'Osteopenia': pd.Series([1000,1100,700,800,500,700]),
     'Osteoporosis': pd.Series([890,650,1100,900,400,350])}

df = pd.DataFrame(d)

# significance level
alpha = 0.05  
# Perfrom ANOVA
outcome = stats.f_oneway(df['Normal Bone Density'],df['Osteopenia'],df['Osteoporosis'])
# gettin p-value of test
p_value= outcome[1]


#Null hypothesis mu_1= mu_2 = mu_3
if p_value <= alpha:
    # we reject null hypothesis
    print 'Null hypothesis is unlikely to except'
else:
    # we reject alternative hypothesis
    print 'Null hypothesis cannot be rejected'
    
    
#Two Way ANOVA Example
