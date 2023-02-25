# TamperMAP

<p align="center">
<img src="https://i.imgur.com/l8gUpXR.jpg" width="75%" height="75%">
</p>

A web verb tampering tool that checks the status code and size of pretty much all HTTP methods for a given URL.

If you don't have access to Burp Suite or other tools like ffuf and you want to test an endpoint for web tampering vulnerability, this tool can help you to do so in the easiest way possible via Python.

___

# *Installation*:

```
git clone https://github.com/undefinedCody/TamperMAP.git

cd TamperMAP/

python3 tampermap.py -u [url]
```

___
# *Usage:*
A valid yet simple example that tests the 9 main HTTP methods:

``` python3 tampermap.py -u https://example.com```

Parameter ``` -u ``` is mandatory and <ins>MUST</ins> have a schema. Works with both *http* and *https*.

</br>

*Optional parameters:*

🔴``` -t / --threads ``` Specify the threads used for testing. Default=5 (Example: --threads 5 )

🔵``` -s / --show ``` Only show results that match the specified HTTP status code(s). (Example: --show 200,301,404)

🔵``` -x / --hide``` Hide results that match the specified HTTP status code(s). (Example: --hide 401,503) 

🟢``` --common ``` Test the 9 common HTTP methods. DEFAULT (Example: --common)

🟢``` --all ``` Test all the available HTTP methods. (Example: --all)

🟠``` -i / --ignore-ssl``` Ignore SSL errors.

🟡``` --save ``` Save the result to a file named result.txt next to tampermap.py file

Options in blue and green <ins>cannot</ins> be used together.

___
# *Additional information:*

```--common``` Includes the following common HTTP methods:

```python
["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]
```

``` --all``` Includes all the HTTP methods available according to [source](https://github.com/for-GET/know-your-http-well/blob/master/methods.md):

```python
["ACL", "BASELINE-CONTROL", "BIND", "CHEKIN", "CHECKOUT", "CONNECT", "COPY", "DELETE", "GET", "HEAD", "LABEL", "LINK", "LOCK", "MERGE", "MKACTIVITY", "MKCALENDAR", "MKCOL", "MKREDIRECTREF", "MKWORKSPACE", "MOVE", "OPTIONS", "ORDERPATH", "PATCH", "POST", "PRI", "PROPFIND", "PROPPATCH", "PUT", "REBIND", "REPORT", "SEARCH", "TRACE", "UNBIND", "UNCHECKOUT", "UNLINK", "UNLOCK", "UPDATE", "UPDATEREDIRECTREF", "VERSION-CONTROL", "GIBBERISH", ""]
```

Please note that the last two methods were added to ensure that targets are being tested properly. Gibberish is an arbitrary non-existent method and the other one is basically empty.

___
# *Changelog:*


**1- Version 0.1 - 02/25/2023:**
- Initial release.

___

# *Todo list:*

- Add an option to hide results that match the specified page size.
- Add an option to take multiple URLs via an external source or a parameter (comma-separated).
- More control over the saved file. (To overwrite or add the current result to existing one).
- Improve stability and fix bugs
- ... You tell me
___

# *Licensing:*

```
Copyright 2023 undefinedCody

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
