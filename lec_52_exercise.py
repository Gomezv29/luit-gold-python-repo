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

for time in connections:
    print(time[2])

def average(connections):
    total = 0
    count = 0
    for time in connections:
        total += time[2]
        count += 1
        return total / count

avg_flight_time = average(connections)

print('Average flight time:', avg_flight_time)    


#print(' with an average flight time of ', time_avg, 'minutes')
