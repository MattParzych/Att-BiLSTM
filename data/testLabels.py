import json

labels = []

with open('test.json', 'r', encoding='utf-8') as fr:
   for line in fr:
      line = json.loads(line.strip())
      label = line['relation']
      if label not in labels:
         labels.append(label)

print(labels)
