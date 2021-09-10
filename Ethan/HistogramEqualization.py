#!/usr/bin/env python

import sys
import os
import re
import numpy as np
from tqdm import tqdm

# Instead of using skimage, I probably should have used open-cv2
from skimage import data, io, exposure, img_as_uint, img_as_float

def main():
    
    path = sys.argv[1]

    regex = re.compile('asteroid_difference_images_([9]+).npz')

    for file in os.listdir(path):
        result = regex.search(file)
        if result is not None:
            outfile = "asteroid_equalized_images_" + result.group(1) + ".npz"
            print(file)
            generate_file(f"{path}/{file}", f"{path}/{outfile}")

        
def generate_file(infile, outfile):
    
    npz_data = np.load(infile)
    print(npz_data.files)
    starAsteroid = npz_data['data']

    # Generate Histogram equalized images

    starAsteroid_float = np.full(starAsteroid.shape, 0, dtype=float)

    num_imgs = starAsteroid.shape[0]
    for i in tqdm(range(num_imgs)):
        image = starAsteroid[i]
        starAsteroid_float[i] = exposure.equalize_hist(image)

    
    np.savez(outfile, data=starAsteroid_float)
    
    
if __name__ == "__main__":
    main()
