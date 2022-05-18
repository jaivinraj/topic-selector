# Topic Selector <!-- omit in toc -->


Do you ever find yourself with lots of tasks and unsure of the order to do them in? Then this app may be for you!

- [How to use this repo ❓](#how-to-use-this-repo-)
- [Background 📖](#background-)
- [ToDo 📝](#todo-)

## How to use this repo ❓

1. Install Docker [here](https://docs.docker.com/get-docker/) (if you don't already have it) 
2. In the terminal, run `docker-compose up -d` (Note: if a new version has been released, you may need to rebuild the image. This can be done using `docker-compose build --no-cache`)
3. Once the container has built (you can check using `docker ps`), bash into it using `docker exec -it topic-selector-2 /bin/bash`
4. Inside the container, run the dashboard using `python src/topic_selector/main.py`
5. Follow the link to http://0.0.0.0:8050/ and you can access the dashboard

## Background 📖

I initially made this for my younger brother when he was revising for exams. He had so many topics to revise in maths and it got pretty overwhelming! There was always a temptation to just revise the topics he liked and neglect the harder ones. I realised that I could use some automation to take this choice out of his hands. The model would be more likely to recommend topics that he finds difficult (has a low rating in) but would still sometimes recommend the easier topics to give a confidence boost!
## ToDo 📝

- [x] Create task generator
- [x] Create probabilistic implementation (based on priority)
- [ ] Create database structure
- [ ] Make the dashboard prettier
- [ ] Allow importing list
- [ ] Allow multiple lists for different sets of tasks
