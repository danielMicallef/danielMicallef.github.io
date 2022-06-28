import os
import pathlib

from PIL import Image

def convert_to_webp(source):
	"""
	Convert image to WebP.

	Args:
		source (pathlib.Path): Path to source iamge.

	Returns:
		pathlib.Path: path to new image.
	"""

	dest = source.with_suffix('.webp')
	image = Image.open(source)
	image.save(dest, formate='webp')
	return dest

if __name__ == '__main__':
	root_dir = pathlib.Path(__file__).parent.resolve()
	# blog_img_dir = os.path.join(root_dir, 'assets', 'images', 'blog_images')
	asset_path = os.path.join(root_dir.parent, 'assets', 'images', 'blog_images')
	images = os.listdir(asset_path)
	png_images = [os.path.join(asset_path, image) for image in images if image.endswith('.png')]
	webp_dirs = [convert_to_webp(pathlib.Path(png_image)) for png_image in png_images]

	for image in png_images:
		os.remove(image)

	print(root_dir)