def get_page_html(form_data):
    print("About to return page home page...")
    page_html=f"""<!DOCTYPE html>
    <html>

    <head>
    <!-- Include the external css file -->
    <link rel="stylesheet" href="style.css">
</head>

</style>
</head>
<body>

<div class="topnav">
  <a href="/">Level1</a>
  <a href="/b_level_2">level2</a>
  <a href="/b_level_3">level3</a>
</div>

<div class="content">
  <h2>CSS Template</h2>
  <p>Level 3</p>
</div>

<div class="footer">
  <p>Footer</p>
</div>

</body>
</html>
"""
    return page_html