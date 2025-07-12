# Custom Wyoming
A custom core component mod that allows you to temporarily trigger the ASR (STT) pipeline without using wake word for **any** assist_satellite device. It does **not require** specific integration or devices like esp32, atom, voice pe etc...

## Installation
##### HACS
HACS > Integrations > 3 dots (upper top corner) > Custom repositories > URL: https://github.com/Steven-Low/custom_wyoming, Category: Integration > Add > wait > Custom Wyoming > Install

##### Manual Install
- manually copy custom_wyoming folder from latest release to /config/custom_components folder.
```
cd /config/custom_components   # ssh to your HA instance first
git clone https://github.com/Steven-Low/custom_wyoming.git
mv custom_wyoming wyoming
```
- Restart your HA.
- Your wyoming devices shall automatically discovered, otherwise add them accordingly:
  1. assist_satelite: 11700 (default port)
  2. openwakeword: 10400
  3. whisper: 10300
  4. piper: 10200

## Service
```
action: wyoming.remote_trigger
data:
  entity_id: assist_satellite.hassmic_wyoming
```

## State
```
wyoming.response_text
```

## Recommended Setup
- Assist Satellite Client: [HassMic](https://github.com/jeffc/hassmic)
- Conversation Agent: [openai_compatible_conversation](https://github.com/Steven-Low/openai_compatible_conversation) (by Steven-Low)

## Roadmap
- [ ] Process audio together with intent (to reduce response time)

## Limitation
- [ ] Edge case like write event error when client disconnected during tts pipeline

# Credits
- https://github.com/rhasspy/wyoming
