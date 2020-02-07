import json

### Load and prepare data

with open('includes/auto_links.json') as f:
    auto_links = json.load(f)[0]

with open('includes/profile.json') as f:
    profile = json.load(f)[0]

### Define templates and fill them in

profile_html = """
<div class="profile">
    <div class="profile-left">
        <img class="headshot" align="left" src="%s" alt="Bryant">
        %s
    </div>
</div>
""" % (profile["headshot"], profile["blurb"])

print("Adding speakers:")
with open('includes/speakers.json') as f:
    speakers = json.load(f)
    speakers_list = ""

    for n in speakers[:3]:
        print(n["name"])
        item = '<div class="news-item">'
        item += n["name"] + ", " + n["university"]
        item += '</div>\n\t\t'
        speakers_list += item

speakers_html = """
<div class="section" id="speakers">
    <h3>Speakers</h3>
    <div id="news">
        %s
    </div>
</div>
""" % (speakers_list)

print("Adding organizers:")
with open('includes/organizers.json') as f:
    organizers = json.load(f)
    organizers_list = ""

    for n in organizers[:3]:
        print(n["name"])
        item = '<div class="news-item">'
        item += n["name"] + ", " + n["university"]
        item += '</div>\n\t\t'
        organizers_list += item

organizers_html = """
<div class="section" id="organizers">
    <h3>Organizers</h3>
    <div id="news">
        %s
    </div>
</div>
""" % (organizers_list)

### Put it all together into a coherent index.html

head_html = """
<head>
    <title>Bryant @ CAV 2020</title>
    <link rel="stylesheet" type="text/css" href="main.css">
</head>
"""

body_html = """
<body>
    <div class="hbar"></div>
    %s
    <br><br><br><br><br><br><br><br><br>
    <div class="hbar"></div>
    <center> Home\t About\t Program </center>
    <br>
    <div class="hbar"></div>
    %s
    %s
</body>
""" % (profile_html, speakers_html, organizers_html)

index_html = """
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
%s
%s
</html>
""" % (head_html, body_html)

### Add in the auto links
print("\nAdding links:")
for name in auto_links.keys():
    if name in index_html:
        print(name)
        index_html = index_html.replace(name, "<a href=\"%s\">%s</a>" % (auto_links[name], name))

### Write it to file

with open('index.html', 'w') as index:
    index.write(index_html)


#### Now do the same basically for about

profile_html = """
<div class="profile">
    <div class="profile-left">
        <img class="headshot" align="left" src="%s" alt="Bryant">
        %s
    </div>
</div>
""" % (profile["headshot"], profile["about"])


body_html = """
<body>
    <div class="hbar"></div>
    <center> Home\t About\t Program </center>
    <br>
    <div class="hbar"></div>
    %s
</body>
""" % (profile_html)

index_html = """
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
%s
%s
</html>
""" % (head_html, body_html)

### Add in the auto links
print("\nAdding links:")
for name in auto_links.keys():
    if name in index_html:
        print(name)
        index_html = index_html.replace(name, "<a href=\"%s\">%s</a>" % (auto_links[name], name))

### Write it to file

with open('about.html', 'w') as index:
    index.write(index_html)


#### Now do the same basically for program

program = "TBD"

body_html = """
<body>
    <div class="hbar"></div>
    <center> Home\t About\t Program </center>
    <br>
    <div class="hbar"></div>
    %s
</body>
""" % (program)

index_html = """
<!DOCTYPE html>
<meta charset="UTF-8">
<html>
%s
%s
</html>
""" % (head_html, body_html)

### Add in the auto links
print("\nAdding links:")
for name in auto_links.keys():
    if name in index_html:
        print(name)
        index_html = index_html.replace(name, "<a href=\"%s\">%s</a>" % (auto_links[name], name))

### Write it to file

with open('program.html', 'w') as index:
    index.write(index_html)