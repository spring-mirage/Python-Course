from datetime import date

# Converting ISO format string to date object
date_str = "2023-04-01"
date_obj = date.fromisoformat(date_str)
print(date_obj) # Output: 2023-04-01