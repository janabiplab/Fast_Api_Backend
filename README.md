# Fast_Api_Backend
<img src=""/>
![image](https://github.com/user-attachments/assets/4698700e-7ea1-4f75-86f3-e7addfc4439b)


### sign up of a user

<pre>
  POST https://fast-api-backend-1-qvp0.onrender.com/signup
</pre>

### body
<pre>
  {
    "username": "biplab",
    "email": "biplab@gmail.com",
    "password": "1234",
  }
</pre>
---
### Login of a user
<pre>
  POST https://fast-api-backend-1-qvp0.onrender.com/signup
</pre>

### body
<pre>
  {
  "username":"biplab",
  "password":"1234"
  }
</pre>
---
###  Send prompt to Replicate
<pre>
   POST https://fast-api-backend-1-qvp0.onrender.com/prompt
</pre>

 -Auth pass token
<pre>
  fd3677e3-6098-4bef-8a6c-ea6a43166e13
</pre>
-body pass prompt
<pre>
  "prompt":"hello"
</pre>
- response
  <pre>
    "response": "Hello! How are you today? Is there something I can help you with or would you like to chat?"
  </pre>

  ---
 ### all user prompts history
 -get history of authenticated user
 <pre>
    POST https://fast-api-backend-1-qvp0.onrender.com/history
 </pre>
 -result
 <pre>
   "biplab": [
    {
      "timestamp": "2025-07-01T14:38:01.183866",
      "prompt": "hello",
      "response": "Hello! How are you today? Is there something I can help you with or would you like to chat?"
    },
    {
      "timestamp": "2025-07-01T14:38:05.180087",
      "prompt": "hello",
      "response": "Hello! How are you today? Is there something I can help you with or would you like to chat?"
    }
  ]
 </pre>
  











