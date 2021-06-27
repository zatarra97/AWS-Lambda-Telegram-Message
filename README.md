# AWS-Lambda: Forwarding SNS Message to Telegram Chat

1.  **Create a Telegram Bot:**<br/> 
Search @BotFather in your Telegram App and send the /start command. Then, send the /newbot command and follow a few simple steps to create a new Telegram bot.
BotFather generates an authorization TOKEN for your new bot. This TOKEN is a string that looks like this: 123456789:ABCD1234efgh5678-IJKLM. It is required to send requests to the Telegram Bot API.

2. **Get The Chat ID:**<br/>
In your Telegram app, search the bot that you just created and send the /start command. Then, write any test message to the chat with your bot.
Execute a Bot API call to get the ID of your chat with your bot. (In the following command, replace <token> with the authorization TOKEN that you received from the BotFather.)<br/>
`curl 'https://api.telegram.org/bot<token>/getUpdates' | python -m json.tool`<br/>
In the output, find your test message and the corresponding chat ID. For example, in the following output, the chat ID is 987654321.<br/><br/>
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
