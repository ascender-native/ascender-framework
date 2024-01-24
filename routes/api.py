
from app.http.controllers.controller import Controller, UserController
from core.routing.router import HttpRoute, Route, RouteList
from core.main import app
from app.http.middleware.auth import SimpleMiddleware

route: RouteList = app.make(Route)

# TODO: реализовать проверку get ключей
route.get('/user/', UserController.index)

route.group(prefix="/group1/",  callback = [
    Route.post(path="/1", endpoint=Controller.index),
    Route.get(path="/2", endpoint=Controller.index),

    Route.group(prefix="/group2",  callback=[
        Route.post(path="/3", endpoint=Controller.index),
        Route.group(prefix="/group3",  callback=[
            Route.post(path="/4", endpoint=Controller.index),
        ])
    ]).middleware(SimpleMiddleware)
])