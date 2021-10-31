# Part 1: In this question, you will apply an image filter to each downloaded
# image using multi-processing. Use the glob module to get all downloaded images
# in the current directory with the extension .jpg. Append these images to
# a list called imgs.
# Part 2: Make a note of the process time. Refactor the code so that it is
# using ThreadPoolExecutor instead of ProcessPoolExecutor. Execute the code
# & compare the process time. Note the differences in a comment at the bottom
# of the file.

from concurrent.futures import ProcessPoolExecutor
from glob import glob
from os import chdir
from PIL import Image, ImageFilter # you'll need to install this with pip
from time import perf_counter

def filter_img(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.save(img_name)
    print(f'{img_name} was processed.')

def main():
    start = perf_counter()

    # Get all images in the current directory with the extension .jpg and
    # append to a list (Use images downloaded from q3)

    # Use a context manager, e.g. "with ProcessPoolExecutor() as ex"
    # Call the ex's map method - pass in a function & iterable

    finish = perf_counter()
    
    elapsed_time = round(finish - start, 2)
    
    print(f'Process finished in {elapsed_time} second(s)')

if __name__ == '__main__':
    main()
