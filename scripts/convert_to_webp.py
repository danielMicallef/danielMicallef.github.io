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

	import pdb

	pdb.set_trace()
	print(root_dir)