import re

# text = '''
# The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
# In previous quarter i.e. FY2020 Q4 it was $3 billion. fy2029 Q2 FY2025 Q3 FY2026 Q44
# '''

# pattern = r"FY(\d{4} Q[1-4])[^\$]+\$([\d.]*)"

# money_pattern = r"\$([\d.]*)"

# pattern_found = re.findall(pattern, text, flags=re.IGNORECASE)
# matches = re.findall(money_pattern, text)

# print(matches)
# print(pattern_found)

# for data in pattern_found:
#     # print(f"Year: {data[0][2:]}\tQuarter: {data[1]}")
#     data_list = data.split()
#     print(f"Year: {data_list[0][2:]}\tQuarter: {data_list[1]}")

text = '''
Follow our leader Elon musk on twitter hear: https://twitter.com/elonmusk, more information
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''

text_2 = '''

'''

pattern = "https://twitter.com/(\w+)"

print(re.findall(pattern, text))