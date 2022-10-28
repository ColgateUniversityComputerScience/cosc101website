day = input("Day (lowercase): ")
hour = int(input("Hour (24 hour): "))
minute = int(input("Minute: "))

# Week starts on Monday
if day == 'monday':
	curr_mins = hour*60 + minute
elif day == 'tuesday':
	curr_mins = 24*60*1 + hour*60 + minute
elif day == 'wednesday':
	curr_mins = 24*60*2 + hour*60 + minute
elif day == 'thursday':
	curr_mins = 24*60*3 + hour*60 + minute
elif day == 'friday':
	curr_mins = 24*60*4 + hour*60 + minute
elif day == 'saturday':
	curr_mins = 24*60*5 + hour*60 + minute
elif day == 'sunday':
	curr_mins = 24*60*6 + hour*60 + minute


class_hour = 8
class_mins = 30

class_mins_tues = 24*60*1 + class_hour*60 + class_mins
class_mins_thurs = 24*60*3 + class_hour*60 + class_mins

if curr_mins < class_mins_tues:
	mins_remaining = class_mins_tues - curr_mins

elif curr_mins > class_mins_tues and curr_mins < class_mins_thurs:
	mins_remaining = class_mins_thurs - curr_mins

else:
	mins_remaining_week = 7*24*60 - curr_mins
	mins_mon_to_tues = 24*60*1 + class_hour*60 + class_minute
	mins_remaining = mins_remaining_week + mins_mon_to_tues

hours = mins_remaining//60
minutes = mins_remaining%60


# mins_to_midnight = 60-minute

# if minute > 0:
# 	hours_to_midnight = 23-hour ## Why is this 23 and not 24? 
# else:
# 	hours_to_midnight = 24-hour


# total_mins_to_midnight = hours_to_midnight*60 + mins_to_midnight

# class_start_hour = 8
# class_start_mins = 30

# class_end_hour = 9
# class_end_mins = 45


# mins_to_class_start = class_start_hour*60 + class_start_mins
# mins_to_class_end = class_end_hour*60 + class_end_mins


# if day == 'monday' or day == 'wednesday':
# 	# Find time until midnight. 
# 	total_mins = total_mins_to_midnight + mins_to_class

# elif day == 'friday':
# 	total_mins = total_mins_to_midnight + mins_to_class + 24*60*3 # saturday + sunday + monday


# elif day == 'Tuesday':
# 	curr_mins = hour*60 + minute
# 	if curr_mins < mins_to_class_end:
# 		if curr_mins < mins_to_class_start:
# 			print('You are in class')
# 		else:
# 			mins_remaining = 


# 	elif 

	
	



