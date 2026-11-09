import pygame
import sys

class Myrobot:
    def __init__(self, name, color, weight, price, height, width, depth, speed, battery_life, material, manufacturer, model_number, year_of_manufacture, operating_system, connectivity, sensors, actuators, autonomy_level, payload_capacity, degrees_of_freedom):
        self.name = "RoboPal"
        self.color = "red, white, and blue"
        self.weight = 15.5  # in kilograms
        self.price = 1499.99  # in USD
        self.height = 130.0  # in centimeters
        self.width = 60.0  # in centimeters
        self.depth = 40.0  # in centimeters
        self.speed = 45.0  # in kilometers per hour
        self.battery_life = 8.0  # in hours
        self.material = "aluminum & iron, plastic"
        self.manufacturer = "RoboTech Industries"
        self.model_number = "Rp-2026-04-07"
        self.year_of_manufacture = 2026
        self.operating_system = "RoboOS 3.0"
        self.connectivity = "Wi-Fi, Bluetooth, 5G"
        self.sensors = ["LIDAR", "ultrasonic", "infrared", "camera"]
        self.actuators = ["servo motors", "hydraulic arms", "grippers", "rotating limbs"]
        self.autonomy_level = 4  # Level 4 autonomy
        self.payload_capacity = 100.0  # in kilograms
        self.degrees_of_freedom = 360  # in degrees

    def move(self, direction, distance):
        return f"{self.name} is moving {direction} for {distance} meters."
    
    def perform_task(self, task):
        return f"{self.name} is performing the task: {task}."
    
    def recharge(self):
        return f"{self.name} is recharging its battery."
    
    def get_info(self):
        """Returns robot information as a list of strings for display"""
        return [
            f"Name: {self.name}",
            f"Color: {self.color}",
            f"Weight: {self.weight} kg",
            f"Price: ${self.price}",
            f"Dimensions (HxWxD): {self.height} x {self.width} x {self.depth} cm",
            f"Speed: {self.speed} km/h",
            f"Battery Life: {self.battery_life} hours",
            f"Material: {self.material}",
            f"Manufacturer: {self.manufacturer}",
            f"Model Number: {self.model_number}",
            f"Year of Manufacture: {self.year_of_manufacture}",
            f"Operating System: {self.operating_system}",
            f"Connectivity: {self.connectivity}",
            f"Sensors: {', '.join(self.sensors)}",
            f"Actuators: {', '.join(self.actuators)}",
            f"Autonomy Level: {self.autonomy_level}",
            f"Payload Capacity: {self.payload_capacity} kg",
            f"Degrees of Freedom: {self.degrees_of_freedom} degrees"
        ]

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RoboPal Robot Information")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 200)
LIGHT_GRAY = (240, 240, 240)

# Fonts
title_font = pygame.font.Font(None, 48)
info_font = pygame.font.Font(None, 24)
message_font = pygame.font.Font(None, 20)

# Create robot instance
robot = Myrobot("RoboPal", "red, white, and blue", 15.5, 1499.99, 130.0, 60.0, 40.0, 45.0, 8.0, "aluminum & iron, plastic", "RoboTech Industries", "Rp-2026-04-07", 2026, "RoboOS 3.0", ["Wi-Fi", "Bluetooth", "5G"], ["LIDAR", "ultrasonic", "infrared", "camera"], ["servo motors", "hydraulic arms", "grippers", "rotating limbs"], 4, 100.0, 360)

# Get robot information
info_lines = robot.get_info()

# Get action messages
action_messages = [
    robot.move("forward", 10),
    robot.perform_task("pick up an object"),
    robot.recharge()
]

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill background
    screen.fill(LIGHT_GRAY)
    
    # Draw title
    title_surf = title_font.render("RoboPal Information", True, BLUE)
    screen.blit(title_surf, (20, 20))
    
    # Draw robot information
    y_offset = 80
    for line in info_lines:
        info_surf = info_font.render(line, True, BLACK)
        screen.blit(info_surf, (30, y_offset))
        y_offset += 32
    
    # Draw action messages
    y_offset += 20
    action_title = message_font.render("Robot Actions:", True, BLUE)
    screen.blit(action_title, (30, y_offset))
    y_offset += 30
    
    for action in action_messages:
        action_surf = message_font.render(action, True, BLACK)
        screen.blit(action_surf, (50, y_offset))
        y_offset += 25
    
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
