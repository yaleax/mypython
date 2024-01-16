import csv

import csv

with open('TOP250.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    counts = {}
    for row in reader:
        favorite = row['评分']
        movie = row['电影名称']  # 假设列标题为“电影名称”

        if favorite not in counts:
            counts[favorite] = {'count': 0, 'movies': []}

        counts[favorite]['count'] += 1
        counts[favorite]['movies'].append(movie)

for favorite, data in counts.items():
    movies_list = ', '.join(data['movies'])
    print(f"{favorite}分的电影有{data['count']}部，包括：{movies_list}")




