import pandas as pd
import quandl as qd

qd.ApiConfig.api_key = "cXwBEsMkyycaT_gLGCVy"

msft_data = qd.get("XETR/NOVA",
                   start_date="2018-11-28",
                   end_date="2018-11-30")
msft_data.head()
