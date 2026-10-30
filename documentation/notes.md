
# Scratchpad

Misc notes and planning for the project

---
## TIME PLANNING

### Mon: 

- ~Setting up repo~
- ~Planning~
- ~Exploratory research~

### Tue: 

- ~Research, reviewing API documentation for GitHub~
- ~Coding exploration. Start hitting endpoints to see data format.~
- ~Refine planning and project scope (maybe decide on bonus approach)~

### Wed:

- ~Main coding and developement. Focus on core features~
- ~Revise where necessary~

### Thu:

- ~Finish most core developement.~
- ~Optimise and debug~
- ~Implement error handling where not yet implemented~
- Implement optional approach if feasable

### Fri:

- ~Final rounding~
- ~Final documenting where necessary~
- ~Testing~

---
## RESEARCH

### GitHub API

docs: 
- https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2026-03-10&tool=curl
- https://docs.github.com/en/rest/pulls/pulls

notes:
- Authenticate using your PAT
- Rate limits usually 5000/h, investigate if certain endpoints gives trouble
- Have implementation of relative pagination (next/prev/first/last page)
- Best practices include ~using webhooks~, handle rate limit errors, etc. (Webhooks not feasable in this repo)

exploratory search:
GET https://api.github.com/repos/home-assistant/operating-system/pulls

GET https://api.github.com/repos/home-assistant/operating-system/pulls/:pull_number/reviews

GET https://api.github.com/repos/home-assistant/operating-system/commits/:ref

### Architecture

Strategy pattern OOP architecture:
https://www.youtube.com/watch?v=Nrwj3gZiuJU

abstract classes and methods refresher:
https://www.youtube.com/watch?v=97V7ICVeTJc

### AI dynamic integrations

notes:
- If integrating with AI, programme must be written with a dynamic OOP structure as to "slot in" any further integration.
