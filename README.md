```bash
git push heroku heroku:main
heroku config:set API_HASH=value API_ID=value BOT_API_TOKEN=value
heroku ps:scale worker=1
heroku logs --tail
```