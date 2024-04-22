from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Los usuarios esperan entre 1 y 5 segundos después de cada tarea.
    wait_time = between(1, 5)

    @task
    def load_main_page(self):
        # Realiza una solicitud GET a la página principal.
        self.client.get("/")

    # @task(3)
    # def load_dashboard(self):
    #     # Realiza una solicitud GET a la página del dashboard.
    #     # Esta página tiene un peso mayor en la simulación (3 veces más frecuente que la principal).
    #     self.client.get("/dashboard")