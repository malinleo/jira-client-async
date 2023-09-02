import invoke


@invoke.task
def chown(context: invoke.Context) -> None:
    """Change owner ship of project files to current user.

    Shortcut for owning apps dir by current user after some files were
    generated using docker-compose (migrations, new app, etc).

    """
    context.run("sudo chown -R ${USER}: .")
