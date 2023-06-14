import requests
import random
import pandas as pd

token_code = "72b2d686746ea2"
valid_ips = []
while len(valid_ips) !=50:
    ip1 = random.randint(1,255)
    ip2 = random.randint(0,255)
    ip3 = random.randint(0,255)
    ip4 = random.randint(1,255)
    while (result:=requests.get(f"https://ipinfo.io/{ip1}.{ip2}.{ip3}.{ip4}?token=72b2d686746ea2")).status_code == 404:
        ip1 = random.randint(1,255)
        ip2 = random.randint(1,255)
        ip3 = random.randint(1,255)
        ip4 = random.randint(1,255)
    valid_ips.append(result.json())

df = pd.DataFrame(valid_ips)
#print(df["country"])
unique_countries = df["country"].dropna().drop_duplicates()
# two descriptive statistics
print("2 descriptave statistics:")
#1 
print(f"unique countries:\n{unique_countries}")
print(f"number of unique countries: {len(unique_countries)}")
#2
print(f"number of columns: {len(df.columns)}")

#Write a query in Pandas
print("\n\n\nquery in pandas\n")
na_city = df.query('country.isnull()')
print(na_city)

#Select and print the SECOND AND THIRD columns of your data frame.
second_and_third = df[df.columns[1:3]]
print(f"\n\n\nSecond and Third columns: \n{second_and_third}")

#Select and print the FIRST 4 rows of you data frame.
print("\n\nSelect and print the FIRST 4 rows of you data frame.\n")
print(df.head(4))