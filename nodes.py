class MagikMultiviewPrompter:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Prompt_start": ("STRING", {"multiline": True, "default": ""}),
                "Prompt_end": ("STRING", {"multiline": True, "default": ""}),
                "top_left_view": ("STRING", {"multiline": True, "default": ""}),
                "top_right_view": ("STRING", {"multiline": True, "default": ""}),
                "bottom_left_view": ("STRING", {"multiline": True, "default": ""}),
                "bottom_right_view": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",) * 5
    RETURN_NAMES = (
        "Prompt_multiview",
        "top_left_prompt",
        "top_right_prompt",
        "bottom_left_prompt",
        "bottom_right_prompt",
    )
    FUNCTION = "build_prompts"
    CATEGORY = "prompt/magik"
    DESCRIPTION = (
        "Builds a 2x2 split-screen multiview video prompt plus one single-view "
        "prompt per quadrant. Prompt_multiview describes a fixed 2x2 grid where "
        "all four panels show the same scene and moment from four stationary "
        "camera positions (top_left_view, top_right_view, bottom_left_view, "
        "bottom_right_view), framed by Prompt_start and Prompt_end. Each "
        "quadrant prompt is Prompt_start + that quadrant's view + Prompt_end."
    )

    def build_prompts(
        self,
        Prompt_start,
        Prompt_end,
        top_left_view,
        top_right_view,
        bottom_left_view,
        bottom_right_view,
    ):
        prompt_multiview = f"""
Create a single continuous video presented as a fixed 2x2 split-screen composition. All four quadrants show the exact same physical scene and the exact same moment in time, viewed simultaneously from four different stationary camera positions.

TOP LEFT: {top_left_view}
TOP RIGHT: {top_right_view}
BOTTOM LEFT: {bottom_left_view}
BOTTOM RIGHT: {bottom_right_view}

The four camera views must remain visible throughout the entire video. All cameras observe the same continuous action. Every character movement, gesture, interaction and environmental event must occur at precisely the same time in all four views.

Maintain consistent character identities, clothing, object positions, architecture, lighting, materials and environment across all four quadrants. Each quadrant must have its own distinct camera perspective, with coherent spatial relationships between the views.

Fixed panel positions and equal panel sizes throughout the video. No camera cuts, no transitions, no changing layouts, no duplicated actions, no independent timelines, no text, no borders between views. Photorealistic cinematic rendering with natural motion and coherent perspective.

{Prompt_start}
{Prompt_end}
"""
        top_left_prompt = f"""
{Prompt_start}
{top_left_view}
{Prompt_end}
"""
        top_right_prompt = f"""
{Prompt_start}
{top_right_view}
{Prompt_end}
"""
        bottom_left_prompt = f"""
{Prompt_start}
{bottom_left_view}
{Prompt_end}
"""
        bottom_right_prompt = f"""
{Prompt_start}
{bottom_right_view}
{Prompt_end}
"""
        return (
            prompt_multiview,
            top_left_prompt,
            top_right_prompt,
            bottom_left_prompt,
            bottom_right_prompt,
        )
