from twilio.rest import Client
accountSid = "ACaa3347d26965e518ac905c4b7199095e"
authToken = "48d134d5473e93b558aabde8d4df8a18"
twilioClient = Client(accountSid, authToken)
myTwilioNumber = "+12512201736"
destCellPhone = "+918639142835"
myMessage = twilioClient.messages.create(body="body",from_=myTwilioNumber, to=destCellPhone)
