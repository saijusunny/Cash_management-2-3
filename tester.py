from forex_python.converter import CurrencyRates
import datetime
from datetime import date,datetime, timedelta

c = CurrencyRates()

dt = datetime.today()



print(c.get_rate( 'INR','YEN', dt))