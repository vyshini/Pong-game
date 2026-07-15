from PIL import Image
import pandas as pd
import os

print("current working directory :",os.getcwd())

im = Image.open("India-state.gif")
im.save("India-state.png")
print(im.size)

df = pd.read_csv("states_data.csv")
df.to_json("states.json",orient = "records")