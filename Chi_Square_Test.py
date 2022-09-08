# This program performed Chi-square test to prove that there is a significant
# difference between casual and member group from Monday to Sunday

import numpy as np
import pandas as pd
import scipy.stats as stats

casual = pd.DataFrame(["Mon"]*37005 + ["Tue"]*38825 +\
                        ["Wed"]*48387 + ["Thu"]*57978 + ["Fri"]*55868+\
                     ["Sat"]*65137 + ["Sun"]*65851)


member = pd.DataFrame(["Mon"]*46791 + ["Tue"]*54986 +\
                        ["Wed"]*68797 + ["Thu"]*73501 + ["Fri"]*57322+\
                     ["Sat"]*49694 + ["Sun"]*49062)

casual_table = pd.crosstab(index=casual[0], columns="count")
member_table = pd.crosstab(index=member[0], columns="count")

print( "Casual")
print(casual_table)
print(" ")
print( "Member")
print(member_table)


# ------------Manual perform Chi-square test------------------
observed = casual_table
expected = member_table

member_ratios = member_table/len(member)  # Get population ratios
print(len(member))

expected = member_ratios * len(casual)   # Get expected counts
#expected = member_table

chi_squared_stat = (((observed-expected)**2)/expected).sum()

print(chi_squared_stat)

crit = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories - 1

print("Critical value")
print(crit)

p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,  # Find the p-value
                             df=6)
print("P value")
print(p_value)

# ------------End Manual perform Chi-square test------------------

# ------------Automatic perform Chi-square test------------------
stats.chisquare(f_obs= observed,   # Array of observed counts
                f_exp= expected)   # Array of expected counts
# ------------End Automatic perform Chi-square test------------------
