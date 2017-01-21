import web

urls = (
    '/hello', 'Index',
    '/fshello', 'fsindex'
)

app = web.application(urls, globals())

render = web.template.render('templates/')


class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)


class fsindex(object):
    def GET(self):
        return render.famsearch_form()


if __name__ == "__main__":
    app.run()

