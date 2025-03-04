from PIL import Image
from os import listdir
from os.path import isfile, join
import shutil
import getpass

cur_user = getpass.getuser()
opth = f'C:/Users/{cur_user}/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'
wp = f'C:/Users/{cur_user}/Pictures/Wallpapers/'

def copyChangeWallpapers():

	orig_wall = listdir(opth)

	for f in orig_wall:
		cur_f_p = join(opth,f)
		if isfile(cur_f_p):
			f_w_ext = f + '.jpg'
			im = Image.open(cur_f_p)
			width, height = im.size
			# will only copy FHD and larger images
			if width >= 1920:
				shutil.copyfile(cur_f_p, join(wp, f_w_ext))

copyChangeWallpapers()