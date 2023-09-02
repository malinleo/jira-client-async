import invoke

import invocations

ns = invoke.Collection(
    invocations.pre_commit,
    invocations.project,
    invocations.system,
    invocations.tests,
)

# Configurations for run command
ns.configure(
    {
        "run": {
            "pty": True,
            "echo": True,
        },
    },
)
