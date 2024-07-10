import dotenv
dotenv.load_dotenv()

from chatbot_api.src.tools.wait_times import (get_current_wait_times,get_most_available_hospital,)

get_current_wait_times("Wallace-Hamilton")
'1 hours 35 minutes'

get_current_wait_times("fake hospital")
"Hospital 'fake hospital' does not exist."

get_most_available_hospital(None)
{'cunningham and sons': 24}


import dotenv
dotenv.load_dotenv()

from chatbot_api.src.tools.wait_times import (get_current_wait_times,get_most_available_hospital,)

get_current_wait_times("Wallace-Hamilton")


get_current_wait_times("fake hospital")


get_most_available_hospital(None)

