from root import app

@app.handle(default=True)
def default(request, responder):
    """This is a default handler."""
    responder.reply('Hello there!')

@app.handle(intent = 'greet')
def prompt_init(request, responder):
    responder.reply("Welcome")

@app.handle(intent = 'create_recipe')
def process_recipe(request, responder):
    responder.reply("Create a recipe...")

@app.handle(intent = 'get_allergen')
def prompt_for_allergen(request, responder):
    responder.reply("Which allergen do you have ?")

@app.handle(intent = 'get_type_recipe')
def prompt_for_recipe(request, responder):
    responder.reply("Which type of recipe ?")

@app.handle(intent = 'get_food')
def prompt_for_liked_food(request, responder):
    responder.reply("What do you like ?")

@app.handle(intent = 'exit')
def prompt_exit(request, responder):
    responder.reply("Good bye !")