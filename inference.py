from peft import PeftModel
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# load the original model first
MODEL = "deepseek-ai/deepseek-coder-6.7b-base"
# OUTPUT_DIR = "DeepSeekCoder_6.7B_APR_FIM_finetuning"
tokenizer = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)
base_model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    quantization_config=None,
    device_map=None,
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
).cuda()

# merge fine-tuned weights with the base model
# peft_model_id = f"ardalaaan/{OUTPUT_DIR}"
# model = PeftModel.from_pretrained(base_model, peft_model_id)
# model.merge_and_unload()


# def get_code_completion(prefix, suffix):
#     text = f"""<｜fim▁begin｜>{prefix}<｜fim▁hole｜>{suffix}<｜fim▁end｜>"""
#     model.eval()
#     outputs = model.generate(
#         input_ids=tokenizer(text, return_tensors="pt").input_ids.cuda(),
#         max_new_tokens=128,
#         temperature=0.2,
#         top_k=50,
#         top_p=0.95,
#         do_sample=True,
#         repetition_penalty=1.0,
#     )
#     return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]


def infer(text):
    MODEL.eval()
    outputs = MODEL.generate(
        input_ids=tokenizer(text, return_tensors="pt").input_ids.cuda(),
        max_new_tokens=256,
        num_return_sequences=10,
        temperature=0.2,
        top_k=50,
        top_p=0.95,
        do_sample=True,
        repetition_penalty=1.0,
    )
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]


def get_base_code_completion(prefix, suffix):
    psm_text = f"""<｜fim▁begin｜>{prefix}<｜fim▁hole｜>{suffix}<｜fim▁end｜>"""
    spm_text = f"""<｜fim▁begin｜><｜fim▁hole｜>{suffix}<｜fim▁end｜>{prefix}"""
    psm_output = infer(psm_text)
    spm_output = infer(spm_text)
    return psm_output, spm_output


prefix = """public class ADD {
    public static int add(int x, int y) {
// buggy code
//        return x | y;"""
suffix = """
    }
}"""
psm_completion, spm_completion = get_base_code_completion(prefix, suffix)
print(f"PSM inference:\n{psm_completion}\n----------\nSPM_inference:\n{spm_completion}")

