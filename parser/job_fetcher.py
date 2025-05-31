import requests

JOB_API_URL = "http://localhost:8080/api/jobs/cached" 

# def fetch_cached_jobs():
#     try:
#         response = requests.get(JOB_API_URL)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print("Failed to fetch jobs:", response.status_code)
#             return []
#     except Exception as e:
#         print("Error fetching jobs:", e)
#         return []

def fetch_cached_jobs():
    try:
        response = requests.get(JOB_API_URL)
        print("Fetched raw job data:", response.text[:300])
        if response.status_code == 200:
            return response.json() 
        else:
            print("Failed to fetch jobs:", response.status_code)
            return []
    except Exception as e:
        print("Error fetching jobs:", e)
        return []
