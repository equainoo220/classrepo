from datetime import datetime

# Proper date format
def validate(date_text):
    try:
        # Search Python documentation online to see if strptime is being used correctly
        datetime.strptime(date_text,'%m-%d-%Y')
        return True
    except ValueError:
        return False

result = validate('11-20-2024')
print(result)