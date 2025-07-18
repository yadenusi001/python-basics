# Define meal for the day

def breakfast():
    print("Good morning! How about having eggs and toast for breakfast")

# Define lunch function
def lunch():
    print("Good afternoon! You could do rice and chicken for lunch.")

# Define dinner function
def dinner():
    print("Good evening! Try pasta with vegetables for dinner.")

# Define meal controller function
def meal_suggestion(time_of_day):
    if time_of_day == "breakfast":
        breakfast()
    elif time_of_day == "lunch":
        lunch()
    elif time_of_day == "dinner":
        dinner()
    else:
        print("Error: Invalid time of day entered.")

# Test the meal_suggestion function with different times of day
meal_suggestion("breakfast")
meal_suggestion("lunch")
meal_suggestion("dinner")
meal_suggestion("midnight")  # Invalid time test