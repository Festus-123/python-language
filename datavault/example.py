
import numpy as np

# # Create an array of 100,000 random 3D coordinates (float32)
# coordinates = np.random.randn(1_000_000_000, 3).astype(np.float32)

# # Save directly to binary format
# coordinates.tofile("mesh_data.bin")

# # Read binary back into NumPy instantly
# loaded_coords = np.fromfile("mesh_data.bin", dtype=np.float32).reshape(-1, 3)

# print("Original shape:", coordinates.shape)
# print("Loaded shape:  ", loaded_coords.shape)

import time

# Representing 100,000 3D points as a list of [x, y, z] lists
points = [[10.0, 20.0, 5.0] for _ in range(100_000)]

start = time.perf_counter()

# Loop through every single coordinate manually
transformed = []
for p in points:
    new_x = p[0] * 1.5
    new_y = p[1] * 1.5
    new_z = (p[2] * 1.5) + 10.0
    transformed.append([new_x, new_y, new_z])

duration = time.perf_counter() - start
print(f"Python Loop time: {duration:.4f} seconds")


# player_data = {
#     "player_id": 1042,
#     "position": [12.4, -5.2, 100.8],
#     "inventory": ["sword", "shield", "potion"],
#     "health": 98.5,
# }

# # Save Python object to binary
# with open("player_save.bin", "wb") as f:
#     pickle.dump(player_data, f)

# # Read Python object back from binary
# with open("player_save.bin", "rb") as f:
#     loaded_data = pickle.load(f)

# print(loaded_data["position"])
