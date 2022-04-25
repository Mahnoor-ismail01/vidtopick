# vidtopick  

Auto subtitle file generation through machine learning in python

This is the Final Year Project (FYP) of Software Engineering Major Students.

This repo contains a DJANGO based Web App that can generate subtitles of any video by use of Machine Learning model developed by us.

This is the parent repository that automated the <a href="https://github.com/Mahnoor-ismail01/py-srt-generator" target="_blank">Subtitle Generator</a> to be worked as a Web based application easily and effectively.

## How to Run

First Clone the Repo
```ruby
git clone https://github.com/Mahnoor-ismail01/vidtopick.git
cd vidtopick
```

Then clone the Submodules (py-srt-generator)
```ruby
git submodule update --init --recursive
```

Next Install the required dependencies
```ruby
python -m pip install -r py-srt-generator/requirements.txt
```

Finally, Run the Web Server
```ruby
cd vidtopic
python manage.py runserver
```

Your server shall be live at <a href="http://localhost:8000" target="_blank">localhost:8000</a>

Enjoy  :)
