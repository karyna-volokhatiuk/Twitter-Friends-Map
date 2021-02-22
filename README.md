# TWITTER-FRIENDS-MAP

TWITTER-FRIENDS-MAP is a program for generating a world map
with location of friends from Twitter.
It has a separated module for navigation through the json-files.

## Installation

To use the program clone the repository
via GitHub (https://github.com/karyna-volokhatiuk/Twitter-Friends-Map.git).

## Usage

After running the program with module 'app.py' from folder 'app'
user should follow the link and input the nickname from Twitter and bearer token there.

![run_app](run_app.png?raw=true'run_app')

If the nickname or bearer token are invalid, html-page with appropriate message will be opened.

![incorrect_input](incorrect_input.png?raw=true'incorrect_input')

![failure](failure.png?raw=true'failure')

If input information is right, the world map with friends' locations will be generated and opened.

![input_data](input_data.png?raw=true'input_data')

![friends_map](friends_map.png?raw=true'friends_map')

To use a separated module for navigation through the json-files user should run 'info_from_json.py'
from folder 'info_from_json' and answwers questions to go to needed information from json file.

## License
[MIT](https://choosealicense.com/licenses/mit/)
