from asccore.support.auth.controller import AuthenticationController
from asccore.routing.router import Route, RouteList
from asccore.main import app

route: RouteList = app.make(Route)

route.post('/login', AuthenticationController.login).name('auth.login')
route.post('/register', AuthenticationController.register).name('auth.register')
route.delete('/logout', AuthenticationController.logout).name('auth.logout')