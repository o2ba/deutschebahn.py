---
description: >-
  The following will document the functions, objects and methods associated with
  oPoint / Betriebsstellen API.
---

# oPoint / Betriebsstellen

{% hint style="info" %}
Note that oPoint is simply a adaptation for the Betriebsstellen name the is instead used by the Deutsche Bahn API.
{% endhint %}

## Functions

### get\_oPoints\_by\_name

```text
get_oPoints_by_name(search_string: str, return_http_code=False) -> list or int
```

This function will return a list of oPoint objects matching a given string.

Parameters

* _search\_string:_ String to search
* _return\_http\_code \[Optional\]:_ False by default. Enabling this will return the HTTP status code if it's not 200, rather than returning an empty list.  

{% tabs %}
{% tab title="Return if success" %}
a list of oPoint objects
{% endtab %}

{% tab title="Return if fail" %}
If _return_\__http\_code_ is False, it will return an empty list. \[default\]

If _return_\__http\_code_ is True, it will return an HTTP status code if it's not 200.
{% endtab %}
{% endtabs %}

### get\_oPoint\_by\_ril100

```text
def get_oPoint_by_ril100(ril100: str, return_http_code=False) -> list or int
```

This function will search for an operating station by ril100 code

Parameters

* _ril100:_ ril100 code
* _return\_http\_code \[Optional\]:_ False by default. Enabling this will return the HTTP status code if it's not 200, rather than returning an empty list.  

{% tabs %}
{% tab title="Return if success" %}
an oPoint object
{% endtab %}

{% tab title="Return if fail" %}
If _return_\__http\_code_ is False, it will return an empty list. \[default\]

If _return_\__http\_code_ is True, it will return an HTTP status code if it's not 200.
{% endtab %}
{% endtabs %}

