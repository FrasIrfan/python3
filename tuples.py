def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours,minutes,remaining_seconds
#Instead of returning each value separately, you're returning them together separated by commas. 
#Python automatically creates a tuple with these values.
user_seconds = int(input("Enter the number of seconds: "))
result = convert_seconds(user_seconds)
print (type(result))
# print (result)
formatted_output = f"{result[0]} hours {result[1]} minutes and {result[2]} seconds"
print(formatted_output)