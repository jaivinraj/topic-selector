# Topic Selector <!-- omit in toc -->


Do you ever find yourself with lots of tasks and unsure of the order to do them in? Then this app may be for you!

- [How to use this repo ❓](#how-to-use-this-repo-)
- [ToDo 📝](#todo-)

## How to use this repo ❓

1. Install Docker [here](https://docs.docker.com/get-docker/) (if you don't already have it) 
2. In the terminal, run `docker-compose up -d`
3. Once the container has built (you can check using `docker ps`), bash into it using `docker exec -it topic-selector-2 /bin/bash`
4. Inside the container, run the dashboard using `python src/topic_selector/main.py`
## ToDo 📝

- [x] Create task generator
- [ ] Create probabilistic implementation (based on priority)
- [ ] Create database structure
- [ ] Make the dashboard prettier
- [ ] Allow importing list
- [ ] Allow multiple lists for different sets of tasks