---
layout: default
title: Home
---

## If you enjoy Punjabi music or want to learn more:

{% for post in site.posts.punjabi %}
- [{{ post.title }}]({{ post.url }}) — {{ post.date | date: "%B %d, %Y" }}
{% endfor %}

## If you want to learn how to do other things:

{% for post in site.posts.funessays %}
- [{{ post.title }}]({{ post.url }}) — {{ post.date | date: "%B %d, %Y" }}
{% endfor %}