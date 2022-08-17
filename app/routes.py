from . import views


def setup_routes(app):
    app.router.add_get('/', views.health)
    app.router.add_get('/get/', views.get_logs_list)
    # app.router.add_get('/get/{log_id}/', views.get_log_by_id)
    # app.router.add_get('/create/', views.create_log)

