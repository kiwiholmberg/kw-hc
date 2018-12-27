# Home automation
Application for home automation. Uses a Nexa Tellstick Duo 433Mhz system.

Webapp built with Next.js (Node.js + React). It was originally [written in Python](https://github.com/kiwiholmberg/kw-hc/tree/legacy-python).

![A really selling image dot png](http://i.imgur.com/ZjaS0or.png)

## Requirements
* TelldusCenter (download at https://telldus.com/resources/)
* Nexa Tellstick or equivalent hardware
* Node >=10 and npm

## Install
* Run `npm install`
* Use `npm run dev` for development.
* For a clean (smaller) build, run `npm run build && npm start`.

## Web interface
Available at http://localhost:3000/ by default.

## API
* `GET /api/devices` - Gets a list of available devices.
* `POST /api/devices/{device-name}/{on|off}` - Control a device

## Notes
* This application has no authentication, I don't recomment exposing it to the internet or to a network with users you don't trust.
