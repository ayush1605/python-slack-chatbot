import time
from slackclient import SlackClient

Slack_token = "xoxb-726174526851-767145403125-qY5EOLxWvyLvxYBehpNYS2Hf"

sc = SlackClient(Slack_token)

if sc.rtm_connect(with_team_state=False):
    print("Successfully Connected,listening for events")

    while True:
        print(sc.rtm_read())

        time.sleep(1)

else:
    print("Connection Failed")
