## Implementation approach
We will use the Flask framework to build the backend of the WeChat mini app. Flask is a lightweight and flexible Python web framework that is suitable for small to medium projects. For the daily fortune prediction algorithm, we will use the AstroPy library, which is a powerful open-source software for astronomy. We will use the WeChat API for sending notifications and sharing on social media. The user interface will be built with HTML, CSS, and JavaScript. 

## Python package name
```python
"wechat_fortune"
```

## File list
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

## Data structures and interface definitions
```mermaid
classDiagram
    class User{
        +str wechat_id
        +str name
        +str birth_date
        +list history
        +__init__(wechat_id: str, name: str, birth_date: str)
        +get_history()
        +add_to_history(prediction: str)
    }
    class Prediction{
        +str date
        +str prediction
        +__init__(date: str, prediction: str)
    }
    class Notification{
        +str wechat_id
        +str message
        +__init__(wechat_id: str, message: str)
        +send()
    }
    User "1" -- "*" Prediction: has
    User "1" -- "*" Notification: receives
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant U as User
    participant P as Prediction
    participant N as Notification
    M->>U: create user
    U->>M: return user
    M->>P: create prediction
    P->>M: return prediction
    M->>U: add prediction to user history
    M->>N: create notification
    N->>M: send notification
    M->>U: update user
```

## Anything UNCLEAR
The requirement is clear to me. However, the actual implementation may require further clarification on the specific requirements of the WeChat API, as well as the details of the prediction algorithm.