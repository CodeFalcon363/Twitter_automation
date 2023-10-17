# Twitter Automation Tool

## Overview

This Python script allows you to automate various Twitter actions using the Twitter API, such as posting tweets, interacting with tweets, and managing user accounts. It is essential to use this tool responsibly and in compliance with Twitter's terms of service.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting Up Twitter API Credentials](#setting-up-twitter-api-credentials)
- [Usage](#usage)
  - [Basic Functions](#basic-functions)
  - [Examples](#examples)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

To use this Twitter automation tool, you need the following prerequisites:

- Python 3.x
- The `tweepy` library (install using `pip install tweepy`)
- Twitter Developer Account with API keys and tokens (see [Setting Up Twitter API Credentials](#setting-up-twitter-api-credentials))

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/twitter-automation.git

2. Navigate to the project directory:
    
    ```bash
    cd twitter-automation
3. Install the required Python packages:
   
    ```bash
    pip install -r requirements.txt


### Setting Up Twitter API Credentials

To interact with the Twitter API, you need to obtain API keys and tokens:

Go to the Twitter Developer platform: https://developer.twitter.com/en/apps
Create a Twitter Developer application and obtain the following credentials:
Consumer Key (API Key)
Consumer Secret (API Secret Key)
Access Token
Access Token Secret
Open the .env file and replace the placeholders with your credentials.


## Usage

### Basic Functions

The Twitter automation tool provides the following basic functions:

post_tweet(text): Posts a tweet with the specified text.
post_media_tweet(text, media_path): Posts a tweet with text and media (image or video).
like_tweet(tweet_id): Likes a tweet by its ID.
user_lookup(username): Looks up a user by their username and displays user information.
follow_user(username): Follows a user by their username.

### Examples

Here are some examples of how to use the functions:

   from twitter_automation import *

  # Post a tweet
  post_tweet("Hello, Twitter!")

  # Post a tweet with media
  post_media_tweet("Check out this cool image!", "path/to/image.jpg")

  # Like a tweet by its ID
  like_tweet(tweet_id)

  # Look up a user
  user_lookup("username")

  # Follow a user
  follow_user("username")


## Error Handling

This Twitter automation tool includes error handling to gracefully handle potential issues that may arise during interactions with the Twitter API. Here's a brief explanation of how errors are managed in the code:

- **Posting a Tweet**: If there's an error while posting a tweet, such as exceeding character limits or connectivity problems, the code will catch the exception and display an error message.

- **Posting a Tweet with Media**: When posting a tweet with media (image or video), the code uploads the media and posts the tweet. If any errors occur during this process, such as media upload failures, it will be caught, and an error message will be displayed.

- **Liking a Tweet**: If there's an issue when attempting to like a tweet by its ID, such as the tweet being unavailable or already liked, the code will catch the exception and provide an error message.

- **Looking Up User(s)**: If there's a problem while looking up user(s) by their usernames, such as invalid usernames or network errors, the code will capture the exception and display an error message.

- **Following a User**: When trying to follow a user by their username, if any issues occur, such as the user not existing or being unreachable, the code will handle the exception and print an error message.

In each case, the code uses the `tweepy.errors.TweepyException` class to capture and handle errors. This ensures that the program continues running smoothly even when errors are encountered, providing informative error messages for troubleshooting.

## Contribution

## License
