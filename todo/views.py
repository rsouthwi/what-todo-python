"""
each "view" is basically a menu context, so we can create a command menu
that's specific to each context.  what is common to each view?
    - each view should have an interface that understands commands
    - each view should be able to display the commands it understands
    - each view should refresh the screen to display fresh information
    - each view should have a `back` function to return to the previous view
    - each view should allow a user to `quit` the application

how to process commands?
    - maybe like Django's CBVs where the name of the method matches the key?
    - perhaps each view should have a property that maps the command to the method
    - each command should get delegated to the controller module (not processed in the view)
"""
import os

import controller


class BaseView:
    commands = {}
    context = None
    
    def __init__(self, *args, **kwargs) -> None:
        self.populate_commands()

    def populate_commands(self) -> None:
        self.commands["q"] = controller.quit_ToDo

    @staticmethod
    def clear_screen() -> None:
        controller.clear_screen()


class UserView(BaseView):
    context = "user"

    def populate_commands(self) -> None:
        super().populate_commands()
        self.commands["1"] = "create user"


class ToDoListView(BaseView):
    context = "list"


class TaskView(BaseView):
    context = "task"
