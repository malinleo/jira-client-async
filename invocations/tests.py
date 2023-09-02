import invoke

from . import printing


@invoke.task
def run(context: invoke.Context, params: str = ""):
    """Run django tests with ``extra`` args for ``p`` tests.

    `p` means `params` - extra args for tests
    manage.py test <extra>

    """
    printing.print_success("Tests running")
    return context.run(f"python3 -m pytest {params}")


@invoke.task
def run_ci(context: invoke.Context):
    """Run tests in github actions."""
    run(context, params="-n auto --create-db -v")
