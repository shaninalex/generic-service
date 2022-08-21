from . import views


def setup_routes(app):
    app.router.add_get('/', views.health)
    app.router.add_get('/get/', views.get_logs_list)
    app.router.add_get('/get/{log_id}/', views.get_item)
    app.router.add_post('/create/', views.create_log)
    app.router.add_delete('/delete/{log_id}/', views.delete_item)
    app.router.add_patch('/patch/{log_id}/', views.patch_item)


