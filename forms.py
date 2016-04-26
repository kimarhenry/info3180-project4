from wtforms import Form,TextField, PasswordField,validators,HiddenField

    

class LoginForm(Form):
	username=TextField('Username', [validators.Length(min=3, max=30),validators.Required()])
	password=PasswordField('New Password',[validators.Required()])

class fetchUrl(Form):
    query=TextField('Enter url to be scraped', [validators.Length(min=3, max=1800),validators.Required()])



class WishInfo(Form):
    category=TextField('Category', [validators.Length(min=3, max=1800),validators.Required()])
    quantity=TextField('Quantity', [validators.Length(min=1, max=1800),validators.Required()])
    hidden=HiddenField('hidden')
    description=TextField('Description', [validators.Length(min=3, max=1800),validators.Required()])

