class vehicle:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

modelx = vehicle(240, 18)

print("Model Max Speed:", modelx.max_speed)
print("Model Mileage:", modelx.milage)