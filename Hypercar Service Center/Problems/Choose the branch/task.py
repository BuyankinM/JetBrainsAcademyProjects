template = """
<html>
  <div>
      {% if post.author is not None %} {{ post.text }} {% endif %}
  </div>
</html>
"""