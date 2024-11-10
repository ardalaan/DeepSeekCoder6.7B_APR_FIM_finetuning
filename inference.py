from peft import PeftModel
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from bench_funcs import funcs

# load the original model first
MODEL = "deepseek-ai/deepseek-coder-6.7b-base"
# ADAPTER_DIR = "deepseek-coder-6.7b-base-APR-FIM-finetuning"
tokenizer = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)
base_model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    quantization_config=None,
    device_map=None,
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
).cuda()


def infer(text):
    model.eval()
    outputs = model.generate(
        input_ids=tokenizer(text, return_tensors="pt").input_ids.cuda(),
        max_new_tokens=256,
        # num_return_sequences=10,
        temperature=0.2,
        top_k=50,
        top_p=0.95,
        do_sample=True,
        repetition_penalty=1.0,
    )
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]


def get_code_completion_fim_transform(prefix, suffix):
    prefix = prefix.lstrip('\n').rstrip() + '\n'
    suffix = suffix.lstrip('\n').rstrip() + '\n'
    psm_text = f"""<｜fim▁begin｜>{prefix}<｜fim▁hole｜>{suffix}<｜fim▁end｜>"""
    spm_text = f"""<｜fim▁begin｜><｜fim▁hole｜>{suffix}<｜fim▁end｜>{prefix}"""

    psm_inference = infer(psm_text)
    psm_output = prefix + psm_inference.partition(suffix + "<｜fim▁end｜>")[-1] + suffix

    spm_inference = infer(spm_text)
    spm_output = prefix + spm_inference.partition("<｜fim▁end｜>" + prefix)[-1] + suffix
    return psm_output, spm_output


def get_code_completion_non_transform(prefix, suffix):
    blank_infilling_text = prefix + "<FILL_ME>" + suffix
    blank_infilling_text = blank_infilling_text.lstrip('\n').rstrip() + '\n'
    blank_infilling_inference = infer(blank_infilling_text)
    blank_infilling_output = blank_infilling_inference.partition("<FILL_ME>" + suffix)[-1]
    prefix = prefix.lstrip('\n').rstrip() + '\n'
    suffix = suffix.lstrip('\n').rstrip() + '\n'
    blank_infilling_output = prefix + blank_infilling_output + suffix
    return blank_infilling_output


def set_adapter(peft_model_id):
    peft_model = PeftModel.from_pretrained(base_model, peft_model_id)
    peft_model.merge_and_unload()
    return peft_model


model = base_model
for func in funcs:
    psm_completion, spm_completion = get_code_completion_fim_transform(func["original_prefix"], func["suffix"])
    print(f"base PSM inference:\n{psm_completion}\n----------\nbase SPM inference:\n{spm_completion}\n----------")


model = set_adapter("ardalaaan/deepseek-coder-6.7b-base-APR-FIM-finetuning")
for func in funcs:
    psm_completion, spm_completion = get_code_completion_fim_transform(func["prefix"], func["suffix"])
    print(f"PSM inference:\n{psm_completion}\n----------\nSPM inference:\n{spm_completion}\n----------")
