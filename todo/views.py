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

from database import get_all_user_dbs


def clear_screen():
    os.system("clear")


def quit_ToDo():
    clear_screen()
    print("Thank you.")
    exit()


class BaseView:
    commands = {}
    context = None
    
    def __init__(self, *args, **kwargs) -> None:
        self.populate_commands()

    def populate_commands(self) -> None:
        self.commands["q"] = quit_ToDo

    @staticmethod
    def clear_screen() -> None:
        clear_screen()

    def display_commands(self) -> None:
        print("\nCommands:")
        for key, command in self.commands.items():
            print(f"\t[{key}] {command}")
        print("________________________")


class UserView(BaseView):
    context = "user"

    def populate_commands(self) -> None:
        self.commands["1"] = "create user"
        self.commands["2"] = "set user"
        self.commands["3"] = "delete user"
        super().populate_commands()

    def display_users(self) -> None:
        users = get_all_user_dbs()
        print("getting users")
        for idx, user in enumerate(users):
            print(f"[{idx}] - {user}")


class ToDoListView(BaseView):
    context = "list"


class TaskView(BaseView):
    context = "task"
