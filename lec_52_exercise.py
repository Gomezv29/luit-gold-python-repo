# Flight connections in Europe

connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
    
    
    # Tuples above are in this format: (city_from, city_to, time) 
    
    # Use a loop to go through all the routes and check how many of them lead to Rome.
    # You should also calculate the avg. flight time.
    # Print this output: {} connections lead to Rome with an average flight time of {} minutes
    # Replace {} with # of connections and avg flight time.
count = 0
t = 0
i = 0

for city_to in connections:
    if city_to[1] == 'Rome':
        count += 1
    for time in connections:
        t += time[2]
        i += 1
        avg = t / i
print(count, 'connections lead to Rome with an average flight time of', avg, 'minutes')


#print(' with an average flight time of ', time_avg, 'minutes')

# answer to exercise
#counter = 0
#sum = 0.0
 
#for con in connections:
 #   if con[1] == 'Rome':
  #      counter += 1
   #     sum += con[2]
 
#print(counter, 'connections lead to Rome with an average flight time of', sum/counter, 'minutes')