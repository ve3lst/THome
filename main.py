# #!/usr/bin/python3


import xml.etree.ElementTree as ET

tree = ET.parse("sites.xml")
root = tree.getroot()
with open('index.html', 'w') as file:
# tag = 0   tag_text = 1  name = 2   link = 3  image_name = 4  powered_by = 5  description_en = 6  description_ar = 7
    head = f"""
<!DOCTYPE html>

<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>THome!</title>
    <script src="./js/jquery.min.js"></script>
    <link rel="stylesheet" type="text/css" href="./css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="./css/customize.css">    
    <script>
      /* my case senstive search script
      $('.searchbox-input').on('keyup',function () {{
        $('.card').show();
        var filter = $(this).val().toUpperCase();
        $( ".col:not(:contains(" + filter + "))" ).css( 'display','none' );
      }});
      */
      //not my script tho, and its perfect! credit: https://stackoverflow.com/a/61621522
      $(document).ready(function(){{
        $('.searchbox-input').on("keyup", function() {{
          var value = $(this).val().toLowerCase();
          $(".col").filter(function() {{
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
          }});
        }});
      }});
    </script>
  </head>
  <body>
    <header>
      <nav class="navbar">
        <a class="navbar-brand">THome</a>
        <form class="form-inline">
          <input class="form-control searchbox-input" type="search" placeholder="Search" aria-label="Search">
        </form>
      </nav>
    </header>

    <div class="cards ">
      <div class="container">
        <div class="row">
"""
    file.write( head )
# find the first 'item' object
    for child in root:
        #print(child.tag, child.attrib, child[name].text, child[textt].text)
        middle = f"""
          <div class="col">
            <div class="card {child[0].text}">
              <a href="{child[3].text}">
                <div class="media">
                  <div class="media-left">
                    <figure class="applogo">
                      <img src="media/{child[4].text}" width="77" height="77">
                    </figure>
                  </div>
                  <div class="media-content">
                    <div class="tag {child[0].text}">
                      <strong class="tag-text">{child[1].text}</strong>
                    </div>
                    <p class="title {child[0].text}" align="left">{child[2].text}</p>
                    <p class="subtitle" id="powerdby">{child[5].text}</p>
                  </div>
                </div>
                <div class="content">
                  <p class="subtitle en_desc">
                      {child[6].text}
                  </p>
                  <p class="subtitle ar_desc" align="right">
                      {child[7].text}
                  </p>
                </div>
              </a>
            </div>
          </div>"""
        file.write(middle)

    end = f"""
        </div>
      </div>
    </div>

    <footer class="footer">
      <div class="container">
        <p class="float-right">
          <a href="#">Back to the top</a>
        </p>
        <p>Copyright © stuff i don't understand goes here, i think?</p>
      </div>
    </footer>

  </body>
</html>

    """
    file.write(end)

file.close()
