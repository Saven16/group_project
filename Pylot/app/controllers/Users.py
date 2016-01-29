from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Moment')

    def index(self):


        return self.load_view('login.html')

    def register(self):
        user_info = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirm_password' : request.form['confirm_password']
        }

        create_status = self.models['User'].register_user(user_info)

        if create_status['status'] == True:
            session['id'] = create_status['user']['id']
            session['name'] = create_status['user']['first_name']
            return redirect('/success')
        else:
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')

    def login(self):
        user_info = {
        'email' : request.form['email'],
        'password' : request.form['password']
        }

        status = self.models['User'].login_user(user_info)

        if status['status'] == False:
            for message in status['errors']:
                flash(message, 'Login_errors')
            return redirect('/')
        else:
            session['id'] = status['user']['id']
            session['name'] = status['user']['first_name']
            return redirect('/success')

    def success(self):
        cats = self.models['Moment'].get_cats()
        return self.load_view('moments.html', cats = cats)

    def logout(self):
        session.clear()
        return redirect('/')
