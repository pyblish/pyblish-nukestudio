import pyblish.api


class CollectActiveProject(pyblish.api.ContextPlugin):
    """Inject the active project into context"""

    order = pyblish.api.CollectorOrder - 0.1

    def process(self, context):
        import hiero

        context.data["activeProject"] = hiero.ui.activeSequence().project()
