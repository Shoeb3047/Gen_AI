from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  
from langchain.schema.runnable import RunnableParallel


load_dotenv()

# Define first prompt 
prompt1 = PromptTemplate(
    template="Generate a easy to understand note of the following .\n {topic}",
    input_variables=["topic"]
)

model = ChatMistralAI(
    model_name="mistral-large-latest",
    temperature=0.1,
)

parser = StrOutputParser()


# Define second prompt
prompt2 = PromptTemplate(
    template="Generate the 5 questions quiz from the following topic.\n {topic}",
    input_variables=["topic"]
)

parallel_chain= RunnableParallel(
    {
        "note": prompt1 | model | parser,
        "quiz": prompt2 | model | parser
    }
)

# prompt3 
prompt3 = PromptTemplate(
    template="Create one single document by merging the follwoing note and quiz. \n {note} \n {quiz}",    
    input_variables=["note", "quiz"]
)

merged_chain = prompt3 | model | parser

chain = parallel_chain | merged_chain

topic = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = chain.invoke({"topic": topic})

print(result)

chain.get_graph().print_ascii()