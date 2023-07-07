import json

descriptor = json.load(open('descriptor_groups.json','r'))

other2 = descriptor['fr']
for desc in other2:
    print(desc['descriptor'],desc['display'])
    desc['display']= desc['descriptor']
    
json.dump(descriptor,open('descriptor_groups.json','w'),indent=4)