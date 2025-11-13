{
    "name": "Awesome MyApp",
    "version": "1.0.0",
    "summary": "Un mini gestionnaire de tâches",
    "author": "Paul",
    "license": "LGPL-3",
    "depends": ["base"],  # + 'mail' si tu veux chatter/suivi
    "data": [
        "security/ir.model.access.csv",
        "views/todo_views.xml",
    ],
    "application": True,   # apparaît comme une app dans le menu
}
