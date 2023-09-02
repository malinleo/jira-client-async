import invoke

from . import pre_commit, printing, tests

##############################################################################
# Build project locally
##############################################################################


@invoke.task
def init(context: invoke.Context):
    """Prepare env for working with project."""
    printing.print_success("Setting up git config")
    pre_commit.install(context)
    tests.run(context)
    pre_commit.run_hooks(context)
