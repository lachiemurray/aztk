from aztk.plugins import PluginDefinition, PluginPort, PluginRunTarget


def definition():
    return PluginDefinition(
        name="rstudio_server",
        ports=[
            PluginPort(
                remote=8787,
                local=8787,
            ),
        ],
        runOn=PluginRunTarget.Master,
        execute="rstudio_server.sh",
        files=[
            "rstudio_server.sh",
        ],
    )