import gc
import unittest

import torch

from diffusers import (
    StableDiffusionInpaintPipeline,
)
from diffusers.utils import load_image
from diffusers.utils.testing_utils import (
    enable_full_determinism,
    require_torch_gpu,
    slow,
)

from .utils import SDSingleFileComponentsTesterMixin


enable_full_determinism()


@slow
@require_torch_gpu
class StableDiffusionInpaintPipelineSingleFileSlowTests(unittest.TestCase, SDSingleFileComponentsTesterMixin):
    pipeline_class = StableDiffusionInpaintPipeline
    ckpt_path = "https://huggingface.co/runwayml/stable-diffusion-inpainting/blob/main/sd-v1-5-inpainting.ckpt"
    original_config = "https://raw.githubusercontent.com/runwayml/stable-diffusion/main/configs/stable-diffusion/v1-inpainting-inference.yaml"
    repo_id = "runwayml/stable-diffusion-inpainting"

    def setUp(self):
        super().setUp()
        gc.collect()
        torch.cuda.empty_cache()

    def tearDown(self):
        super().tearDown()
        gc.collect()
        torch.cuda.empty_cache()

    def get_inputs(self, device, generator_device="cpu", dtype=torch.float32, seed=0):
        generator = torch.Generator(device=generator_device).manual_seed(seed)
        init_image = load_image(
            "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main"
            "/stable_diffusion_inpaint/input_bench_image.png"
        )
        mask_image = load_image(
            "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main"
            "/stable_diffusion_inpaint/input_bench_mask.png"
        )
        inputs = {
            "prompt": "Face of a yellow cat, high resolution, sitting on a park bench",
            "image": init_image,
            "mask_image": mask_image,
            "generator": generator,
            "num_inference_steps": 3,
            "guidance_scale": 7.5,
            "output_type": "np",
        }
        return inputs

    def test_single_file_format_inference_is_same_as_pretrained(self):
        super().test_single_file_format_inference_is_same_as_pretrained(expected_max_diff=1e-3)


class StableDiffusion21InpaintPipelineSingleFileSlowTests(unittest.TestCase, SDSingleFileComponentsTesterMixin):
    pipeline_class = StableDiffusionInpaintPipeline
    ckpt_path = "https://huggingface.co/stabilityai/stable-diffusion-2-1/blob/main/v2-1_768-ema-pruned.safetensors"
    original_config = "https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference-v.yaml"
    repo_id = "stabilityai/stable-diffusion-2-inpainting"

    def setUp(self):
        super().setUp()
        gc.collect()
        torch.cuda.empty_cache()

    def tearDown(self):
        super().tearDown()
        gc.collect()
        torch.cuda.empty_cache()

    def get_inputs(self, device, generator_device="cpu", dtype=torch.float32, seed=0):
        generator = torch.Generator(device=generator_device).manual_seed(seed)
        init_image = load_image(
            "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main"
            "/stable_diffusion_inpaint/input_bench_image.png"
        )
        mask_image = load_image(
            "https://huggingface.co/datasets/diffusers/test-arrays/resolve/main"
            "/stable_diffusion_inpaint/input_bench_mask.png"
        )
        inputs = {
            "prompt": "Face of a yellow cat, high resolution, sitting on a park bench",
            "image": init_image,
            "mask_image": mask_image,
            "generator": generator,
            "num_inference_steps": 3,
            "guidance_scale": 7.5,
            "output_type": "np",
        }
        return inputs

    def test_single_file_format_inference_is_same_as_pretrained(self):
        super().test_single_file_format_inference_is_same_as_pretrained(expected_max_diff=1e-3)
