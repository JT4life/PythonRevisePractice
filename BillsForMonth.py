import datetime
import calendar
'''Background
In the past, we provided some raw billing data in JSON format to the finance team, which they used to manually generate
 monthly invoices for our customers. Recently, they’ve asked us to create some automation to make this process less error-prone.
Instructions
Your goal is to implement the bill_for function to calculate the total monthly bill for a customer.
Customers are billed based on their subscription tier for the month. We charge them a prorated amount for each user who 
was active during that month. You talked with the other engineers on the team and decided that the following algorithm would work:

    Calculate a daily rate for the active subscription tier
    For each day of the month, identify which users were active that day
    Multiply the number of active users for the day by the daily rate to calculate the total for the day
    Return the running total for the month at the end, rounded to 2 decimal places

Parameters
This billing function accepts the following parameters:
month
Always present. Has the following structure:
"2019-01"   # January 2019 in YYYY-MM format
active_subscription
May be None. If present, has the following structure:
{
  'id': 1,
  'customer_id': 1,
  'monthly_price_in_dollars': 4  # price per active user per month
}
users
May be empty, but not None. Has the following structure:
[
  {
    'id': 1,
    'name': 'Employee #1',
    'customer_id': 1,

    # when this user started
    'activated_on': datetime.date(2018, 11, 4),

    # last day to bill for user
    # should bill up to and including this date
    # since user had some access on this date
    'deactivated_on': datetime.date(2019, 1, 10)
  },
  {
    'id': 2,
    'name': 'Employee #2',
    'customer_id': 1,

    # when this user started
    'activated_on': datetime.date(2018, 12, 4),

    # hasn't been deactivated yet
    'deactivated_on': None
  }
]
'''
def bill_for(month, active_subscription, users):
    # month = "2019-01", active_subscription = dictionary, may be None, users not None, dictionary
    # Active users * daily rate
    # return total 2 decimals places .00

    active_users = 0
    if users == None or active_subscription == None:
      return 0
    elif month >= users['activated_on'] and month <= users['deactivated_on']:
        for numberOfUsers in users:
            active_users += 1
    total = active_subscription['monthly_price_in_dollars']*active_users
    rounded = str(round(total, 2))
    return rounded

active_subscription = {
  'id': 1,
  'customer_id': 1,
  'monthly_price_in_dollars': 4  # price per active user per month
}
month = "2019-01"
users = [
  {
    'id': 1,
    'name': 'Employee #1',
    'customer_id': 1,
    # when this user started
    'activated_on': datetime.date(2018, 11, 4),
    # last day to bill for user
    # should bill up to and including this date
    # since user had some access on this date
    'deactivated_on': datetime.date(2019, 1, 10)
  },
  {
    'id': 2,
    'name': 'Employee #2',
    'customer_id': 1,
    # when this user started
    'activated_on': datetime.date(2018, 12, 4),
    # hasn't been deactivated yet
    'deactivated_on': None
  }
]
print(bill_for(month, active_subscription, users))

# Helper Functions
def first_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the first day of that month. For example:

    >>> first_day_of_month(datetime.date(2019, 2, 7))  # Feb 7
    datetime.date(2019, 2, 1)                          # Feb 1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date.replace(day=1)


def last_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the last day of that month. For example:

    >>> last_day_of_month(datetime.date(2019, 2, 7))  # Feb  7
    datetime.date(2019, 2, 28)                        # Feb 28

    Input type: datetime.date
    Output type: datetime.date
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return datetime.date(date.year, date.month, last_day)


def next_day(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the next day. For example:

    >>> next_day(datetime.date(2019, 2, 7))   # Feb 7
    datetime.date(2019, 2, 8)                 # Feb 8

    >>> next_day(datetime.date(2019, 2, 28))  # Feb 28
    datetime.date(2019, 3, 1)                 # Mar  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date + datetime.timedelta(days=1)