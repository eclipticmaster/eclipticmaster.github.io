---
layout: default
title: Home
---

<div class="home-section">
  <h2>Meta Posts</h2>
  <ul>
    {% for post in site.categories.meta %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="post-date">— {{ post.date | date: "%B %d, %Y" }}</span>
      </li>
    {% endfor %}
  </ul>
</div>

<div class="home-section">
  <h2>Translations</h2>
  <ul>
    {% for post in site.categories.translations %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="post-date">— {{ post.date | date: "%B %d, %Y" }}</span>
      </li>
    {% endfor %}
  </ul>
</div>

<div class="home-section">
  <h2>Instagram Posts</h2>
  <ul>
    {% for post in site.categories.posts %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="post-date">— {{ post.date | date: "%B %d, %Y" }}</span>
      </li>
    {% endfor %}
  </ul>
</div>

<div class="home-section">
  <h2>Fundamentals</h2>
  <ul>
    {% for post in site.categories.fundamentals %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="post-date">— {{ post.date | date: "%B %d, %Y" }}</span>
      </li>
    {% endfor %}
  </ul>
</div>

<div class="home-section">
  <h2>Random Post</h2>
  <button onclick="goToRandomPost()">Surprise me</button>
</div>

<script>
function goToRandomPost() {
  const posts = [
    {% for post in site.posts %}
      "{{ post.url }}",
    {% endfor %}
  ];
  const random = posts[Math.floor(Math.random() * posts.length)];
  window.location.href = random;
}
</script>