import json
filtered_result = []
dict_example = {"rates": {"CAD": 100, "JPY": 10, "USD": 1}}
json_response = json.dumps(dict_example)
loaded_json = json.loads(json_response)
quotes = ["CAD", "JPY", "USD"]
def try_again():
    for i in range(len(quotes)):
        quote = quotes[i]
        result =(f"{quote}: {loaded_json["rates"][quote]}")
        filtered_result.append(result)
    return filtered_result

real_result = try_again()
print(real_result)