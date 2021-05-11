# Getting Started

## Documentation

This module's documentation is hosted on [Gitbook](http://o2ba.gitbook.io/deutschebahn)

## Getting your API token

The first step that you must complete before using the module. To generate an API token, you must first create an account on the [API Portal website](https://developer.deutschebahn.com/). 

Then, create an API. The same is non-significant and so is the Callback URL and Description.

![My Applications page](.gitbook/assets/image%20%281%29.png)

You can then go to My Subscriptions, select your application, and generate keys.

![My Subscriptions page](.gitbook/assets/image%20%282%29.png)

Now, you should have an Access Token, which you will use in Python to authenticate yourself.

In order for the module to work, you need to subscribe to modules you intend to use. To be safe, subscribe to the following modules:

* Betriebsstellen
* StaDa Station Data
* FaSta Station Facilities
* Timetable
* Fahrplan
* Reisezentren

![](.gitbook/assets/image%20%283%29.png)

Now in your Python file, you can initialize the module by using the client.Auth function

```
import deutschebahn as db

db.client.Auth("Your token")
```



