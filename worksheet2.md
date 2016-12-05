# The Scratch Weather Dashboard

In this next worksheet you will learn how to display some weather data visually, producing a Weather Dashboard. You'll want to start a new Scratch file and enable the remote sensors, just like you did in the first [worksheet](worksheet.md).

## Choosing a forecaster

The first thing you'll want to do is to choose a weather forecaster, who will be telling the viewers what the weather is like. Weather forecasters are often called meteorologists.

1. Choose a new sprite by clicking on the middle button as shown below:

	![](images/new-sprite.png)

1. Choose any sprite you like. Here we've gone for the `squaregirl` image:

![](images/square-girl.png)

## Your forecaster script

1. You can start off by making your weather forecaster set the `id` of the Weather Station you'll be using:

	![](images/set-id.png)

1. She'll then need to say a little bit about the location of the weather forecast. Use a `join` block within a `say` block to begin with, just like you did in [worksheet one](worksheet.md):

	![](images/forecaster-1.png)

1. Now grab two more `join` blocks. In the right-hand side of one, you can place the `town` the weather forecast is coming from. In the left-hand side of the other, you can place the `country` of the weather forecast:

	![](images/forecaster-2.png)

1. Now the two `join` blocks can be placed together. It may not be obvious in the image, but you should add a single space character between the two `sensor values`:

	![](images/forecaster-3.png)

1. With that done, you can place all three `join` blocks together into the `say` block:

	![](images/forecaster-final.png)

1. Your forecaster is now finished. Next, you can add some graphical elements to help users visualise the weather.

## A weathervane

1. Next, you can make a weathervane. Weathervanes show the direction of the wind, but yours is also going to visualise the speed of the wind.

1. Click on the `New Sprite` button to choose another sprite:

	![](images/new-sprite.png)

1. In `things` you should see a `Clock-hand` which is basically just an arrow. Import this sprite and delete any scripts that come with it:

![](images/clock.png)

1. When your weather forecast begins, you'll need to set the size and direction that the arrow points:

	![](images/arrow-1.png)

1. In `Motion` you should see a `turn clockwise __ degrees` block. Add this to the bottom of the script. Then choose the `wind_direction` sensor value, and add this block in:

	![](images/arrow-2.png)

1. To visualise the wind speed, you can change the size of the arrow. Find the `change size by __` block and add this to your script:

	![](images/arrow-3.png)

1. To finish off, find the `__ * __` block in `Operators` and use it to multiply the `wind_speed` by `10`. You can choose a different number if you like, though:

	![](images/arrow-4.png)

1. This can then be added into the `change size by __` block:

	![](images/arrow-final.png)

## Adding a thermometer

1. Next, you're going to produce a working thermometer. You'll need a graphic to represent it, and the one below should be good enough. You can get a large version of it [here](images/therm-sprite.png).

	![](images/therm-sprite-small.png)

1. Import this sprite into your Scratch program. You'll need to place this sprite in a very particular place, so it's best to add this into the script. You're also going to use the pen tool to draw the mercury inside the thermometer, but because you can't draw over the top of Sprites, you need to stamp the Sprite's image to the canvas first, and then hide it. This is the only script you'll need on the thermometer:

	![](images/thermometer.png)

You'll notice the `broadcast` at the end. This is going to be used to tell the pen to start filling in the mercury inside the thermometer.

## Drawing the mercury

1. Now you're going to need a new and very tiny sprite. Click on the leftmost button in the `New Sprite` menu:

	![](images/new-sprite.png)

1. All you need is a single white dot in the middle of the screen:

	![](images/canvas.png)

1. Now you're going to get this tiny pixel to draw a red line of mercury inside the thermometer. When the pixel receives a message to draw, it needs to set up its pen:

	![](images/pixel-1.png)

1. How the mercury is drawn will depend on whether the temperature is higher or lower than `0`. You write the code for temperatures above `0` first:

	![](images/pixel-2.png)
	
1. The first thing to do is to make the pen go all the way to the bottom of the thermometer, and for the pen to be placed `down` on the canvas:

	![](images/pixel-3.png)

1. Next, the pen can move up to the `0` degrees mark on the thermometer:

	![](images/pixel-4.png)
	
1. Then, depending on the temperature, the pen can move upwards on the `y` axis. You might want to tweak the values a little, but 1.7 pixels per degree seems to work fairly well:

	![](images/pixel-5.png)

1. If the temperature is below zero, the pen needs to move to the `-30` degree mark:

	![](images/pixel-6.png)

1. Then the pen needs to again move in the `y` direction. This can be achieved using a little bit of maths:

	![](images/pixel-7.png)
	
1. The pen can then be placed into the finished script:

	![](images/pixel-8.png)

## What next?
In [worksheet three](worksheet3.md) you'll learn how to fetch the weather from more than one Weather Station, giving you a global weather dashboard.
