import kkdata
import matplotlib.pyplot as plt

neighbourhoods_in_2015_data = kkdata.STATISTICS[2015].keys()
print('neighbourhoods: ',neighbourhoods_in_2015_data)
print('age range of neighbourhood 1', kkdata.STATISTICS[2015][1].keys(),'\n')
print('20 year olds in hood 1', kkdata.STATISTICS[2015][1][20], '\n')
print('20 year old danes in hood 1 (danes=5100)', kkdata.STATISTICS[2015][1][20][5100])
neighbourhoods = neighbourhoods_in_2015_data


def get_population_stat():
    
    age_range = set([])
    for n in neighbourhoods:
        age_range.update(kkdata.STATISTICS[2015][n].keys())

    no_danes_per_age = {}
    no_foreign_per_age = {}

    for n in neighbourhoods:
        for age in age_range:
            if age in kkdata.STATISTICS[2015][n].keys():
                c_codes = set(kkdata.STATISTICS[2015][n][age].keys())
                
                if 5100 in c_codes:
                    no_danes_per_age.setdefault(age, 0)
                    no_danes_per_age[age] += kkdata.STATISTICS[2015][n][age][5100]
                    
                    c_codes.remove(5100)

                for f_code in c_codes:
                    no_foreign_per_age.setdefault(age, 0)
                    no_foreign_per_age[age] += kkdata.STATISTICS[2015][n][age][f_code]
                    
    return no_danes_per_age, no_foreign_per_age # returning a comma separated set of elements creates a tuple

danes_per_age, foreigners_per_age = get_population_stat() #returned tuple is deconstructed into 2 variables

ages = list(danes_per_age.keys())
no_citicens = list(danes_per_age.values()) 
ages_f = list(foreigners_per_age.keys())
no_citicens_f = list(foreigners_per_age.values())

plt.bar(ages, no_citicens, width=0.5, linewidth=0, align='center')
plt.ticklabel_format(useOffset=False)
plt.axis([0, max(ages) + 10, 0, 17000])
title = 'Distribution of CPH Citizens in {}'.format(2015)
plt.title(title, fontsize=12)
plt.xlabel("Ages", fontsize=10)
plt.ylabel("Amount", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.bar(ages_f, no_citicens_f, width=0.5, linewidth=0, align='center', color='red')

fakes = list(range(10900, 300, -100))
print(len(ages), '\n\n', no_citicens, '\n\n', len(fakes))
#plt.bar(ages, fakes, width=0.5, linewidth=0, align='center', color='yellow')

plt.show()