# SafeNet

![](https://cdn.discordapp.com/attachments/1010348308587348088/1015399109261279282/unknown.png)


## Impressions on the Prompt

First, I would like to give you guys an idea about what went through my mind when I first saw the themes. The prompt that caught my attention was the one titled communication. Now, communication is a very broad word so there were a lot of things I could work on. So, the first thing I did was search up the word “communication” on Google.  The definition that caught my eye was this one: “the successful conveying or sharing of ideas and feelings.” Now, I knew that if I create a system, which can transmit useful information in real-time, I should be good to go. I didn’t want to do something very traditional and boring like creating a discord bot, chat application or calendar. I wanted to do something different and impactful. And after some brainstorming, I finally found a very important problem I could solve.

## The Problem

I would like to spend some time talking about the problem I am tackling and its importance.  The problem I am trying to solve is the reporting of crime. The way crime is currently reported goes something like this:
* The crime happens. 
* Someone notices that a crime has occurred. 
* The person calls 911 to report it to the police. 
* The police arrive and start the investigation.

This process is very inefficient. In most cases, crimes are reported when the damage has already been done and the culprits have gotten away. This is especially prevalent in cases of assault, incest, and murder. The victim in such cases does not have means to call for help. And by the time someone else informs authorities, it’s too late.


## The Solution

This is where “SafeNet” comes in. SafeNet a real-time monitoring system which monitors CCTV feeds in real time and alerts the nearest police station if anything out of the ordinary is detected. It uses Machine Learning (specifically a Convolutional Neural Network) to process CCTV video feeds and make predictions on the current state of the video feed.

If the Neural Network detects that something wrong is going on, a docker container running on Hop’s ignite platform alerts the nearest police station along with information like the address of the crime. This allows the authorities to react to these problems without having to wait for someone to report the crimes.

## How it was made

I used a lot of frameworks and libraries to make this project easy to use and powerful. The ML model was trained using TensorFlow using the DenseNet architecture. I use OpenCV for image processing and numpy for some basic mathematics. The frontend is powered by streamlit. Streamlit made it easy for me to connect the ML model to a sleek and modern frontend. But most importantly, I used Hop to power the system that sends the alerts. I created a Docker Image loaded with FastApi to create a Rest API powered by Hop’s ignite service. 


