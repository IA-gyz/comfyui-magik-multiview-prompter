from .nodes import MagikMultiviewPrompter

NODE_CLASS_MAPPINGS = {
    "MagikMultiviewPrompter": MagikMultiviewPrompter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MagikMultiviewPrompter": "Magik Multiview Prompter",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
