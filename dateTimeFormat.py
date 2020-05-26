from datetime import datetime
now = datetime.now()
print('{:%Y-%B-%d %H:%M:%S %p %A}'.format(now))
# 2019-May-01 13:06:36 PM Saturday
print('{:%y-%b-%d %I:%M:%S %p %a}'.format(now))
# 19-May-01 01:06:36 PM Sat# American style date, May 01, 19
print('{%B %d, %y}'.format(now))