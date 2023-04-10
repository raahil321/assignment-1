import math

for angle in range(0, 346, 15):
    rad = math.radians(angle)
    sin = round(math.sin(rad), 4)
    cos = round(math.cos(rad), 4)
    print(f"Angle: {angle} degrees, Sine: {sin}, Cosine: {cos}")