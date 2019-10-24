import csv
import platform
if platform.system() == 'Windows':
    newline=''
else:
    newline=None
with open("output.csv", 'w', newline=newline) as output_file:
    output_writer = csv.writer(output_file)

    output_writer.writerow(['2015', '1', '0', '5100', '614,5'])
    output_writer.writerow(['2015', '1', '0', '5104', '2,3'])
    output_writer.writerow(['2015', '1', '0', '5106', '1'])
    output_writer.writerow(['2015', '1', '0', '5110', '1'])