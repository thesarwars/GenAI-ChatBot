import re, os
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek

def clean_string(s):
    # Remove \boxed{} wrapper
    s = re.sub(r'\\boxed\{([^}]*)\}', r'\1', s)
    # Remove extra quotes at start/end if present
    s = re.sub(r'^"(.*)"$', r'\1', s)
    # Remove newlines and extra whitespace
    s = ' '.join(s.split())
    return s.strip()

def gen_restaurant_name_and_items(cuisine):
    llm = ChatDeepSeek(
        model="deepseek/deepseek-prover-v2:free",
        temperature=0.6,
        api_key=os.environ.get("api_key"),
        api_base="https://openrouter.ai/api/v1",
    )

    prompt_temp_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for it."
    )

    name_chain = prompt_temp_name | llm | StrOutputParser()

    prompt_temp_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""Suggest some menu items for {restaurant_name}. return it as comma separated list.""",
    )

    def full_chain(input_dict):
        restaurant_name = name_chain.invoke(input_dict)
        food_items = (prompt_temp_items | llm | StrOutputParser()).invoke({"restaurant_name": restaurant_name})
        return {
            "restaurant_name": restaurant_name,
            "menu_items": food_items
        }

    response = full_chain({"cuisine": cuisine})
    
    # Clean the response
    # response["restaurant_name"] = clean_string(response["restaurant_name"])
    # response["menu_items"] = [item.strip() for item in clean_string(response["menu_items"]).split(",")]
    
    return response


if __name__ == "__main__":
    gen_restaurant_name_and_items("Turkish")