# it3038c-scripts
I used the plugin Pillow. To start, create a virtual environment, activate it, and install pillow with the following commands
```bash
virtualenv ~/venv/pillow
source ~/venv/pillow/bin/activate
pip3 install pillow
```
After finding an image and downloading it to the hard drive, run this code 
```python
python3
from PIL import Image,ImageFilter
myImage = Image.open('/home/cechuser/Desktop/bird.jpg')
myImage.load
```
You can then use these commands to blur, create thumbnail, or apply a filter to the image
```python
myImage.BLUR
myImage.thumbnail((90,90))
myImage.MinFilter
```
To apply the filter and show it run
```python
blur = myImage.filter(ImageFilter(BLUR)).show()
```
Make sure to quit out of python and deactivate the virtual environment with
```python
quit()
deactivate
```
