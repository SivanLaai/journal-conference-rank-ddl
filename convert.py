from PIL import Image
from argparse import ArgumentParser
 
parser = ArgumentParser(description="conver png to ico")
parser.add_argument("--image_path", type=str, help="image path", default="favicon.png")
args = parser.parse_args()
logo = Image.open(args.image_path)
fileName = args.image_path.split(".")[0] + ".ico"
logo.save(fileName,format='ICO')