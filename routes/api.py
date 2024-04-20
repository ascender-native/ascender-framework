
from app.http.controllers.controller import Controller, UserController
from asccore.routing.router import HttpRoute, Route, RouteList
from asccore.main import app
from asccore.support.auth.middleware import JWTAuthentication

route: RouteList = app.make(Route)

route.get('/user/{user}', UserController.index).name('home')

route.group(prefix="/group1/",  callback = [
    Route.post(path="/1", endpoint=Controller.index).name('group1.1'),
    Route.get(path="/1", endpoint=Controller.index).name('group1.2'),

    Route.group(prefix="/group2",  callback=[
        Route.post(path="/3", endpoint=Controller.index).name('group2.group1.1'),
        Route.group(prefix="/group3",  callback=[
            Route.post(path="/4", endpoint=Controller.index).name('group2.group2.2'),
        ])
    ])
]).middleware(JWTAuthentication)