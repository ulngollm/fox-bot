## Prepare environment
`cp .env.example .env` and set `.env` variables.  
Set local environment from `.env`: `source .env`  

Set Heroku environment 
```bash 
heroku config:set API_ID=$API_ID API_HASH=$API_HASH BOT_API_TOKEN=$BOT_API_TOKEN`
```

## Deploy
```bash
heroku stack:set container # for docker only https://devcenter.heroku.com/articles/stack
git push heroku heroku-docker:main
heroku ps:scale worker=1 # run app if not running
```