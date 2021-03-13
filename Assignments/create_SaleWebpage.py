#
# Create a script that creats and opens an html webpage
#
#

import webbrowser

htmlWeb = open("SummerSale.html", "w")
htmlWeb.write(""" <html> \
                  <body> \
                      <h1> \
                      Stay tuned for our amazing summer sale! \
                      </h1> \
                  </body> \
                </html>
                """)
htmlWeb.close()


webbrowser.open_new_tab('SummerSale.html')

              
