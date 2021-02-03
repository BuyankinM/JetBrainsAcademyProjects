template = """
<html>
  <ul>
  {%for elem in todos %}
    <li> {{ elem }} </li>
  {%endfor%}
  </ul>
</html>
"""