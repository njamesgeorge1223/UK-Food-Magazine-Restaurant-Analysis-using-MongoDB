
![72907](https://github.com/njgeorge000158/nosql-challenge/assets/137228821/1d0c380f-f729-49fc-b7b2-7c25c02375a3)

# Eat Safe, Love

In this Challenge, I've been contracted by the editors of a food magazine, Eat Safe, Love, to evaluate ratings data for where to focus future articles; the data comes from the UK Food Standards Agency, which evaluates various establishments across the United Kingdom. 

Due to a request from the magazine's editors, I make some modifications to the data imported into a MongoDB database such as adding information for an exciting new halal restaurant in Greenwich, "Penang Flavours".  The magazine is not interested in any establishments in Dover, so I remove any establishments within the Dover Local Authority from the database and check the number of documents to ensure they are not present.  Some of the values in each MongoDB document such as latitude, longitude, and rating value are text when they should be numbers; to facilitate future inquiry, I appropriately change these data types.

For the analysis, I use my knowledge of Python, PyMongo, and MongoDB to answer specific questions posed by the management and staff of Eat Safe, Love.  Here are the questions and their query results.

1. Which establishments have a hygiene score equal to 20 (the worst possible rating)?
<img width="1105" alt="NoSQLQuery1_1" src="https://github.com/njgeorge000158/nosql-challenge/assets/137228821/2f17fa6b-5c2b-475e-9d37-fe5cee7d2473">

2. Which establishments in London have a high rating value greater than or equal to 4 (1-5)?
<img width="1107" alt="NoSQLQuery2_1" src="https://github.com/njgeorge000158/nosql-challenge/assets/137228821/c4c154d3-7985-40ac-bd29-07afa43e0e8b">

3. What are the top 5 establishments with a rating value of 5, sorted by best hygiene score, nearest to the new restaurant added, "Penang Flavours?
<img width="1106" alt="NoSQLQuery3_1" src="https://github.com/njgeorge000158/nosql-challenge/assets/137228821/40dcf991-fc52-488c-bf7a-17dde0bac8d5">

4. How many establishments in each Local Authority area have a hygiene score of 0 (the best possible rating)? Sort the number of establishments from highest to lowest, and print out the top ten local authority areas.
<img width="1107" alt="NoSQLQuery4" src="https://github.com/njgeorge000158/nosql-challenge/assets/137228821/e5df9c89-b73a-48a6-856c-3b2ba3c09f5b">

From the analysis, there are a number of insightful conclusions.  The locations with the worst hygiene scores are on or near the coastline outside of London. There is a concentration of highly rated restaurants inside the city of London proper. Greenwich is the location with establishments scoring highest in both value and hygiene; for hygiene alone, Thanet is the best location.

----

### Copyright

N. James George © 2023. All Rights Reserved.
