# Gift of Games Picker for Reddit

An utility (and a bot, too!) that picks the winner of [r/GiftofGames](https://www.reddit.com/r/GiftofGames) drawings in accordance with the subreddit's [rules](https://www.reddit.com/r/GiftofGames/wiki/rules). The latest release is sluggish but works more often than not. The script uses [random.org](https://www.random.org/)'s API to select the winner.

The GoG Picker works with Steam giveaways only.

As of now, the picker does not implement any throttling, so APIs query limits can be easily exceeded. Please keep this in mind! In the future, cache may be implemented to improve execution time.

# Covered rules

The GoG Picker covers only a small subset of the subreddit rules, but large enough to pick a winner and save you some tedious work.

* a link to Steam profile was provided
* the link leads to an existing profile
* the profile is public
* the profile is level 2 or above
* games list is public
* a Redditor has 300 comment karma or more
* the thread title contains required keywords

# Usage

The GoG Picker requires Python 3.6+ installed on your PC. To install the necessary dependencies, execute the following on the command line:

```
pip install -r requirements.txt
```

You will need Steam, Reddit, and Random.org API keys. Check [the configuration section](#configuration) for more details. 

You can access help screen by running the script with `-h` (`--help`) flag.

## Single winner

The script is intended to be invoked from a [CLI](https://en.wikipedia.org/wiki/Command-line_interface). By running it with `-u` (`--url`) parameter you can pick a winner of a single drawing:

```
$ python picker.py --url URL
```

`URL` is a link to a r/GiftofGames thread like this one: `https://www.reddit.com/r/GiftofGames/comments/9n7ywa/offersteam_n/`.

## Multiple winners

The script can handle drawings with multiple winners by running it with `-n` (`--number`) parameter. The following line would run the script and pick 2 winners in the aforementioned thread:

```
$ python picker.py -u https://www.reddit.com/r/GiftofGames/comments/9n7ywa/offersteam_n/ -n 2
``` 
 
Passing `-r` (`--replacement`) flag makes it possible for users to win multiple times:

```
$ python picker.py -u https://www.reddit.com/r/GiftofGames/comments/9n7ywa/offersteam_n/ -n 2 -r 
``` 

Using `-a` (`--all`) flag *ensures* that every user wins at least once (given that there are more games to giveaway than participants):

```
$ python picker.py -u https://www.reddit.com/r/GiftofGames/comments/9n7ywa/offersteam_n/ -n 2 -a 
``` 

It can be combined with `-r` flag so that every user wins multiple times (but at least once):

```
$ python picker.py -u https://www.reddit.com/r/GiftofGames/comments/9n7ywa/offersteam_n/ -n 2 -ra
``` 

## Bot
When the script is invoked without the optional `url` parameter, it acts like a bot and fetches the latest threads from the subreddit provided in `settings.ini`. This translates to the following command:

```
$ python picker.py
```

# Configuration

GoG picker comes with a `settings.ini` configuration file. In order to run the script, you will need to provide API keys for the following services:

* [Steam](https://steamcommunity.com/dev/apikey)
* [Reddit](https://www.reddit.com/prefs/apps/)
* [Random.org](https://api.random.org/api-keys/beta)

Some of the keys are intended to reference OS environmental variables, but it is okay to enter those values directly into the config file.

The configuration is divided into several sections:

### [general]

General settings that don't fall into more specific categories.

* `replied_to` - a list of threads that the bot has already replied to
* `included_users` - a list of users that can participate in a drawing. If it's empty, every user except those listed in `excluded_users` can participate in the drawing
* `excluded_users` - a list of users excluded from drawings. It is only taken into account if `included_users` is empty

### [steam]

Steam-related settings and [Steam API wrapper](https://github.com/ValvePython/steam) configuration.

* `url` - a Steam community URL
* `min_level` - a minimum [Steam account level](https://support.steampowered.com/kb_article.php?ref=4395-TUZC-9912)

In order to configure the wrapper, you need to provide the following information:

* `api_key` - [a Steam API key](https://steamcommunity.com/dev/apikey)

The wrapper is documented [here](https://steam.readthedocs.io/en/latest/).

### [reddit]

Reddit-related settings and [Python Reddit API Wrapper](https://github.com/praw-dev/praw) configuration.

* `subreddit` - a future-proof setting. It specifies a subreddit which the bot crawls through.
* `tag` - a tag that invokes the bot.
* `required_keywords` - comma-separated keywords that every thread title has to contain. Whitespace characters and capitalization are ignored. Ignored if empty.
* `limit` - limits number of comments fetched at once.
* `min_karma` - minimum Redditor comment [karma](https://www.reddit.com/wiki/faq#wiki_what_is_that_number_next_to_usernames.3F_and_what_is_karma.3F).

API wrapper can be configured using the following settings:

* `client_id` - an unique ID obtainable [here](https://www.reddit.com/prefs/apps)
* `client_secret` - an unique secret phrase obtainable [here](https://www.reddit.com/prefs/apps)
* `username` - a Reddit username
* `password` - a Reddit user password
* `user_agent` - every hit to the Reddit API server have to come with an user agent. Recommended to be left on the default setting.

The wrapper is documented [here](https://praw.readthedocs.io/en/latest/).

### [random]

Random.org-related settings.

* `api_key` - [a Random.org beta API key](https://api.random.org/api-keys/beta)

The wrapper is documented [here](https://github.com/RandomOrg/JSON-RPC-Python).

# License

The GoG Picker is licensed under a permissive [MIT License](LICENSE).
