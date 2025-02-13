import falcon
from falcon import App
from wsgiref import simple_server
import os


class AboutMe:
    def on_get(self, req, resp):
        about_me = {
            "name": "Ananda Rauf Maududi",
            "description": "I am a passionate software developer with experience in building web applications and APIs.",
            "email": "anandaraufm@gmail.com"
        }
        resp.media = about_me


class Skills:
    def on_get(self, req, resp):
        skills = {
            "programming_languages": ["Python", "Visual Basic", "Dart"],
            "frameworks": ["Falcon", "Flask", "Sanic", "Flutter", ".Net"],
            "tools": ["Visual Studio Code","Visual Studio Community","PyCharm","Git", "Docker", "DBEaver","Laragon"]
        }
        resp.media = skills


class WorkExperience:
    def on_get(self, req, resp):
        work_experience = [
            {
                "company": "PT Tunas Ridean Tbk",
                "position": "System Engineer",
                "duration": "October 2024 - November 2024",
                "responsibilities": [
                    "Develope new module Odoo 8, New Module is Product Management.",
                    "Customize and modify Module BMW Tunas Odoo 8"
                ]
            },
        ]
        resp.media = work_experience


class Index:
    def on_get(self, req, resp):
        try:
            file_path = os.path.join(os.getcwd(), 'templates', 'index.html')
            with open(file_path, 'r', encoding='utf-8') as f:
                resp.content_type = 'text/html'
                resp.text = f.read() 
        except FileNotFoundError:
            resp.status = falcon.HTTP_404
            resp.text = "File index.html not found"  

class StaticFiles:
    def on_get(self, req, resp, file_name):
        try:
            file_path = os.path.join(os.getcwd(), 'static', file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                resp.content_type = 'text/css'
                resp.text = f.read()  
        except FileNotFoundError:
            resp.status = falcon.HTTP_404
            resp.text = f"File {file_name} not found"  


app = App()

app.add_route('/about-me', AboutMe())
app.add_route('/skills', Skills())
app.add_route('/work-ex', WorkExperience())
app.add_route('/', Index())
app.add_route('/static/{file_name}', StaticFiles())

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)

    print("Server running on http://127.0.0.1:8000")
    httpd.serve_forever()
