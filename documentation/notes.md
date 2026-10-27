
# Scratchpad

Misc notes and planning for the project

---
## TIME PLANNING

### Mon: 

- Setting up repo
- Planning 
- Exploratory research

### Tue: 

- Research, reviewing API documentation for GitHub
- Coding exploration. Start hitting endpoints to see data format.
- Refine planning and project scope (maybe decide on bonus approach)

### Wed:

- Main coding and developement. Focus on core features
- Revise where necessary

### Thu:

- Finish most core developement.
- Optimise and debugging
- Implement error handling where not yet implemented
- Unit Tests
- Implement optional approach if feasable

### Fri:

- Final rounding
- Testing
- Final documenting where necessary

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
- Best practices include using webhooks, handle rate limit errors, etc.

exploratory search:
GET https://api.github.com/repos/home-assistant/operating-system/pulls


### AI dynamic integrations

notes:
- If integrating with AI, programme must be written with a dynamic and OOP structure as to "slot in" any further integration.
