# btt-healthchecks

A [BetterTouchTool](https://folivora.ai/) Trigger for monitoring healthchecks.io cron jobs in your Touch Bar!

## How to Install

1. Create a Shell Script/Task Widget
2. Set Launch Path to your Python 3 location. To find it, run `which python`. For me, it's `~/opt/anaconda3/bin/python`.
3. Set Parameters to `-c`.
4. Paste the contents of [healthchecks.py](healthchecks.py) into the Script field.
5. Replace `INSERT_YOUR_API_KEY_HERE` with your [healthchecks.io](http://www.healthchecks.io) API key.
6. At the very bottom, set Alternate Color Regex to `^down`.
7. Configure Common attributes to fit your theme!

## To do:

- Multiple projects
- Job-specific status widgets
