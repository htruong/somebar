# StripBar

Simple indicator for NeoPixel on Arduino inspired by [AnyBar](https://github.com/tonsky/AnyBar) (basically it is a clone of AnyBar)

Tested on Ubuntu 14.10 and Mac OS 10.10

## Install

```sh
sudo python setup.py install
```

## Program your Arduino

Hook up the LED strip to the Arduino and compile & upload the .ino file in the Arduino folder. Change the pin name and number of LEDs as needed.

## Set correct permission for serial device

On Ubuntu and other Linux distributions you might need to set the correct permission for the Arduino device. Simply add your current user to the `dialout` group, then log out and log back in again:

```sh
sudo adduser ${USER} dialout
```

Mac systems seem to have set this right out of the box, so no worries.

## Usage

to run stripbar just execute in console
```sh
stripbar --serialdev /dev/ttyACM0 --numleds 9
```

You can set the brightness for the LED strip as well as the number of LEDs.

For all options try

```sh
stripbar -h
```

stripbar is controlled via UDP port (1738 by default). Send it a message and it will change a color:

```sh
echo -n "red" | nc -4u -w0 localhost 1738
```

Any color recognized by a webbrowser will work.

If you have more than one LED, all the sockets will start listening from the base port (1738) and offset from there. 

And one special command forces somebar to quit: `quit`

