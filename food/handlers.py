from root import app

@app.handle(default=True)
def default(request, responder):
    """This is a default handler."""
    responder.reply('Hello there!')

@app.handle(intent = 'greet')
def prompt_init(request, responder):
    responder.reply("Welcome")
    responder.listen()

@app.handle(intent = 'create_recipe')
def process_recipe(request, responder):
    responder.reply("Create a recipe...")

@app.handle(intent = 'get_allergen')
def prompt_for_allergen(request, responder):
    responder.reply("Ok we have your allergen what's your meal type ?")
    responder.listen()

@app.handle(intent = 'get_diet_type')
def prompt_for_recipe(request, responder):
    responder.reply("Ok we have your diet type what's your food liked ?")
    responder.listen()

@app.handle(intent = 'get_food')
def prompt_for_liked_food(request, responder):
    responder.reply("Ok is everything good now that we have your food ?")
    responder.listen()

@app.handle(intent = 'exit')
def prompt_exit(request, responder):
    responder.reply("Good bye !")

@app.handle(intent = 'get_age')
def prompt_for_(request, responder):
    responder.reply("Ok we have your age -> exercise ?")
    responder.listen()

@app.handle(intent = 'get_exercise')
def prompt_for_(request, responder):
    responder.reply("Ok exercise -> gender")
    responder.listen()

@app.handle(intent = 'get_gender')
def prompt_for_(request, responder):
    responder.reply("Ok gender -> height?")
    responder.listen()


@app.handle(intent = 'get_user_type')
def prompt_for_(request, responder):
    responder.reply("Ok weight ?")
    responder.listen()

@app.handle(intent = 'get_weight&height')
def prompt_for_(request, responder):
    responder.reply("Ok weight -> age ?")
    responder.listen()







