import requests
from datetime import datetime


APP_ID = "955fb082"
API_KEY = "528be99fdaf7a6bbd814c0ad19cf5f41"
nutritionix_endpoint = "https://trackapi.nutritionix.com"
USER_NAME = "011c8e45a9810491ce236612babfb554"
PROJECT_NAME = "workoutTracking"

exercise_endpoint = f"{nutritionix_endpoint}//v2/natural/exercise"
# exercise = input("Which exercises you did? ")

# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY
# }
# exercise_params = {
#     "query": exercise,
#     "gender":"male",
#     "weight_kg": 62.5,
#     "height_cm": 174.64,
#     "age": 33
# }

# response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
# result = response.json()

# sheety_endpoint = f"https://api.sheety.co/{USER_NAME}/{PROJECT_NAME}/workouts"

# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")

# for exercise in result["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }

#     sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)
#     print(sheet_response.text)
get_endpoint = "https://api.sheety.co/011c8e45a9810491ce236612babfb554/workoutTracking/workouts"

response = requests.get(url=get_endpoint, auth=("yusuf", "yusufyusufyusufyusuf"))
print(response.text)