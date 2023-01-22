# Cat-Dog-Quote

You ever had money to burn and decided to give it to Amazon Web Services?

Yeah me neither.

But here's a simple project I made to familiarize myself with deploying Django inside a VPC, using EC2, S3 and RDS.

This application runs a single api endpoint at /inspire. When this is called via a GET request, it returns a JSON response consisting of the following components:

timestamp - The timestamp that the server generated the response at
quote - The randomly picked quote from the quote database
cat_pic - The URL of the cat picture
dog_pic - The URL of the dog picture

I have defined a single model in the API app, called Quote, which stores the quote text and quote author. I prepopulated these from my local computer and dumped the mysql database then repopulated my RDS instance with its contents. The dog pic is randomly selected from a S3 bucket I own, and the cat pic is retrieved from The Cat API (https://thecatapi.com/).