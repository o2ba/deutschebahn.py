---
description: >-
  Welcome to deutschebahn.py's module documentation. The following is a basic
  guide on how to get started with this API(s) Wrapper.
---

# Getting Started

## Deutsche Bahn's APIs

Deutsche Bahn provides a collection of APIs made to the public with little barrier to entry, but unfortunately they are poorly documented, which means that in the creation of this API, I've had to try and infer as much information as I could from the information made available in English and German. Please understand that this may not be entirely accurate.

This module wraps a couple of the APIs in to one module, and tries to the best extent to make them interact with each other, but it's important to understand how the APIs are different from each other.

### Betriebsstellen API 

{% hint style="info" %}
Rate limit: 10 requests per minute
{% endhint %}

Betriebsstellen \(operation point, oPoint in the module\) is an API provided by DBOpenData that allows you to get basic information about operating points in Germany

#### What qualifies as an operating point?

Operating points consist of not just train stations, but also depots and platforms, and other niche areas on the tracks. This API will also return operating points outside of Germany \(but only within Europe\), but they mainly, and almost exclusively consist of major stations.

There's a comprehensive but not exhaustive [Wikipedia page](https://en.wikipedia.org/wiki/Railway_station_types_in_Germany) detailing the types of railway stations \(equivalent to operating points\). 

### StaDa-Station\_Data API

{% hint style="info" %}
Rate limit: 100 requests per minute, but this module allows you to store every service center and station locally, allowing you to have unlimited requests in practice. Please check the StaDa documentation for more information
{% endhint %}

StaDa-Station\_Data API provides detailed information on stations that run on major and medium importance lines, but also on service centers. In the module, stations gathered form this API will be Station objects, which allows you to use other APIs, and provides a lot of functionality. This API also allows wildcards and advanced search.

### Timetables \(Not in the module yet\)

{% hint style="info" %}
Rate limit: 20 requests per minute
{% endhint %}

This module allows you to retrieve timetable information for certain stations. This returns an XML response that is converted in to JSON, which is then further converted to a list of trip objects, sorted by time.

## Getting your API token

The first step that you must complete before using the module

```
$ give me super-powers
```

{% hint style="info" %}
 Super-powers are granted randomly so please submit an issue if you're not happy with yours.
{% endhint %}

Once you're strong enough, save the world:

{% code title="hello.sh" %}
```bash
# Ain't no code for that yet, sorry
echo 'You got to trust me on this, I saved the world'
```
{% endcode %}



