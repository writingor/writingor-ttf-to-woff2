# Writingor TTF to WOFF2

Are you tired of setting up complicated Webpack configurations to convert old .ttf fonts (like those downloaded from Google Fonts) into modern .woff2 format? 

Do you want a quicker, simpler solution without relying on "free" online services that are often limited and slow?

Here’s the solution!

This small Python script works fast and efficiently!

## Usage

1. Place the script `writingor-ttf-to-woff2.py` in the directory with your .ttf files.
2. Run the script using the following command:

```
python3 writingor-ttf-to-woff2.py
```

## Notes

Ensure that you have `pip3` installed on your system. If not, install it with:

```
sudo apt install python3-pip
```

This script uses the `fontTools` library, which is typically included with Python 3. It should already be available in `/usr/lib/python3/dist-packages`. However, if needed, you can manually install the required dependencies by running:

```
pip3 install -r requirements.txt
```
