Django App To Hold Preferences
===============================

A few Models:

1. Sport Model: Holds each sport, just name of
2. Team Model: Holds Team (as a string), link to sport
3. Fixture Model: Holds a game: link to team, time (string), location (string), date (string)
4. Subscriber Model: One-To-One with user, holds their mobile number, email and pushover client id.

Only One View: The Modify Subscription page, where users can modify their pushover/email/mobile and opt in/out.
- Use Twitter Bootstrap for HTML (leave if don't know)
