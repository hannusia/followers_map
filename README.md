# followers_map
<a href="https://twitter.com"><img src="https://img.icons8.com/color/48/000000/twitter--v1.png"/></a>
# Followers map
This application gives an opportunity to see a location of user's friends on Twitter

## How to use the application
1. Download all files
2. Start application.py
3. Enter a username and BEARER-TOKEN in the input fields
4. Tap on "Submit"

## Modules
* application.py - 'frontend part' - cretes site with flask library to input username and token, and to show generated map
* get_friends.py - gets nicknames and locations of given user's followers; this module uses information from Twitter API
* get_map.py - generates map with markers on followers locations, which the site will show

## Templates
* index.html - main screen, where user should enter name of account
* failure.html - screen with error, when user with this name isn't exist or hasn't friends with location or another error appears
* layout.html - template for previous two screens

## Example of working program
![screenshot1](https://user-images.githubusercontent.com/71673095/109715621-8de33080-7bac-11eb-8be4-70f61a7a31bc.png)
![screenshot2](https://user-images.githubusercontent.com/71673095/109715627-90458a80-7bac-11eb-8f07-833893c2e2be.png)

## Module parse.json.py
This module does not connect to the previous program. It just helps to navigate through json-file.
