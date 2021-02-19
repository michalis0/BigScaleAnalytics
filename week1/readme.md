# Introduction to cloud services

Welcome to the first BSA lab! In this week, we will give you a brief overview of what cloud-based services can offer. More specifically, we will look into **Microsoft Azure** and **Google Cloud**, two of the most popular cloud services platforms.

## Goals

* Create an account on [Microsoft Azure](https://azure.microsoft.com/en-us/free/students/) and get a student subscription (you will receive a free $100 credit for one year).
* Create an account on [Google Cloud](https://cloud.google.com). **Note**: For that, you will need to enter your credit card information, but you won't be charged. It is just to verify that you are not a bot. You will receive a free $300 credit valid for one year. See also [here](https://edu.google.com/programs/students/?modal_active=none) for classes on Google Cloud for students.
* Do some simple exercises using the cloud.

You are going to use these services all throughout the semester, so make sure that you have created your accounts by the end of the week. After having made an account, try to explore the various features you see in Azure and Google Cloud.

**Highly recommended**: If at any point you feel lost while using these services, we encourage you to look at the documentation provided by [Microsoft](https://docs.microsoft.com/en-us/learn/) and [Google](https://cloud.google.com/docs). They are rich resources that teach you how to use their services, along with numerous code examples.

## Walkthroughs
See files in this Git folder.

## Exercises

### Storage in Google Cloud

* Go to _Storage_ > _Storage_ and create a new bucket.
* Upload a CSV from your laptop (either an existing one or one that you create for that purpose).
* Change the permissions so that the file is readable by everyone (i.e., "Public").
* Access the CSV file from your browser using the public URL.
* Remove the previously set permission.

### Cloud functions
* Go _Compute_ > _Cloud Functions_.
* Create a simple Python function that can be triggered over HTTP.
   * The function should accept one parameter called `company_stock_name` and call the following external API, using that parameter as the value for the `symbol` parameter: https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo. "demo" should be replaced with your own API key, which you can get for free [here](https://www.alphavantage.co/support/#api-key).
   * The function should return the last recorded value of the company's stock.
* Call your function using its URL, trying different values for the company name (MSFT, IBM, ZM, etc.) to make sure it works properly.
