from fasthtml.common import *

# App with custom styling to override the pico defaults
css = Style(':root { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(picolink))
messages = ["This is a message, which will get rendered as a paragraph"]
count = 0

@app.route("/", methods='get')
def home():
    return (Title("Hello World"), 
            Main(H1('Messages'),
                 *[P(msg) for msg in messages], 
                 P(A("Link to Page 2 (to add messages)",href="/page2")),
                 P(A("Or try counting things",href="/counter"))
                 )
    )

@app.route("/", methods="post")
def add_message(data:str):
    messages.append(data)
    return home()


@app.route("/page2", methods="get")
def page2():
    return Main(P("Add a message below:"),
                Form(Input(type="text", name="data"),
                     Button("Submit"),
                     action="/", method="post"))

@app.route("/counter", methods = "get")
def counter():
    return Title("Count Demo"), Main(
        H1("Let's count"),
        P(f"Count is set to {count}", id="count"),
        Button("Increment",
               hx_post="/increment",hx_target="#count", hx_swap="innerHTML")
    )

@app.route("/increment", methods="post")
def increment():
    print("incrementing")
    global count
    count +=1
    return f"Count is set to {count}"



if __name__ == '__main__':
    serve()