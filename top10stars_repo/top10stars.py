import pandas as pd
import requests 
from datetime import datetime

today = datetime.today()
print("Today's date:", today.strftime("%Y-%m-%d"))
df = pd.DataFrame(columns=['repository_ID', 'name', 'URL', 'created_date',  'description', 'number_of_stars']) 
results = requests.get('https://api.github.com/search/repositories?q=created:">2000-12-27"language:java&sort=stars&order=desc&per_page=10').json()
 
for repo in results['items']:
        d_tmp = {'repository_ID': repo['id'],
                'name': repo['name'],
                'URL': repo['html_url'],
                'created_date': datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
                'description':repo['description'],

                'number_of_stars': repo['stargazers_count']}
        df = df.append(d_tmp, ignore_index=True)

df.to_csv('top10stars_repo_java.csv',encoding='utf_8_sig')

print(d_tmp)