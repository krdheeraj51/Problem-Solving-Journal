# Business Day Count
# Given a start date and an end date, return the number of business days between the two.

# Given dates are in the format "YYYY-MM-DD".
# Weekdays are business days (Monday through Friday).
# Weekends are not business days (Saturday and Sunday).
# Include both the start and end dates when counting.


def business_day_count(start_date, end_date):
    from datetime import datetime, timedelta

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    print(start, end)

    
    business_days = 0
    current_date = start
    
    while current_date <= end:
        if current_date.weekday() < 5:  # Monday to Friday are business days
            business_days += 1
        current_date += timedelta(days=1)
    
    return business_days

print(business_day_count("2026-02-01", "2026-02-28"))  # 20
print(business_day_count("2026-02-01", "2026-02-01"))  # 1