import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

#print(ad_clicks.head(10))

utm_source_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()

#print(utm_source_count)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

#print(ad_clicks)

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

#print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id'
).reset_index()



clicks_pivot['percent_clicked'] = clicks_pivot[True] /(clicks_pivot[False] + clicks_pivot[True])*100

#print(clicks_pivot)

clicks_by_experimental_group = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

#print(clicks_by_experimental_group)

clicks_by_experimental_group_pivot = clicks_by_experimental_group.pivot(
  columns='is_click',
  index='experimental_group',
  values='user_id'
).reset_index()

clicks_by_experimental_group_pivot['percent_clicked'] = clicks_by_experimental_group_pivot[True] /(clicks_by_experimental_group_pivot[False] + clicks_by_experimental_group_pivot[True])*100

#print(clicks_by_experimental_group_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'].reset_index()

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'].reset_index()

#print(a_clicks)
#print(b_clicks)

a_clicks_count = a_clicks.groupby('day').user_id.count().reset_index()

b_clicks_count = b_clicks.groupby('day').user_id.count().reset_index()

#print(type(b_clicks_count))

#print(a_clicks_count)
#print(b_clicks_count)

day_count = ad_clicks.groupby('day').user_id.count().reset_index()

#print(day_count)
