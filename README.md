# Custom Wyoming
Home assistant custom core component that allows you to trigger the ASR (STT) pipeline without using wake word for any assist_satellite device. You may wonder why am I re-inventing the wheel when there is StreamAssist out there. Well, because the StreamAssist integration is blocking my home assistant frontend from loading the service action. 

## Installation
HACS > Integrations > 3 dots (upper top corner) > Custom repositories > URL: https://github.com/Steven-Low/custom_wyoming, Category: Integration > Add > wait > Custom Wyoming > Install

Or manually copy custom_wyoming folder from latest release to /config/custom_components folder.

## Service
```
action: wyoming.remote_trigger
data:
  entity_id: assist_satellite.hassmic_wyoming
```

## Recommended Setup
- Assist Satellite Client: [HassMic](https://github.com/jeffc/hassmic) 
- Conversation Agent: [openai_compatible_conversation](https://github.com/Steven-Low/openai_compatible_conversation) (by Steven-Low) 

