# Stripbar: Colorful dots for your computer

Introducing Stripbar - Simple indicator for NeoPixel strips. 

Stripbar is a small indicator for your computer that does one simple thing: it displays colored dots. What the dot means and when to change it is up to you.

Powered by Arduino. Inspired by [AnyBar](https://github.com/tonsky/AnyBar). Works on any platform.

![LED strip](https://github.com/htruong/stripbar/raw/master/IMG_20161128_183947.jpg "LED strip")

## Compability

- Unlike competitors such as AnyBar or somebar, stripbar is cross platform. Tested on Ubuntu 14.10 and Mac OS 10.10. Should work on Windows, too.

- 100% protocol-level compatibility with AnyBar, or your money back!

- As far as I am concerned, this is the real deal, when it comes to color. You can tell it to display any color, unlike AnyBar.

## Hardware

- Arduino or Arduino Pro Micro 5V 16Mhz, I particularly love the Pro Micro because of its size, but you can use whatever. Get it on SparkFun https://www.sparkfun.com/products/12640 or eBay. The $5 version of the Pro Micro works just fine.

- Adafruits NeoPixel RGB LED strips https://www.adafruit.com/product/1138 - you can also get it cheap on eBay or AliExpress.

- A 1000uF-capacitor.

Hook them up as described: https://learn.adafruit.com/adafruit-neopixel-uberguide/basic-connections

## Program your Arduino

- You need to get Arduino board and port set up right, and import Adafruit's neopixel library.

- Change the pin name and number of LEDs as needed.

- Compile & upload the .ino file in the Arduino folder.  

## Set correct permission for serial device

On Ubuntu and other Linux distributions you might need to set the correct permission for the Arduino device. Simply add your current user to the `dialout` group, then log out and log back in again:

```sh
sudo adduser ${USER} dialout
```

Mac systems seem to have set this right out of the box, so no worries.

## Install stripbar

```sh
sudo python setup.py install
```

## Usage

Execute in console

```sh
stripbar --serialdev /dev/ttyACM0 --numleds 9
```

You can set the brightness for the LED strip as well as the number of LEDs.

For all options try

```sh
stripbar -h
```

Stripbar is controlled via UDP port (1738 by default). 

Send it a message and it will change a color:

```sh
echo -n "red" | nc -4u -w0 localhost 1738
```

Any color recognized by a webbrowser will work.

If you have more than one LED, all the sockets will start listening from the base port (1738) and offset from there. So second LED will listen on port 1739 and so on.

And one special command forces stripbar to quit: `quit`

```sh
echo -n "quit" | nc -4u -w0 localhost 1738
```
