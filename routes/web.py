from core.routing.router import Route
from app.http.controllers.controller import Controller
from core.main import app

route: Route = app.make(Route)

route.get('/123', Controller.index).middleware()