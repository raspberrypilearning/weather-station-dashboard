# The Scratch Weather Dashboard

In this resource, you will be creating a basic weather dashboard, to monitor the weather at stations all over the world.

## Fetching the interface.py file

For Scratch to be able to talk to weather stations around the world, it needs a little help. There's a complicated Python script that you can run, that will help Scratch chat to weather stations.

1. Open up a terminal, by pressing the `ctrl`, `alt` and `t` keys all at the same time, or by clicking on the icon in the left hand corner of the screen.

1. Into the terminal type the following command to get the Python file.

	```bash
	 wget -O interface.py https://raw.githubusercontent.com/raspberrypilearning/scratching-the-weather/master/code/interface.py?token=AETp8m9CBcAxVOOTmuLO7X9K7cXqPRcrks5YQZB_wA%3D%3D
	```
- note get shortened URL off BEN

1. That's it, you have downloaded the file. Keep the terminal open though, as you'll need it in a minute.

## Setting up Scratch

Now we need to help Scratch talk to the file you have downloaded.

1. Open up Scratch by clicking on `Menu` > `Programming` > `Scratch`

1. Once Scratch opens, you need to enable `remote sensors`. Click on the `sensing` button to reveal the `sensing blocks`

	![](images/sensing.png)

1. Now find the block called `slider sensor value` and right click on it. Click on `enable remote sensor connections`

![](images/enable.png)

## Starting your Python script

1. Now that Scratch can talk to Python, you need to start the Python script so that it can fetch lots of weather station data and send it to Scratch.

1. Go back to the terminal, and type the following:

```bash
python3 interface.py
```

## Getting data from a Weather Station

1. If you have your own weather station at your school, ask your teacher for the weather station's `id`. If you don't then you can use the `id` in the code below.

1. The first step is simple. You can make the Scratch cat tell you the weather for any particular weather station you like. First grab a `when green flag clicked` block.

	![](images/cat-1.png)

1. Then click on `Variables` and then `Make a variable`. Call it `id`.

	![](images/variable.png)

1. Once you have created the variable, you can set it to your weather station's id or use `490722`

	![](images/cat-2.png)

1. Now if you go back to the `Sensing` menu in Scratch, and find the the `slider sensor value` block, you should see there is a little black arrow that points downwards, next to the word `slider`. Click this menu and you can change the sensor value to lots of different things.

	![](images/menu.png)

1. To start off with, you can choose `air_pressure`, and then use a `say` block so that the cat will tell you the air pressure at the weather station.

	![](images/cat-final.png)
	
## Playing around with the sensors.

1. Have a play around with different sensor values to see what they do, and what readings they produce.

1. If you like, you could use `join` blocks to also get the cat to tell you more than one sensor value.

	![](images/cat-extension.png)
	
## What Next?

1. In the [next worksheet](worksheet2.md) you will learn how to produce a graphical dashboard, to show you the weather at your station using images and animations.
