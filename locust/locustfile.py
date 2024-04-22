from locust import HttpUser, task, between
import json

class PenguinApiUser(HttpUser):
    wait_time = between(1, 5)  # Los usuarios esperan entre 1 y 5 segundos entre tareas

    @task
    def predict_penguin(self):
        url = "/predict/"
        headers = {'Content-Type': 'application/json'}
        data = {
            "studyName": ["Example Study"] * 3,
            "Sample_Number": [101, 102, 103],
            "Region": ["Region1", "Region2", "Region3"],
            "Island": ["Island1", "Island2", "Island3"],
            "Stage": ["Adult", "Juvenile", "Adult"],
            "Individual_ID": ["A123", "A124", "A125"],
            "Clutch_Completion": ["Yes", "No", "Yes"],
            "Date_Egg": ["2021-06-01", "2021-06-02", "2021-06-03"],
            "Sex": ["Male", "Female", "Male"],
            "Delta_15_N_ooo": ["0.5", "0.6", "0.7"],
            "Delta_13_C_ooo": ["0.4", "0.3", "0.2"],
            "Comments": ["None", "None", "None"],
            "Culmen_Length_mm": [49.1, 48.7, 50.0],
            "Culmen_Depth_mm": [18.7, 17.3, 19.6],
            "Flipper_Length_mm": [200, 195, 193],
            "Body_Mass_g": [3800, 3700, 3600]
        }
        response = self.client.post(url, headers=headers, data=json.dumps(data), params={"model_type": "decision_tree"})
        print("Response status code:", response.status_code)
        print("Response data:", response.text)