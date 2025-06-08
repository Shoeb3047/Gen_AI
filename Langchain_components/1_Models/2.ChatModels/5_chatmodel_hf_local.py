from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# import os

# os.environ['HF_HOME'] = 'D:/huggingface_cache'
# device = "cuda" if torch.cuda.is_available() else "cpu"
import torch
if not hasattr(torch, "get_default_device"):
    torch.get_default_device = lambda: "cpu"

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)

