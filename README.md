# it3038c-scripts
```bash
PROJECT 2
```
I expanded on my original calculator to make one with more features. This calculator can do addition, subtraction, multiplication, and division. 
To run the script you will have to first enter the C:\it3038c-scripts/ directory and run 
```python
python python/calculator.py
```
After running the script you will enter either +, -, *, or / depending on what you want the calculator to do. You will then press enter, select your fist number, 
and press enter again. Then, after entering your second number and pressing enter the script will calculate your two numbers. I used the link for a python calculator from Lab 1 as a resource. 


```bash 
LAB 7
```
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
