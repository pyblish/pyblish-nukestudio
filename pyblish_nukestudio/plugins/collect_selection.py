import pyblish.api


class CollectSelection(pyblish.api.ContextPlugin):
    """Inject the selection in the context."""

    order = pyblish.api.CollectorOrder - 0.1

    def process(self, context):
        import hiero

        if hasattr(hiero, "selection"):
            context.data["selection"] = hiero.selection
