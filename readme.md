#Mood-Seeker

##Info
> This project is inspired from attending Microsoft's cognitive services API workshop. 
> Our goal is to experiment with the API and come up with something to demonstrate our learning.

The basic idea behind this project is to analyze the average sentiments over a weekly twitter feeds and the average emotion over a weekly of selfie. 

For demonstration purposes, we borrowed Taylor Swift's twitter feeds and images, who is a celebrity known for her expressiveness on twitter and instagram. The images are hardcoded in 'moodnode/public/mood.py'. Her twitter account and feeds can be found in 'moodnode/public/sentiment.py'.

The homepage 'index.html' shows the emotion and sentiment measurements, with respective color for highlights.

##Future implementation & Problem Encountered
We want to create an app that request users to give their permission for accessing photos, then we auto-processed the week of photos, with the addition of user's twitter account. 

Problems encountered are the choice of backend framework. We struggled with choosing the appropriate framework for working with the data, and within limited time we come up with the most feasible solution to use nodejs and cached json files.
