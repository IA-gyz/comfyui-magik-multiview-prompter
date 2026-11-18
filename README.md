# ComfyUI Magik Multiview Prompter

Custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that builds
prompts for a fixed **2x2 split-screen multiview video** plus one single-view
prompt per quadrant.

## Install

Clone this repository into ComfyUI's `custom_nodes` directory and restart ComfyUI:

```bash
git clone https://github.com/IA-gyz/comfyui-magik-multiview-prompter.git \
  ComfyUI/custom_nodes/comfyui-magik-multiview-prompter
```

## Usage

Add the **Magik Multiview Prompter** node (category `prompt/magik`) and fill in:

- `Prompt_start` / `Prompt_end` — text framing the scene description
- `top_left_view`, `top_right_view`, `bottom_left_view`, `bottom_right_view` —
  the camera position for each quadrant

Outputs:

- `Prompt_multiview` — one prompt describing a single continuous video shown as a
  fixed 2x2 split-screen, where all four quadrants show the same scene and the
  same moment from the four given camera positions, with `Prompt_start` and
  `Prompt_end` appended
- `top_left_prompt`, `top_right_prompt`, `bottom_left_prompt`,
  `bottom_right_prompt` — per-quadrant prompts of the form
  `Prompt_start` + view + `Prompt_end`, for single-view generations
