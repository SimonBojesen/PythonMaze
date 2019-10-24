import kkdata
import matplotlib.pyplot as plt

neighbourhoods_in_2015_data = kkdata.STATISTICS[2015].keys()
print('neighbourhoods: ',neighbourhoods_in_2015_data)
print('age range of neighbourhood 1', kkdata.STATISTICS[2015][1].keys(),'\n')
print('20 year olds in hood 1', kkdata.STATISTICS[2015][1][20], '\n')
print('20 year old danes in hood 1 (danes=5100)', kkdata.STATISTICS[2015][1][20][5100])
neighbourhoods = neighbourhoods_in_2015_data

def get_population_stat(year_of_interest=2015):
    neighbourhoods = kkdata.STATISTICS[year_of_interest].keys()
    age_range = set([])
    for n in neighbourhoods:
        age_range.update(kkdata.STATISTICS[year_of_interest][n].keys())

    no_citicens_per_age = {}

    for n in neighbourhoods:
        for age in age_range:
            if age in kkdata.STATISTICS[year_of_interest][n].keys():
                c_codes = set(kkdata.STATISTICS[year_of_interest][n][age].keys())
                for f_code in c_codes:
                    no_citicens_per_age.setdefault(age, 0)
                    no_citicens_per_age[age] += kkdata.STATISTICS[year_of_interest][n][age][f_code]

    return no_citicens_per_age

stats = get_population_stat(2015)
ages = list(stats.keys())
no_citicens = list(stats.values())

#plt.cla()
plt.bar(ages, no_citicens, width=0.5, align='center') # bar(x-vals, y-vals, bar width, align bar relative to x-val on x-axis) )
#plt.ticklabel_format(useOffset=False)
plt.axis([0, max(ages) + 10, 0, 17000]) #axis(x-min, x-max, y-min, y-max)
title = 'Distribution of {} CPH Citizens in {}'.format(sum(no_citicens), 2015)
plt.title(title, fontsize=12)
plt.xlabel("Ages", fontsize=10)
plt.ylabel("Amount", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()