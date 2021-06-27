# AWS-Lambda: Forwarding SNS Message to Telegram Chat

1.  **Create a Telegram Bot:**<br/> 
Search @BotFather in your Telegram App and send the /start command. Then, send the /newbot command and follow a few simple steps to create a new Telegram bot.
BotFather generates an authorization TOKEN for your new bot. This TOKEN is a string that looks like this: 123456789:ABCD1234efgh5678-IJKLM. It is required to send requests to the Telegram Bot API.

2. **Get The Chat ID:**<br/>
In your Telegram app, search the bot that you just created and send the /start command. Then, write any test message to the chat with your bot.
Execute a Bot API call to get the ID of your chat with your bot. (In the following command, replace <token> with the authorization TOKEN that you received from the BotFather.)<br/>NOTE: For Windows user you should use " instead of ' or there may be problems.<br/><br/>
`curl 'https://api.telegram.org/bot<token>/getUpdates' | python -m json.tool`<br/><br/>
In the output, find your test message and the corresponding chat ID. For example, in the following output, the chat ID is 987654321.<br/>
```json
{
  "ok": true,
  "result": [
    {
      "message": {
        "chat": {
          ...
          "id": 987654321,
          ...
        },
        ...
        "message_id": 2,
        "text": "Hello"
      },
      ...
    }
  ]
}
```
3. Open the Amazon SNS Console at https://console.aws.amazon.com/sns/home and create a new SNS topic in the AWS region of your choice.<br/>
  Open the Lambda Management Console at https://console.aws.amazon.com/lambda/home and switch to the same AWS region where you created your SNS topic. Then, create a new Lambda function and paste the code that youfind in this repository (https://github.com/zatarra97/AWS-Lambda-Telegram-Message/blob/main/send_message.py)<br/>
  
4. Set Envirornent Variables: <br/>
  Go to the "configuration" tab and click on "Envirornent Variables", create this two variables:<br/>
Key | Value
--- | -----
CHAT_ID | Your chat_id 
TOKEN | You Telegram Bot Token
  
  
  
  <br/>
  First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column
