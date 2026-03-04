# Copilot Instructions for AI Coding Agents

## Overview
This codebase is focused on streaming and searching Twitter data using the Tweepy library. It consists of three main files:
- **call_streamingAPI.py**: Streams tweets in real-time and saves them to a JSON file.
- **PythonRESTAPI.py**: Searches for recent tweets using the Twitter API v2 and Tweepy Client.
- **Import_data.py**: Currently empty, likely intended for future data import or processing logic.

## Architecture & Data Flow
- **Streaming**: `call_streamingAPI.py` uses a custom `MyStreamListener` class to collect tweets and write them to `FIFA.json`. The stream ends after a set number of tweets (`n_tweets`).
- **REST Search**: `PythonRESTAPI.py` uses Tweepy Client to search for tweets matching a query (e.g., `#Debt -is:retweet`). Results are stored in a list and can be further processed.
- **API Keys**: Credentials are hardcoded in `PythonRESTAPI.py` and left blank in `call_streamingAPI.py`. Consider using a `config.py` or environment variables for security.

## Critical Workflows
- **Streaming Tweets**: Run `call_streamingAPI.py` to start streaming. Tweets are saved to `FIFA.json`.
- **Searching Tweets**: Run `PythonRESTAPI.py` to search for recent tweets. Adjust the `query` variable as needed.
- **No Build/Test Automation**: There are no build scripts, test files, or automation. Run scripts directly with Python.

## Project-Specific Patterns
- **Tweepy Usage**: Both streaming and REST API approaches are used. Streaming uses `tweepy.StreamListener`; REST uses `tweepy.Client`.
- **Data Storage**: Tweets are stored as JSON objects in a list and written to a file.
- **Credential Handling**: Credentials are sometimes commented out or hardcoded. Prefer secure handling.
- **Progress Tracking**: Streaming prints tweet count to terminal for progress monitoring.

## Integration Points
- **Twitter API**: All scripts depend on Tweepy and Twitter API credentials.
- **External Libraries**: Requires `tweepy` and `json`. Install with `pip install tweepy`.

## Examples
- To stream tweets:
  ```python
  python call_streamingAPI.py
  ```
- To search tweets:
  ```python
  python PythonRESTAPI.py
  ```

## Recommendations for AI Agents
- When adding new scripts, follow the pattern of storing tweets as JSON and tracking progress.
- Use environment variables or a `config.py` for credentials.
- Document any new data flows or integration points in this file.
- Reference `call_streamingAPI.py` for streaming logic and `PythonRESTAPI.py` for REST search examples.

---
_Last updated: 2026-02-22_
