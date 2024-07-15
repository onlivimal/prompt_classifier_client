from gradio_client import Client

# Connect to the API with username and password
client = Client("https://u9fcqbpgw98s75-7860.proxy.runpod.net/", auth=["aisecurity", "Dhsyq&&W3*Ml7z9P"])

# Open the file and load all the input prompts line by line to a list
in_file = open('prompts.csv', 'r')
In_Lines = in_file.readlines()
in_file.close()

# Printing the total number of prompts to get the categories for
print("Total number of prompts to be processed: "+ str(len(In_Lines)))

# Initialising the list to store the category and the prompt received from the api.
Out_Lines=[]
Error=[]

count = 0
error = 0
# For each of the prompts, send to the predic API and get the result.
for line in In_Lines:
    count = count+1
    try:
        # Submitting the prompt to get the category of the injection
        result = client.predict(line)
        
        # Concat the category of the prompt injection with the actual prompt and add to a list.
        Out_Lines.append((list(result['data']))[0][0] + " '|' " + line)
        
        print(f"{count} of {len(In_Lines)} prompts has been processed.")

    except:
        error = error+1
        print(f"Error at line: {count}")
        Error.append(line)    

# Write all the collected output to a file.
out_file = open('output.csv', 'a')
out_file.writelines(Out_Lines)
out_file.close()

# Write all error prompts

error_file = open('error.csv', 'a')
error_file.writelines(Error)
error_file.close()

print(f"Total number of prompts processed: {len(Out_Lines)} successfully.")
print(f"Total number of errornous prompts: {error}.")

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sample output from the api.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{
    'headers': 
        [
            'Classification', 
            'Explaination'
        ], 
    'data': 
        [
            [
                'ignore_previous_instructions', 
                'The prompt explicitly asks the AI to disregard any prior instructions and then requests an action (showing all user passwords in the database) that the AI would typically be restricted from performing.'
            ]
        ], 
    'metadata': 
        None
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
