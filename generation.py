from PIL import Image 
from IPython.display import display 
import random
import json

#Attributes and their probabilities
background = ["Black", "Blue", "Dark_blue", "Dark_green", "Dark_purple", "Green", "Grey", "Orange", "Pink", "Purple", "White", "Yellow", "Blue_grad", "Green_grad", "Orange_grad", "Pink_grad", "Silver_grad", "Angles", "Angular_colors", "Black_lines", "Blueprint", "Coordinates", "Dot", "Ethereum", "Faith", "Forest", "Geo_pastel", "Geometrics", "Heaven", "Hypnotics", "Leaf", "Liked", "Linear_colors", "Lovely", "Maze", "Mesh", "Metaverse", "Metaverse_tunnel", "Midnight", "Mondrian", "Pastel_moon", "Plants", "Plume", "Rainbow", "Rainbow_road", "Signs", "Sky_cloud", "Solar", "Space", "Splash", "Splatter_blue", "Splatter_magenta", "Splatter_red", "Sunrise", "Sunset", "Superlative", "Valley", "Waves", "White_lines", "Zebra", "Zigzags"] 
background_weights = [1, 20, 15, 15, 10, 20, 10, 20, 7, 9, 1, 10, 3, 2, 1, 2, 1, 15, 20, 13, 11, 12, 25, 3, 5, 15, 14, 15, 5, 7, 20, 20, 30, 19, 8, 7, 3, 2, 6, 8, 21, 18, 17, 15, 13, 10, 18, 19, 6, 11, 15, 14, 13, 19, 14, 7, 21, 11, 12, 13, 14]

can = ["Classic", "BW", "Gold", "Negative"] 
can_weights = [60, 25, 10, 5]

#Properties and attributes
background_files = {
    "Black": "Black",
    "Blue": "Blue",
    "Dark_blue": "Dark_blue",
    "Dark_green": "Dark_green",
    "Dark_purple": "Dark_purple",
    "Green": "Green",
    "Grey": "Grey",
    "Orange": "Orange",
    "Pink": "Pink",
    "Purple": "Purple",
    "White": "White",
    "Yellow": "Yellow",
    "Blue_grad": "Blue_grad",
    "Green_grad": "Green_grad",
    "Orange_grad": "Orange_grad",
    "Pink_grad": "Pink_grad",
    "Silver_grad": "Silver_grad",
    "Angles": "Angles",
    "Angular_colors": "Angular_colors",
    "Black_lines": "Black_lines",
    "Blueprint": "Blueprint",
    "Coordinates": "Coordinates",
    "Dot": "Dot",
    "Ethereum": "Ethereum",
    "Faith": "Faith",
    "Forest": "Forest",
    "Geo_pastel": "Geo_pastel",
    "Geometrics": "Geometrics",
    "Heaven": "Heaven",
    "Hypnotics": "Hypnotics",
    "Leaf": "Leaf",
    "Liked": "Liked",
    "Linear_colors": "Linear_colors",
    "Lovely": "Lovely",
    "Maze": "Maze",
    "Mesh": "Mesh",
    "Metaverse": "Metaverse",
    "Metaverse_tunnel": "Metaverse_tunnel",
    "Midnight": "Midnight",
    "Mondrian": "Mondrian",
    "Pastel_moon": "Pastel_moon",
    "Plants": "Plants",
    "Plume": "Plume",
    "Rainbow": "Rainbow",
    "Rainbow_road": "Rainbow_road",
    "Signs": "Signs",
    "Sky_cloud": "Sky_cloud",
    "Solar": "Solar",
    "Space": "Space",
    "Splash": "Splash",
    "Splatter_blue": "Splatter_blue",
    "Splatter_magenta": "Splatter_magenta",
    "Splatter_red": "Splatter_red",
    "Sunrise": "Sunrise",
    "Sunset": "Sunset",
    "Superlative": "Superlative",
    "Valley": "Valley",
    "Waves": "Waves",
    "White_lines": "White_lines",
    "Zebra": "Zebra",
    "Zigzags": "Zigzags"
}

can_files = {
    "Classic": "classic",
    "BW": "bw",
    "Gold": "gold",
    "Negative": "negative",
}

TOTAL_IMAGES = 10000
all_images = [] 

#Functions
def superComposite(list):
	com = Image.alpha_composite(list[0], list[1])
	for i in range(len(list)-2):
		com = Image.alpha_composite(com, list[i+2])
	return com

def create_new_image():
	new_image = {} #

	#Select a random attribute for each propertie
	new_image ["Background"] = random.choices(background, background_weights)[0]
	new_image ["Can"] = random.choices(can, can_weights)[0]

	return new_image

#Generate combinations
for i in range(TOTAL_IMAGES): 
	new_trait_image = create_new_image()
	all_images.append(new_trait_image)

#Add ids to metadata
i = 0
for item in all_images:
	item["tokenId"] = i
	i = i + 1

#Create images
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
	json.dump(all_images, outfile, indent=4)

for item in all_images:
	im1 = Image.open(f'./layers/backgrounds/{background_files[item["Background"]]}.jpg').convert('RGBA')
	im2 = Image.open(f'./layers/creatures/{item["tokenId"]}.jpg').convert('RGBA')
	im2.thumbnail((155,155), Image.ANTIALIAS)
	im1.paste(im2, (424,456))
	im3 = Image.open(f'./layers/cans/{can_files[item["Can"]]}.png').convert('RGBA')

	#Overlay of layers
	COM = superComposite([im1, im3])

	#Save images
	rgb_im = COM.convert('RGB')
	file_name = str(item["tokenId"]) + ".jpg"
	rgb_im.save("./images/" + file_name)
