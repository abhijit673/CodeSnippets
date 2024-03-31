#
# Code to 
# 1. Download models from Huggingface on to the local computer
# 2. Integrate with Langchain using the CTransformers package
# 3. Invoke the LLM with a question
# 
# To calculate the size of RAM needed to support a LLM
# RAM requirements = No. of training parameters of the model * 32 / 8
#
# Explanation:
#   Each parameter takes 32 bits in memory and each byte is 8 bits each. So if a model is trained on 1B parameters,
#   the RAM requirements = 1,000,000 * 32 / 8 = 3.81 GB
# So to run this we would need double the RAM
#

import os
from langchain_community.llms import CTransformers
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory


class mistral():

    def __init__(self) -> None:
        self.model_id = "TheBloke/Mistral-7B-codealpaca-lora-GGUF" # Model name
        os.environ["XDG_CACHE_HOME"]="./model/cache" # Where to keep it on the local computer
        self.config = {"temperature":0.0, "context_length":4000}
        self.llm = CTransformers(model = self.model_id,
                  model_type = "llama",
                  config = self.config,
                  callbacks = [StreamingStdOutCallbackHandler()])
        # pass

class tinyllama():

    def __init__(self) -> None:
        self.model_id = "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF" # Model name
        os.environ["XDG_CACHE_HOME"]="./model/cache" # Where to keep it on the local computer
        self.config = {"temperature":0.0, "context_length":4000}
        self.llm = CTransformers(model = self.model_id,
                  model_type = "llama",
                  config = self.config,
                  callbacks = [StreamingStdOutCallbackHandler()])
        # pass

if __name__ == "__main__":
    # model = mistral()
    model = tinyllama()

    model.llm.invoke("Write a function to a dataframe and a column and return a dataframe with all null values converted to 0 in the column")
    print(" ")
    model.llm.invoke("Tell me about yourself")

