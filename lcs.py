import random
import os
import jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)
import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']='text/html'
        X = self.request.get('X')
        Y = self.request.get('Y')
        Z = self.request.get('Z')
        W = self.request.get('W')
        URL = gif()
        LCS = across_bridge(X,Y,Z,W)
        jtemplate = JINJA_ENVIRONMENT.get_template('template.jinja2')
        self.response.write(jtemplate.render(X=X, Y=Y, Z=Z, W=W, LCS=LCS, URL=URL))
def across_bridge(X,Y,Z,W):
    people = [int(X),int(Y),int(Z),int(W)]
    people.sort()
    print(people[1])
    x = people[0]+people[1]+people[3]+people[1]+people[1]
    y = people[3]+people[0]+people[2]+people[0]+people[1]
    z = people[3]+people[2]+people[2]+people[1]+people[1]
    results = [x,y,z]
    results.sort()
    return(results[0])


images = [
    "https://media.giphy.com/media/cfuL5gqFDreXxkWQ4o/giphy.gif",
    "https://media.giphy.com/media/W8krmZSDxPIfm/giphy.gif",
    "https://media.giphy.com/media/UxGNvgpU1hoAw/giphy.gif",
    "https://media.giphy.com/media/UxGNvgpU1hoAw/giphy.gif",
    "https://media.giphy.com/media/WLNASdXoq0ZtC/giphy.gif",
    "https://media.giphy.com/media/HYpZKsyLOn1ks/giphy.gif",
    "https://media.giphy.com/media/l8px6snusvpII/giphy.gif",
    "https://media.giphy.com/media/l0Iy9Kry5yhBSwQSs/giphy.gif",
    "https://media.giphy.com/media/7SfAXqgRgh0li/giphy.gif",
    "https://media.giphy.com/media/W80Y9y1XwiL84/giphy.gif"
]
def gif():
    return random.choice(images)

    
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
