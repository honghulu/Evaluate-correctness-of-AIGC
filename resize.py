import os
from PIL import Image

def getAllFile(filename):
    goodSamples = os.walk(filename)
    
    files = []
    for _, _, fs in goodSamples:
        for f in fs:
            files.append(f)
    return files

def resizeAllFiles(filename, outputDir):
    files = getAllFile(filename)
    for i, file in enumerate(files):
        image = Image.open(filename + '/' + file)
        new_image = image.resize((512, 512))
        new_image.save(outputDir+ '/' + str(i) + '.jpg')

if __name__ == '__main__':
    resizeAllFiles('./goodsample', './resizedSample')