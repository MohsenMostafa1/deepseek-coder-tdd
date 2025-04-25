import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class DeepSeekCoderModel:
    """
    Encapsulates the DeepSeek-Coder model for code generation.
    """

    def __init__(
        self,
        model_name="deepseek-ai/deepseek-coder-6.7b-instruct",
        model_config=None
    ):
        # Default config matches your notebook
        if model_config is None:
            model_config = {
                "torch_dtype": torch.float16,
                "device_map": "auto",
                "low_cpu_mem_usage": True
            }
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, **model_config)

    def generate_code(
        self,
        prompt: str,
        max_new_tokens: int = 512,
        temperature: float = 0.7,
        top_p: float = 0.9,
        do_sample: bool = True,
        repetition_penalty: float = 1.1,
        **kwargs
    ) -> str:
        """
        Generate code from a prompt using DeepSeek-Coder.
        """
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.model.device)
        with torch.no_grad():
            output = self.model.generate(
                input_ids,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                do_sample=do_sample,
                repetition_penalty=repetition_penalty,
                **kwargs
            )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
