# MedBay-V1 - Ensuring citizen health, Always

# Table of Contents

- [MedBay-V1](#medbay-v1)
- [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Inspiration](#inspiration)
  - [What it does](#what-it-does)
  - [How we built it](#how-we-built-it)
  - [Main features](#main-features)
  - [Tech stack](#tech-stack)
  - [Screenshots](#screenshots)
  - [What's next for MedBay-V1](#whats-next-for-medbay-v1)
  - [Demo](#demo)

## Installation

Clone the project repository

``` bash
# change directory
$ cd MedBay-V1

# Setup Virtual Environment(LINUX)
$ virtualenv venv
$ source venv/bin/activate

# Install requirements
$ pip install -r requirements.txt

# Migrate db File
$ python manage.py makemigrations
$ python manage.py migrate
```

## Usage

```
# Launch server
$ python manage.py runserver

```
## Inspiration

The global COVID-19 pandemic has introduced massive changes in both need and availability of telemedicine and telehealth services. Physicians have increased their use of telemedicine to care for individuals and populations who have difficulty accessing care because of geography, lack of available trained practitioners, or health limitations. If we can provide an application which would help in handling mental fitness, heart-rate monitoring and also a smart chatbot to be aware of symptoms and diseases and doctors needed to consult, then it would be highly beneficiary to the generation especially in this pandemic world. The motivation behind this idea was driven by wellness for the entire society in these times. People fret about their pulse or heartrate considering as a symptom for COVID, they suffer from anxiety or depression. They are unaware or worried about what symptoms would prompt what disease and which doctor to consult. Also a medical platform to order medicines online through a voice based chatbot would benefit the older generation as well. Hence, our application MEDBAY-V1 comes to the rescue providing a one stop for all.


## What it does

WORKOUT PLANNER AND MONITOR Physical activity and exercise have many immediate and long-term health benefits. Most importantly, regular activity can improve your quality of life. A minimum of 30 minutes a day can allow you to enjoy these benefits. So, in our application we have a workout planner that gives you a set of exercises, shows you how to do them and then checks if you are doing them correctly. Our posture detection system will check if you are doing correctly and when the set count gets over, it moves on to the next exercise. Thereby ensuring your fitness and physical health. HEART RATE MONITORING SYSTEM Our application has an unique heart rate monitoring system, which is a non-contact based system to measure Heart Rate using real-time application using camera. Heart Rate (HR) is one of the most important Physiological parameter and a vital indicator of people‘s physiological state. The main principle is to extract heart rate information from facial skin color variation caused by blood circulation to monitor the user’s‘ physiological state Detect face, align and get ROI using facial landmarks Apply band pass filter with fl = 0.8 Hz and fh = 3 Hz, which are 48 and 180 bpm respectively Average color value of ROI in each frame is calculate pushed to a data buffer which is 150 in length FFT the data buffer. The highest peak is Heart rate Amplify color to make the color variation visible AI DIET PLANNER There is a diet planner in our application, which helps our end-users get a customized diet plan for them. There are two part, one which takes in basic user details for profile building, which later will be utilized to connect other users with the similar likes and disliked and they can share their weekly diet plans and commencements. The second part takes in all important metrics like the person’s favorite food, diet, cuisines, nutrients he/she wants their diet to be comprised of, and also about any past medical history or diseases they suffer from. All these inputs are fed into our ML model which accurately forms a diet planner for the user, listing out all the meals with their nutrient value and ratings to the user. Using celery running in the background, the diet planner refreshed weekly giving a diversified option to the users. REALTIME GROUP YOGA POSTURE MONITORING SYSTEM In these difficult times, mental as well as physical health need to be looked into. Hence, our application is at the service with a yoga monitoring system, where multiplayers can join and share their video and audio. A particular yoga posture would be displayed to the users at a time, and the users have to do yoga as displayed in the posture. Our posture detection system would run in the background for each user and score them real-time based on their accurate performance, and finally declare a winner in the end. Thus physical health is monitored as well mental health is maintained by social connection in this unique effort. DEPRESSION CHATBOT In today’s pandemic situation, when everyone is at home, mental health has become an even more important thing to focus on. That is why our application comes with a depression chatbot which serves as the patient’s listener in these time of crisis. And using our NLP Sentiment analysis models trained in the backend on TensorFlow, it supports and cheers the person up person based on all the conditions they have mentioned. It suggests some appropriate quotes about life, love and family. It also suggests some songs that can uplift user moods and help get over the hard times. Hence, it reduces the mental stress or worry a person goes through especially on low days. WORKOUT PLANNER AND POSTURE DETECTOR In today’s pandemic situation, when everyone is at home, physical health has also become an important aspect to focus on. Thus our workout planner comes with a posture detector where certain exercise poses are taught to the user, and they have to try their best to attain that pose. There is a unique timer attached with each pose maintaining the exercise duration which has to be completed before going to the next exercise. There is also a scoring system based on the posture detection system running in real-time in the background. MEDICAL CHATBOT The application comes with a chatbot MEDBOT, which serves as the patient’s listener in these time of crisis. Any person can chat with our chatbot describing about their current state of body and what they are suffering from, mental or physical. Our chatbot comes to their assist, asks them counter questions about their exact symptoms or feelings they are undergoing. And using ML and NLP models trained in the backend, it predicts the disease for the person based on all the symptoms they have mentioned. Our chatbot also predicts type of doctor to consult for the disease. Hence, it reduces the hassle or worry a person goes through while thinking about which hospital or which doctor to consult for his symptoms. MEDICAL TEST COMPARISON There is often a variety of prices for medical tests offered by different hospitals. People are confused and do not get a clear comparison statistic of the medical tests. Hence, MEDBAY has a unique section in the patient portal where users can search for their desired medical test. It would enlist all the hospitals where the tests are available and lists them in increasing order of price. Thus, users can get a clearer insight. PHARMACEUTICAL STORE MEDBAY has a linked up pharmacy store where, allopathy, homeopathy as well as ayurvedic medicines are available and any user can buy from. It has integrated STRIPE payment gateway for smooth checkout. It has home delivery system which would really help the older generation. It connects medicine from local pharmacy stores based on geolocation, hence reducing the delivery price to minimum.


## How we built it 

Made in Django Powered by superior quality design, to intrigue users. The frontend is mainly made on full bootstrap and Night owl CDN and Bulma, providing state of the art UI. We have tried to keep the UI/UX transitions as much smooth and user friendly as possible. We decided to use Django as the core of our application as it is powered by Python. All the work is done on the very latest Django version and Python 3.7.3 . Python enabled us to use all the machine learning and recommendation technology to its full potential. The Django model gives us a total boost by letting us easily override the BASE USER model. The chatbot is a state of the art model trained via RASA NLU It is capable of differentiating between the different user Intent, which then serves as an input to the various Machine and Deep Learning Algorithms to Predict the various Diseases, Drugs and Doctors from our Database. Also we have implemented a Diet Planner System, which initially takes all the inputs from the users and then trains on an intricate machine learning model achieved by ensemble learning algorithms. These algorithms predict the exact diet plan for an entire week or month based on the users choice. It also is connected to our database, from where it estimates the different ingredients used, and the calories. The diet prediction algorithm, automatically runs every 7 days, by celery. It triggers an automatic notification to the users to re feed the data, if any changes are detected in their personal taste and body mass indexing. It is a very powerful system, which can be extended to various domains. It also amounts the total calories that will be consumed by the user for the particular recommendation, by feeding the items recommended into another Machine Learning Model. Thus, this system enables a remote diet system, which predicts accurately, keeping in mind the health and well being of all our users and the entire society. Our depression chatbot runs on trained sentiment analysis model and also has a recommender database having a collection of quotes and songs. Predicting the sentiment of the user, the chatbot recommends some songs and likely quotes to uplift the user’s mood. Uses GTTS module to pass in the chatbot response and output it in a soothing female voice, to uplift user mood instantly. The yoga posture detector and exercise planner makes use of real time posture detection system using Tensorflow PosNet. The video of the users are monitored and analyzed in real time generating a score metric for each measure based on accuracy of the moves or postures of the person. There is also a timer and counter to keep track of the duration and repetitions of each exercise the person is doing. The heart rate monitoring system is achieved by : Detect face, align and get ROI using facial landmarks Apply band pass filter with fl = 0.8 Hz and fh = 3 Hz, which are 48 and 180 bpm respectively. Average color value of ROI in each frame is calculate pushed to a data buffer which is 150 in length. FFT the data buffer. The highest peak is Heart rate Amplify color to make the color variation visible. The yoga application makes use of real time posture detection system. Tensorflow PosNet is used for posture detection. The video of the users are monitored and analyzed in real time generating a score metric for each measure based on accuracy of the moves or postures of the person playing the yoga game. That score metric is then used in the end to declare the winner with the maximum score. The E-Tests provides recommendation to users based on various cost factors and hospital locations, providing a detailed and accurate comparisons, helping the users to choose the best. MEDBAY has a linked up pharmacy store where, allopathy, homeopathy as well as ayurvedic medicines are available and any user can buy from. It has integrated STRIPE payment gateway for smooth checkout. It has home delivery system which would really help the older generation. It connects medicine from local pharmacy stores based on geolocation, hence reducing the delivery price to minimum.


## Main features

	1. Multi Authentication via face-recognition
	2. WORKOUT PLANNER AND MONITOR
	3. HEART RATE MONITORING SYSTEM
	4. AI DIET PLANNER 
	5. AI DRUG RECOMMENDER 
	6. REALTIME GROUP YOGA POSTURE MONITORING SYSTEM
	7. DEPRESSION CHATBOT
	8. WORKOUT PLANNER AND POSTURE DETECTOR
	9. MEDICAL CHATBOT
	10.MEDICAL TEST COMPARISON
	11.PHARMACEUTICAL STORE AYURMED
	12.Stripe Payment
	13.AI AUTOMATED ADDITION TO CART
	14.FOOD REVIEWS VIA SENTIMENT ANALYSIS & GENETIC RANKING ALGORITHM
	15.Recommender ranking top medicine distributing facilities
	16.Genetic algorithm ranking the mediicine facilities 
	17.Genetic algorithm for ranking uses location, reviews, availability and price
	18.Auto cart addition via voice based chatbot
	19.Product quantity and price enquiry via the voice based chatbot

## Tech stack

- Weavy Django 
- RASA NLU 
- HTML, CSS, JavaScript 
- Machine Learning Algorithms 
- Random Forest, Naïve Bayes Classifier 
- Deep Learning 
- Posture Detection Algorithms 
- FFT and Band filtering techniques 
- NLP Sentiment Analysis Model 
- GTTS module
- STRIPE
- Celery
- Google Geolocation 
- Python ML,DL libraries 
- Bootstrap, Ajax, jQuery etc.

## Screenshots



## What's next for MedBay-V1

 - Integrating different languages into our chatbots to provide even a better user experience and adding all our ideated modules to the main application. 
 - Adding a IoT device like Fitbit to our heart rate monitoring system application Provide a detailed yoga plan recommendation Adding customer feedback portal in the e-test comparison application
 - Integration of local languages to our product and expand our products to several more local medicine distributors for better user experience and wider reach out.
 - Make our chatbot robust to handle more complex enquiry or product detail enquiry
 - Include a voice based assitant to navigate the entire application

## Demo

https://youtu.be/BzWEbHi-c3Q
