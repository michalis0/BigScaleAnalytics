# Introduction to Cloud Services

## Goals:

- Create an account at Microsoft Azure
- Create an account in [Google Cloud](https://cloud.google.com). **Note:** For that you will need to put in your credit card but you won't be charged. It's just to verify that you are not a bot. You will get $300 credit for free which you can use for 90 days.
- Do some simple exercises using the Cloud

In this week we are going to have a brief overview of what cloud based services are. Specifically, we will look into Microsoft Azure, one of the most used cloud services, and get to know many services that Azure provides. Later on, we want you to create an account on MS Azure and register for a student subscription. You will get a 100$ credit for one year with the student subscription.

We are going to use MS Azure throughout the semester, so make sure that you make an account and get the student subscription at the end of this week. Once you make an account, try to explore the different features you see in the Azure portal, which is basically a user interface.

**Highly recommended: We incourage you to check https://docs.microsoft.com/en-us/learn/ , it is a rich resource to learn how to use different services in MS Azure**


## Walkthroughs & Exercises:

- **Storage Bucket in Google Cloud:** Go to storage; create a bucket; upload a CSV from your laptop; change the reading permissions so that it's accessible from everyrone (Public); access the csv file from the browser; change back the permissions.

- **Create a simple cloud function:** Go to Google Cloud Dashboard; Compute>Cloud Functions; Create a simple function in python that accepts one parameter called `company_stock_name` and calls the external API using that parameter in the value of the parameter symbol:
`https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo`
Return the result of that call with the value for the stock of the company (eg MSFT, ZM, etc)
