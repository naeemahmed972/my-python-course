

# You need to empty out the rectangular swimming pool which is 12 meters long, 7 meters wide and 2 meter depth. You have a pump which can move 17 cubic meters of water in an hour. Write a program to find how long it will take to empty your pool? (Volume = l * w * h, and flow = volume/time).


# Volume = L x W x H
# Flow rate = 17 m^3/hr
# Flow = volume/time
# time = volume/flow


















pool_length = 12
pool_width = 7
pool_height = 2

flow_rate = 17

pool_volume = 12 * 7 * 2

time_to_empty = round(pool_volume / flow_rate)

print(f"It will take app. {time_to_empty} hrs to empty the pool")