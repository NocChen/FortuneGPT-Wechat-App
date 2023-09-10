## Required Python third-party packages
```python
"""
flask==1.1.2
bcrypt==3.2.0
astropy==4.2
wechatpy==1.8.15
"""
```

## Required Other language third-party packages
```python
"""
No third-party packages required.
"""
```

## Full API spec
```python
"""
openapi: 3.0.0
info:
  title: WeChat Fortune API
  version: 1.0.0
paths:
  /users:
    post:
      summary: Create a new user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                wechat_id:
                  type: string
                name:
                  type: string
                birth_date:
                  type: string
      responses:
        '200':
          description: User created
  /predictions:
    post:
      summary: Create a new prediction
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                date:
                  type: string
                prediction:
                  type: string
      responses:
        '200':
          description: Prediction created
  /notifications:
    post:
      summary: Send a notification
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                wechat_id:
                  type: string
                message:
                  type: string
      responses:
        '200':
          description: Notification sent
"""
```

## Logic Analysis
```python
[
    ("main.py", "Contains the main entry of the application, should initialize Flask app and routes."),
    ("prediction.py", "Implements the prediction algorithm using AstroPy, should be done after main.py to ensure Flask app is initialized."),
    ("notification.py", "Implements the notification sending functionality using WeChat API, should be done after main.py to ensure Flask app is initialized."),
    ("history.py", "Manages user's prediction history, should be done after main.py and prediction.py."),
    ("share.py", "Implements the sharing functionality using WeChat API, should be done after main.py to ensure Flask app is initialized."),
    ("templates/index.html", "Contains the HTML structure of the user interface, should be done after all Python files to ensure all functionalities are implemented."),
    ("static/css/main.css", "Contains the CSS styles of the user interface, should be done after templates/index.html to ensure the HTML structure is finalized."),
    ("static/js/main.js", "Contains the JavaScript scripts of the user interface, should be done after templates/index.html and static/css/main.css to ensure the HTML structure and CSS styles are finalized.")
]
```

## Task list
```python
[
    "main.py",
    "prediction.py",
    "notification.py",
    "history.py",
    "share.py",
    "templates/index.html",
    "static/css/main.css",
    "static/js/main.js"
]
```

## Shared Knowledge
```python
"""
'prediction.py' contains the prediction algorithm using AstroPy.
'notification.py' uses the WeChat API to send notifications.
'history.py' manages the user's prediction history.
'share.py' uses the WeChat API to implement the sharing functionality.
'templates/index.html', 'static/css/main.css', and 'static/js/main.js' together form the user interface of the WeChat mini app.
"""
```

## Anything UNCLEAR
The specific requirements of the WeChat API and the details of the prediction algorithm need further clarification. Also, we need to ensure that all third-party libraries are properly initialized.